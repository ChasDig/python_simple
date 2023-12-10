import time

# Декоратор - Структурный Паттерн.


def wrapper(func):
    def sleep_func(*args, **kwargs):
        print("Start sleep")
        func(*args, **kwargs)
        print("Stop sleep")

    return sleep_func


@wrapper
def sleep_func(time_sleep: int) -> None:
    time.sleep(time_sleep)


# sleep_func(time_sleep=3)
