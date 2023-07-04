import zmq

host = "127.0.0.1"
port = 6789
topics = ["Stark", "Winchester"]

sub = zmq.Context()
connect = sub.socket(zmq.SUB)
connect.connect("tcp://%s:%s" % (host, port))

print("ZMQ Подписчик готов получать рассылки...")

for topic in topics:
    connect.setsockopt(zmq.SUBSCRIBE, topic.encode("utf-8"))

while True:
    s_bytes, f_bytes = connect.recv_multipart()
    s_text = s_bytes.decode("utf-8")
    f_text = f_bytes.decode("utf-8")
    print(f"ZMQ Подписчик получил для фамилии {s_text} имя {f_text}...")
