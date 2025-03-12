import socket
from datetime import datetime

# Function to scan a range of ports
def scan_ports(target_ip, port_range):
    print(f"Starting port scan on {target_ip}...")
    print(f"Scanning ports {port_range[0]} to {port_range[1]}")
    print("-" * 50)

    # Record the start time
    start_time = datetime.now()

    # Scan the specified range of ports
    for port in range(port_range[0], port_range[1] + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        # Try to connect to the port
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is open")
        sock.close()

    # Record the end time
    end_time = datetime.now()

    # Display the time taken for the scan
    scan_duration = end_time - start_time
    print(f"Scan completed in {scan_duration}")

# Get target IP and port range
target_ip = input("Enter the IP address to scan: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

# Scan the given range of ports
scan_ports(target_ip, (start_port, end_port))
