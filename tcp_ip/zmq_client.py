import zmq

host = "127.0.0.1"
port = 6789

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))
print("Клиент запущен...")

for number in range(1, 6):
    request_text = "Message num. %s" % number
    request_bytes = request_text.encode("utf-8")
    client.send(request_bytes)
    print("Клиент отправил сообщение: %s" % request_text)
    response_bytes = client.recv()
    response_text = response_bytes.decode("utf-8")
    print("Клиент получил ответ %s", response_text)
