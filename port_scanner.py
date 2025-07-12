import socket
import sys
import argparse
import time


def scan_port(host, port, timeout=1):
    """
    Attempts to connect to a specific port on a host.

    Args:
        host (str): The target IP address or hostname.
        port (int): The port number to scan.
        timeout (int): The maximum time in seconds to wait for a connection.

    Returns:
        bool: True if the port is open, False otherwise.
    """
    global sock
    try:
        # Create a new socket. AF_INET is for IPv4, SOCK_STREAM is for TCP.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)  # Set a timeout for the connection attempt

        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))  # connect_ex returns an error indicator

        if result == 0:
            return True  # Port is open
        else:
            return False  # Port is closed or filtered
    except socket.gaierror:
        print(f"Error: Hostname '{host}' could not be resolved.")
        return False
    except socket.error as e:
        print(f"Socket error while scanning port {port}: {e}")
        return False
    finally:
        sock.close()  # Always close the socket


def main():
    """
    Main function to parse arguments and run the port scan.
    """
    parser = argparse.ArgumentParser(description="A simple Python port scanner.")
    parser.add_argument("target", help="The target IP address or hostname to scan.")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="Port range to scan (e.g., '1-100', '80,443', or '22'). Default is 1-1024.")
    parser.add_argument("-t", "--timeout", type=float, default=1.0,
                        help="Connection timeout in seconds. Default is 1.0.")

    args = parser.parse_args()

    target_host = args.target
    port_range_str = args.ports
    timeout = args.timeout

    print(f"[*] Scanning target: {target_host}")
    print(f"[*] Port range: {port_range_str}")
    print(f"[*] Timeout per port: {timeout} seconds")
    print("-" * 30)

    try:
        # Resolve hostname to IP address if necessary
        target_ip = socket.gethostbyname(target_host)
        print(f"[*] Resolved {target_host} to {target_ip}")
    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname '{target_host}'. Exiting.")
        sys.exit(1)

    ports_to_scan = []
    if '-' in port_range_str:
        try:
            start_port, end_port = map(int, port_range_str.split('-'))
            ports_to_scan.extend(range(start_port, end_port + 1))
        except ValueError:
            print("[-] Error: Invalid port range format. Use 'start-end'.")
            sys.exit(1)
    elif ',' in port_range_str:
        try:
            ports_to_scan.extend(map(int, port_range_str.split(',')))
        except ValueError:
            print("[-] Error: Invalid comma-separated ports. Use 'port1,port2,...'.")
            sys.exit(1)
    else:
        try:
            ports_to_scan.append(int(port_range_str))
        except ValueError:
            print("[-] Error: Invalid single port number.")
            sys.exit(1)

    open_ports = []
    start_time = time.time()

    for port in sorted(list(set(ports_to_scan))):  # Sort and unique ports
        print(f"Scanning port {port}...", end='\r')  # Print on same line to show progress
        if scan_port(target_ip, port, timeout):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        # else:
        #     print(f"[-] Port {port} is CLOSED/FILTERED") # Uncomment for verbose output

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n" + "-" * 30)
    if open_ports:
        print(f"[*] Scan complete. Open ports found: {', '.join(map(str, open_ports))}")
    else:
        print("[*] Scan complete. No open ports found in the specified range.")
    print(f"[*] Scan took {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    main()
