import socket
import datetime

server_address = ("127.0.0.1", 6789)
max_size = 4096
text_send = b"Hello, server!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

client.sendall(text_send)
print(f"Client send '{text_send}' to {server_address} at {datetime.datetime.now()}...")

data = client.recv(max_size)
print(f"Client at {datetime.datetime.now()} got a message '{data}' from Server...")
client.close()
