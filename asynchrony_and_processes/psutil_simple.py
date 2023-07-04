"""
    Psutil:
        - содержит информацию:
            -- Системе: ЦП, память, диск, сеть, сенсоры.
            -- Процессы: идентификатор, родительский идентификатор, ЦП, память, открытые файлы, потоки.
"""
import psutil

# Время использования процессов:
for item in psutil.cpu_times(True):
    print(item)
# Занятость процессов:
print(psutil.cpu_percent(percpu=True))
