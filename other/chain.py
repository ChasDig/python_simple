from itertools import chain

"Атомарное итерирование по объектам последовательности."
chained_simple = chain('ab', [33])
c_1 = next(chained_simple)  # a
c_2 = next(chained_simple)  # b
c_3 = next(chained_simple)  # 33

print(c_1, c_2, c_3)
