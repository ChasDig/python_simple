import numpy as np
# Таймер высокого разрешения:
from time import perf_counter as pc

# Создаем массив:
array_np_1 = np.arange(12)
# print(array_np_1)
# print(type(array_np_1))
# # Размер данного массива:
# print(array_np_1.shape)

# Меняем представление массива - 3 строки и 4 столбца
# array_np_1.shape = 3, 4
# print(array_np_1)
#
# # Выводим: строку с индексом 2, строку с индексом 2 и столбец с индексом 1, все элементы столбца 1
# print(array_np_1[2])
# print(array_np_1[2, 1])
# print(array_np_1[:, 1])
#
# # Транспонируем массив (матрицу):
# print(array_np_1.transpose())


#---------------------------------------------------------------------------------------------------------------------#
# Работа сразу со всеми элементами массива:
print(array_np_1)
array_np_1 *= 2
print(array_np_1)
