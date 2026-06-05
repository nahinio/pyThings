import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname("www.google.com")  # Get the IP address of the host
print(f"IP address of www.google.com: {ip}")

