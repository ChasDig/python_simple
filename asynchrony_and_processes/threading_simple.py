import threading
import time
import random


# ---------------------------------------------------------------------------------------------------------------------#
def get_data(data, thread):
    # Получаем текущий поток:
    for _ in range(thread):
        print(f"[{threading.current_thread().name}]: {data}")
        time.sleep(1)


thread_list = []
for thread in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), thread, ), name=f"thr-{thread}")
    thread_list.append(thr)
    thr.start()
#  Ожидание выполнения потоков по индексу- блокировка кода:
for thread in thread_list:
    thread.join()

print("END!")


# ---------------------------------------------------------------------------------------------------------------------#
# Поток daemon:

def get_data(data):
    for _ in range(5):
        print(f"[{threading.current_thread().name}]: {data}")
        time.sleep(1)


thr_1 = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1.1", daemon=True)
# thr_1.setDaemon(True)
thr_1.start()
print("finish")


# ---------------------------------------------------------------------------------------------------------------------#
# # Блокировщики Lock и RLock:

g_value = 0
# Имеется возможность разблокировать поток:
lock = threading.Lock()
# Нельзя разблокировать поток. Разблокирует только тот поток, что заблокировал его:
rlock = threading.RLock()


def inc_g_value():
    global g_value
    for _ in range(100):
        # Блокируем участок кода для других потоков:
        with lock:
            print(f"{g_value} - [{threading.current_thread().name}]")
            g_value += 1
            time.sleep(0.01)


for item in range(5):
    threading.Thread(target=inc_g_value,  name=f"thr-{item}").start()


# ---------------------------------------------------------------------------------------------------------------------#
# Timer в потоках:

def test_timer():
    while True:
        print("test")
        time.sleep(1)


thr = threading.Timer(interval=5, function=test_timer)
thr.start()
# Отменяет таймер до его начала:
# thr.cancel()
while True:
    print("!!!")
    time.sleep(2)


# ---------------------------------------------------------------------------------------------------------------------#
# Хранилище Local:
# Хранилища доступны только внутри ОДНОГО потока:


data = threading.local()


def get_data():
    print(f"thr_{data.thr}: {data.value}")


def data_1():
    data.value = threading.current_thread().name
    data.thr = 1
    get_data()


def data_2():
    data.value = threading.current_thread().name
    data.thr = 2
    get_data()


thr_1 = threading.Thread(target=data_1).start()
thr_2 = threading.Thread(target=data_2).start()


# ---------------------------------------------------------------------------------------------------------------------#
# Семафоры и Барьеры - синхронизация потоков:
# Семафор - количество потоков, которые одновременно могут использовать семафор. Остальным потокам придется ждать:

max_connection = 6
pool = threading.BoundedSemaphore(value=max_connection)


def semaphore_test():
    with pool:
        print(f"[{threading.current_thread().name}]")
        time.sleep(6)


for item in range(10):
    threading.Thread(target=semaphore_test, name=f"thr-{item}").start()


# ---------------------------------------------------------------------------------------------------------------------#
# Барьер - ожидаем запуска и выполнение некоторых действий определенного количества потоков. Пока все эти потоки не
# дойдут до этого момента, ни один из них не продолжит выполнение программы:


def barrier_test(barrier):
    slp = random.randint(1, 6)
    print(f"[{threading.current_thread().name}] - запущен в {time.ctime()} и ожидает {slp} секунд")
    time.sleep(slp)
    barrier.wait()
    print(f"[{threading.current_thread().name}] - преодолел барьер в {time.ctime()}")


bar = threading.Barrier(5)
for item in range(5):
    threading.Thread(target=barrier_test, args=(bar,), name=f"thr-{item}").start()
