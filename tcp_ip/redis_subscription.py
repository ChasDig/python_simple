import redis

topics = ["Stark", "Winchester"]

connect = redis.Redis()
sub = connect.pubsub()
sub.subscribe(topics)

print("Клиент готов получать сообщения только по определенным подпискам (фамилиям)...")

for message in sub.listen():
    if message["type"] == "message":
        s_name = message["channel"]
        f_name = message["data"]
        print("Клиент получил для фамилии(подписки) %s имя(данные по данной подписке) '%s'..." % (s_name, f_name))
