import socket
import datetime

server_address = ("127.0.0.1", 6789)
max_size = 4096
QUEUE = 5
text_answer = b"The server received a message..."

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen(QUEUE)

client, _ = server.accept()
data = client.recv(max_size)

print(f"Server at {datetime.datetime.now()} got a message '{data}' from {client}...")

client.sendall(text_answer)
client.close()
server.close()
