import socket  # Required for network connections
import sys     # Required for system actions like exiting the script

try:
    # Create a socket: AF_INET = IPv4, SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print(f"Socket creation failed with error {err}")
    sys.exit(1)

# Target port (80 is default for standard HTTP)
port = 80


try:
    # Resolve the domain name (URL) to an IP address (DNS lookup)
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror as err:
    # Handle address/DNS resolution errors and stop execution
    print(f"Error occurred while fetching IP address: {err}") 
    sys.exit(1)


try:
    # Connect to the target server using a tuple: (IP, port)
    s.connect((host_ip, port))
    print(f"The socket has successfully connected to google on {host_ip}:{port}")
except socket.error as err:
    # Handle connection failures (e.g., timeout, server offline)
    print(f"Connection failed: {err}")
    sys.exit(1)
finally:
    # Always close the socket to free up system resources
    s.close()
    print("Socket closed successfully.")