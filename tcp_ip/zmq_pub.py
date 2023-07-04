import zmq
import random
import time

host = "127.0.0.1"
port = 6789

second_name = ["Fisher", "Winchester", "Dilan", "Smit", "Stark"]
first_name = ["Alex", "Bob", "Frank", "Fred", "Anna"]

ctx = zmq.Context()
connect = ctx.socket(zmq.PUB)
connect.bind("tcp://%s:%s" % (host, port))
time.sleep(1)
print("Сервер Zmq готов к отправке публикаций...")

for number in range(10):
    s_text = random.choice(second_name)
    s_byte = s_text.encode("utf-8")
    f_text = random.choice(first_name)
    f_byte = f_text.encode("utf-8")
    print(f"Сервер Zmq отправляет сообщение с именен {f_text} для фамилий {s_text}...")
    connect.send_multipart([s_byte, f_byte])
    