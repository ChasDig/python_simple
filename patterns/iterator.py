# Итератор - Структурный Паттерн. Реализующий логику прохождения по последовательности.
# - Пример: распаковка большого набора значений (тяжелый файл), парсинг.


class SimpleIterator:

    def __init__(self):
        self._data = "qweasdzcx"
        self._item = 0

    def __next__(self):
        try:
            val = self._data[self._item]
            self._item += 1
            return val
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


# simples = SimpleIterator()
#
# for simple in simples:
#     print(simple)
