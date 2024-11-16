import dns.resolver
import dns.query
import dns.name
import dns.update
import socket
import time
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(filename='dns_sinkhole_service.log', level=logging.INFO, format='%(asctime)s %(message)s')

SINKHOLE_IP = '192.168.1.1'  # Replace with the IP that will be used as the sinkhole
MALICIOUS_DOMAINS = [
    "badexample.com",
    "maliciousdomain.com",
    "phishingattack.net",
    "ransomware-site.org"
]

@app.route('/dns-query', methods=['GET'])
def dns_query():
    domain = request.args.get('domain')
    client_ip = request.remote_addr
    if not domain:
        return jsonify({"error": "Domain parameter is required."}), 400

    # Check if domain is in the malicious list
    if domain in MALICIOUS_DOMAINS:
        logging.info(f"Sinkhole redirection triggered for domain: {domain} by client: {client_ip}")
        return jsonify({"redirect_to": SINKHOLE_IP}), 200
    
    # Normal resolution
    try:
        resolver = dns.resolver.Resolver()
        answer = resolver.resolve(domain, 'A')
        resolved_ip = [str(rdata) for rdata in answer]
        logging.info(f"Domain {domain} resolved normally to {resolved_ip} for client: {client_ip}")
        return jsonify({"resolved_ip": resolved_ip}), 200
    except Exception as e:
        logging.error(f"Error resolving domain {domain}: {e}")
        return jsonify({"error": "Failed to resolve domain."}), 500

@app.route('/add-malicious', methods=['POST'])
def add_malicious_domain():
    new_domain = request.json.get("domain")
    if not new_domain:
        return jsonify({"error": "Domain is required."}), 400
    
    MALICIOUS_DOMAINS.append(new_domain)
    logging.info(f"Domain {new_domain} added to malicious list.")
    return jsonify({"message": "Domain added to malicious list."}), 200

@app.route('/list-malicious', methods=['GET'])
def list_malicious_domains():
    return jsonify({"malicious_domains": MALICIOUS_DOMAINS}), 200

# DNS sinkhole handler (simulated)
def sinkhole_dns_query(domain):
    logging.info(f"DNS sinkhole invoked for domain: {domain}")
    # Simulated reroute to sinkhole IP
    return SINKHOLE_IP

if __name__ == "__main__":
    print("Starting DNS Sinkhole Service...")
    app.run(host='0.0.0.0', port=5000, debug=True)
