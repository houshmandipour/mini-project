import socket

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

print("IP address is : ", ip)
