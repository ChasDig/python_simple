# gevent - зеленый поток (greenlet). Главная особенность - не блакируется.
# Т.е. при ошибке переключает выполнение задачи на другой зеленый поток.
import gevent
from gevent import socket

hosts = ["www.pythonist.ru", "www.python.org", "www.tproger.ru"]

# Listcomp: ассинхронный запуск gethostbyname благодаря 'зеленым' потокам из библиотеки gevent:
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
# Ожидаем выполнения всех созданных задач:
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
