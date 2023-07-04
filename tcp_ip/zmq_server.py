import zmq

host = "127.0.0.1"
port = 6789

context = zmq.Context()
server = context.socket(zmq.REP)

server.bind("tcp://%s:%s" % (host, port))
print("Сервер запущен...")

while True:
    request_bytes = server.recv()
    request_text = request_bytes.decode("utf-8")
    print("Сервер получил запрос: %s" % request_text)
    response_text = "Ответ сервера на запрос: %s" % request_text
    response_bytes = response_text.encode("utf-8")
    server.send(response_bytes)
