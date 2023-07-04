import multiprocessing
import random
import time

# ---------------------------------------------------------------------------------------------------------------------#
# Многопроцессорность:


def mpr_test(item):
    for _ in range(item):
        print(f"[{multiprocessing.current_process().name}] - {time.ctime()}")
        time.sleep(2)


mpr = multiprocessing.Process(target=mpr_test, args=(5, ), name=f"mpr-1")
mpr.start()

# Ожидаем завершения всех процессов:
mpr.join()
# ID:
print(mpr.pid)
print(mpr.is_alive())
# Убиваем процесс:
mpr.terminate()


# ---------------------------------------------------------------------------------------------------------------------#
# Мультипроцессорность на основе классов:
# Наследуемся от базового класса мультипроцессора:

class MyProcess(multiprocessing.Process):
    def run(self) -> None:
        print("Start")


m_pr = MyProcess()
m_pr.start()


# ---------------------------------------------------------------------------------------------------------------------#
# Синхронизация процессов Python | Lock, RLock, Array, Queue
# Lock, RLock работает также как и в многопоточности
# Array - передача данных между процессами через массив НЕ :
SIZE = 3
arr = multiprocessing.Array("i", range(SIZE))
locker = multiprocessing.Lock()
list_mlp = []


def add_arr(arr, locker, index):
    with locker:
        random_number = random.randint(0, 10)
        mtime = time.ctime()
        arr[index] = random_number
        print(f"arr[{index}] = {random_number} - {mtime}")
        time.sleep(random_number)


for index in range(SIZE):
    mlp = multiprocessing.Process(target=add_arr, args=(arr, locker, index,), name=f"mlp-{index}")
    mlp.start()
    list_mlp.append(mlp)


for mlp in list_mlp:
    mlp.join()

print(list(list_mlp))


# ---------------------------------------------------------------------------------------------------------------------#
# Queue - очереди. Задаем количество процессов, которые могут использовать данные из другой очереди НА ПРЯМУЮ:

que = multiprocessing.Queue()


def queue_test(q):
    q.put("text")


mlp = multiprocessing.Process(target=queue_test, args=(que, ))
mlp.start()
print(f"{multiprocessing.current_process().name} - {que.get()}")
mlp.join()


# ---------------------------------------------------------------------------------------------------------------------#
# Multiprocessing Python Pool

def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}] - value: {value}")
    return value


def end_func(response):
    print(f"Response: {response}")


def apply_async_out(value):
    print(f"Value: {value}")
    return value


def apply_async_out_many(x, y, z):
    print(f"Value: {x}:{y}:{z}")
    return x, y, z


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 2) as p:
        # Запускаем наши процессы:
        # p.map(get_value, range(50))

        # Запускаем наши процессы с callback:
        # p.map_async(get_value, range(50), callback=end_func)

        # apply_async - выводим резуьтат выполнения процесса СРАЗУ:
        # for index in range(25):
        #     p.apply_async(apply_async_out, args=(index, ), callback=end_func)

        # Запускаем наши процессы для работы с несколькими значениями/переменными:
        p.starmap_async(apply_async_out_many, [(1, 2, 3), (4, 5, 6)], callback=end_func)
        p.close()
        p.join()


# ---------------------------------------------------------------------------------------------------------------------#
# Condition, Event - технология синхронизации, позволяет передавать сигналы между процессами:

event = multiprocessing.Event()


def event_test():
    print("Функция event_test запущена!")
    while True:
        # event - False
        event.wait()
        print("Event пройден!")
        time.sleep(2)


def track_event():
    while True:
        time.sleep(2)
        # event - True
        event.set()
        time.sleep(2)
        # event - False
        event.clear()
        print("Event is False!")


multiprocessing.Process(target=event_test).start()
multiprocessing.Process(target=track_event).start()


# ---------------------------------------------------------------------------------------------------------------------#
# Condition - в отличии от Event, метод разблокировки вызывается один раз:
# cond = multiprocessing.Condition()


def cond_test():
    while True:
        with cond:
            # При проходе цикла, сбрасывается значение в False -> True -> False и т.д.:
            cond.wait()
            print("Получили Condirion (событие)")


def track_cond():
    for index in range(100):
        if index % 10 == 0:
            with cond:
                # cond - True:
                cond.notify()
        else:
            print(f"track cond = {index}")
        time.sleep(1)


multiprocessing.Process(target=cond_test).start()
multiprocessing.Process(target=track_cond).start()


# ---------------------------------------------------------------------------------------------------------------------#
# Барьеры - ожидаем запуск нужного кол-ва процессов перед тем как продолжить выполнение программы:

NUM = 5
bar = multiprocessing.Barrier(NUM)


def barrier_1(bar):
    name = multiprocessing.current_process().name
    sl = random.randint(1, 4)
    print(f"[{name}] ожидает {sl} секунд")
    time.sleep(sl)
    bar.wait()
    print(f"[{name}] - запущен!")


for value in range(10):
    multiprocessing.Process(target=barrier_1, args=(bar,)).start()


# ---------------------------------------------------------------------------------------------------------------------#
# Manager - позволяют использовать общую память между процессами, создавать структуры и передавать данные структуры
# между процессами:
# Можно использовать разные типы данных, в отличии от Array:


def m_func(m_dict, m_list):
    m_dict["name"] = "test"
    m_dict["version"] = "0.1"
    m_list.append(1)
    m_list.append(2)


if __name__ == "__main__":
    with multiprocessing.Manager() as man:
        # Основной процесс:
        m_dict = man.dict()
        m_list = man.list()
        pr = multiprocessing.Process(target=m_func, args=(m_dict, m_list))
        pr.start()
        pr.join()

        print("Получаем результат изменения Менеджера через основной процесс: ")
        print(f"dict: {m_dict}")
        print(f"list: {m_list}")


# ---------------------------------------------------------------------------------------------------------------------#
# Python Pipe - использование труб/каналов для общения между процессами:

pipe_send, pipe_give = multiprocessing.Pipe()
# Канал отправки данных:
pipe_send.send([2, "Aloha!"])
# Канал получения данных:
res = pipe_give.recv()
print(res)


def send_data(conn):
    conn.send("Ho-ho-ho!")
    conn.close()

# Функция только для получения данных:
def getter(pipe):
    out, inp = pipe
    inp.close()
    while True:
        try:
            print("Data: ", out.recv())
        except Exception as _:
            break


def setter(data, inp):
    for value in data:
        time.sleep(1)
        inp.send(value)


if __name__ == "__main__":
    output_data, input_data = multiprocessing.Pipe()
    pr = multiprocessing.Process(target=getter, args=((output_data, input_data),))
    pr.start()

    setter([1, 2, 3, 4, 5], input_data)
    output_data.close()
    input_data.close()
