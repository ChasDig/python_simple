from array import array
from random import random

# array_floats_1 = array("d", (random() for item in range(10**7)))
# print(array_floats_1[-1])
# with open("array_floats.bin", "wb") as file:
#     array_floats_1.tofile(file)
#
# array_floats_2 = array("d")
# with open("array_floats.bin", "rb") as file:
#     array_floats_2.fromfile(file, 10**7)
# print(array_floats_2[-1])

# print(array_floats_1 == array_floats_2)


# ---------------------------------------------------------------------------------------------------------------------#
# Memoryview - это тип последовательности в общей памяти, который позволяет работать со срезами массивов,
# ничего не копируя.
# memoryview.cast - Он позволяет изменить способ чтения и записи нескольких байтов в виде блока не перепещая ни одного
# бита.

# Строим массив из 6-ти байтов:
array_oct_1 = array("B", range(6))

# Преобразовываем этот массив в Memoryview:
m_1 = memoryview(array_oct_1)
print(m_1)
# Экспортируем memoryview как список:
print(m_1.tolist())

# Построение memoryview на основе m_1 но с 2 строками и 3 столбцами:
m_2 = m_1.cast("B", [2, 3])
print(m_2.tolist())

# Перезаписываем байт:
m_2[1, 1] = 22
print(m_2.tolist())

# Выводим исходный массив, на основе которого были построены memoryview m_1 и m_2 с ОБЩЕЙ ОБЛАСТЬЮ ПАМЯТИ:
print(array_oct_1)
