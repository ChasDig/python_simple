import socket
import datetime

server_address = ("127.0.0.1", 6789)
max_size = 4096
text_answer = b"The server received a message..."

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)
print("Server was start...")

data, client = server.recvfrom(max_size)
print(f"Server at {datetime.datetime.now()} got a message '{data}' from {client}...")

server.sendto(text_answer, client)
server.close()
