import redis
import random

second_name = ["Fisher", "Winchester", "Dilan", "Smit", "Stark"]
first_name = ["Alex", "Bob", "Frank", "Fred", "Anna"]
connect = redis.Redis()

for message in range(10):
    s_name = random.choice(second_name)
    f_name = random.choice(first_name)
    print(f"Отправлена рассылка: для фамилии %s было отправлено имя %s" % (s_name, f_name))
    connect.publish(s_name, f_name)
