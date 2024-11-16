### Cloud-Based DNS Sinkhole Service

#### Introduction
This cloud-based DNS sinkhole service is designed to help companies mitigate malicious domains within their networks. When a client attempts to access a known malicious domain, the traffic is rerouted to a sinkhole IP address. This allows organizations to safely mitigate threats by preventing access to malicious resources and logging attempted access.

#### Features
- **Sinkhole IP Redirection**: Redirects DNS queries for known malicious domains to a designated sinkhole IP.
- **Logging and Monitoring**: Logs every redirection attempt for later analysis.
- **Malicious Domain Management**: Allows adding domains to the malicious list and querying the current list.
- **REST API**: Provides a simple REST API for companies to integrate with the service.

#### Usage Instructions
1. **Setup Dependencies**: Install necessary Python packages using `pip`.
    ```sh
    pip install Flask dnspython
    ```
2. **Run the Service**: Start the DNS Sinkhole Service using the command.
    ```sh
    python dns_sinkhole_service.py
    ```
3. **Endpoints**:
   - **DNS Query Endpoint**: `GET /dns-query`
     - **Parameters**: `domain` (the domain name to be resolved)
     - **Returns**: Either the resolved IP address or the sinkhole IP if the domain is malicious.
   - **Add Malicious Domain**: `POST /add-malicious`
     - **Body**: `{ "domain": "maliciousdomain.com" }`
     - **Action**: Adds the given domain to the malicious list.
   - **List Malicious Domains**: `GET /list-malicious`
     - **Returns**: A list of currently flagged malicious domains.

#### Prerequisites
- **Python 3.6 or above**: Ensure you have Python installed in your system.
- **Sinkhole IP Setup**: Replace `SINKHOLE_IP` in the script with your configured sinkhole IP.

#### How It Works
1. **Domain Query**: The client sends a domain query request to the `/dns-query` endpoint.
2. **Redirection Logic**: If the queried domain is on the malicious list, the client receives the `SINKHOLE_IP` as the response. Otherwise, the domain is resolved normally using a DNS resolver.
3. **Management API**: The service allows adding and listing malicious domains using API calls.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Use `pip install -r requirements.txt` to install all required dependencies.
3. **Run the Tool**: Execute `python dns_sinkhole_service.py` to start the DNS sinkhole service.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This tool is intended for educational purposes and internal organizational use. Users are responsible for ensuring compliance with applicable laws and regulations before deploying or using this DNS sinkhole in production environments.
