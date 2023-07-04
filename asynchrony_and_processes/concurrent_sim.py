import concurrent.futures as pool
import threading
import time

# concurrent.futures с использованием threading (для потоков - то же самое, тт):


def worker_threading(number):
    threading_name = threading.current_thread().name
    print(f"Поток '{threading_name}': начало обработки данных...")
    result = number / 10
    time.sleep(result)
    print(f"Поток '{threading_name}': обработка данных завершена...")
    return result


data = [item for item in range(1, 10, 2)]


main_threading_name = threading.current_thread().name
print(f"Основной поток '{main_threading_name}' запущен...")

with pool.ThreadPoolExecutor(max_workers=3) as executor:
    res = executor.map(worker_threading, data)

results = list(res)
print(f"{main_threading_name}: результаты: {results}")
