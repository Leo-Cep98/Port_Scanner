# Python Basic Network Scanner (Port Scanner)

## Project Overview

This project is a command-line tool written in Python that functions as a basic network port scanner. It allows users to scan a target host (IP address or hostname) for open TCP ports within a specified range. This tool demonstrates fundamental networking concepts, the use of Python's `socket` module, argument parsing, and basic error handling, crucial skills in network security and system administration.

## Features

* **Target Specification:** Scan any valid IP address or resolvable hostname.
* **Custom Port Ranges:** Specify a single port, a comma-separated list of ports, or a range of ports to scan (e.g., `80`, `22,80,443`, `1-1024`).
* **Configurable Timeout:** Set a connection timeout for each port to control scan speed and prevent hanging on filtered ports.
* **Open Port Detection:** Identifies and reports ports that are actively listening for connections.
* **Hostname Resolution:** Automatically resolves hostnames to IP addresses.
* **Scan Summary:** Provides a summary of open ports and the total scan time.

## Cybersecurity Concepts Demonstrated

* **Network Reconnaissance:** Port scanning is a fundamental step in understanding a target's network footprint and identifying potential entry points.
* **TCP/IP Fundamentals:** Direct interaction with TCP sockets illustrates the underlying mechanics of network connections.
* **Ports and Services:** Understanding that open ports often correspond to running network services, which can have vulnerabilities.
* **Firewalls (Implicit):** Closed or filtered ports can indicate the presence of firewalls or other security measures.
* **Socket Programming:** Demonstrates how programs can interact with the network stack.

## How to Run

1.  **Save the file:** Save the Python code as `port_scanner.py`.

2.  **Open your terminal or command prompt.**

3.  **Navigate to the directory** where you saved `port_scanner.py`.

4.  **Run the script from the command line:**

    * **Basic Scan (default ports 1-1024):**
        ```bash
        python port_scanner.py example.com
        # OR
        python port_scanner.py 192.168.1.1
        ```

    * **Scan a specific port:**
        ```bash
        python port_scanner.py example.com -p 80
        ```

    * **Scan a range of ports:**
        ```bash
        python port_scanner.py example.com --ports 1-100
        ```

    * **Scan a comma-separated list of ports:**
        ```bash
        python port_scanner.py example.com -p 22,80,443
        ```

    * **Adjust timeout:**
        ```bash
        python port_scanner.py example.com -p 1-100 -t 0.5
        ```

## Example Usage

```bash

$ python port_scanner.py scanme.nmap.org -p 20-100 [] Scanning target: scanme.nmap.org [] Port range: 20-100 [*] Timeout per port: 1.0 seconds
[*] Resolved scanme.nmap.org to 45.33.32.178 Scanning port 20... Scanning port 21... Scanning port 22... [+] Port 22 is OPEN Scanning port 23... ... Scanning port 80... [+] Port 80 is OPEN Scanning port 81... ...
[] Scan complete. Open ports found: 22, 80
[] Scan took 81.23 seconds.

```

___

## Technologies Used

* **Python 3**
* **`socket` module:** For low-level network communication (TCP connections).
* **`sys` module:** For exiting the script on critical errors.
* **`argparse` module:** For parsing command-line arguments, making the script user-friendly.
* **`time` module:** For calculating scan duration.

## Important Considerations

* **Ethical Hacking:** Only scan hosts and networks you have explicit permission to scan. Unauthorized port scanning can be considered illegal and disruptive.
* **Rate Limiting:** Aggressive scanning can trigger intrusion detection systems (IDS) or be blocked by firewalls. This simple script does not implement any rate-limiting.
* **TCP Only:** This scanner only checks for TCP ports. UDP ports require a different approach.

## Future Enhancements (Ideas for Personal Learning)

* **Concurrency:** Implement multithreading or asyncio to scan multiple ports simultaneously, significantly speeding up the scan process.
* **Service Banner Grabbing:** After detecting an open port, attempt to read a small amount of data from the service to identify its version or type (e.g., HTTP server, SSH server).
* **UDP Scanning:** Extend the scanner to include UDP port scanning.
* **OS Detection (Passive):** Based on open ports or banner grabs, attempt to make an educated guess about the target's operating system.
* **Verbose Output:** Add options for more detailed output (e.g., showing closed/filtered ports).
* **Output to File:** Save scan results to a file (e.g., TXT, CSV, JSON).
* **Ping Scan (Host Discovery):** Before port scanning, perform a basic ping sweep to identify active hosts on a network.