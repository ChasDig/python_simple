from array import array
import math


class Vector2D:
    typecode = 'b'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        #  Итерация. Благодаря этому методу реализуется распаковка. В данном случае реализуется генераторным выражением:
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        #  Интерполируем компоненты с помощью синтаксиса '{!r}' для получения представлений.
        #  *self - доступна распаковка благодаря __iter__
        return "{}: {!r}, {!r}".format(class_name, *self)

    def __str__(self):
        #  tuple - реализуется благодаря __iter__:
        return str(tuple(self))

    def __bytes__(self):
        #  Преобразуем typecode в bytes и конкатенируем его с bytes, полученным преобразованием массива, полученного
        #  при обходе экземпляра класса:
        return (
            bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))
        )

    def __eq__(self, other):
        #  Проводим сравнение кортежа, содержащего компоненты атрибута класса.
        #  Минус данной реализации: сравнение возможно между экземпляром класса и итерируемым объектом (напр: [1, 2]):
        return tuple(self) == tuple(other)

    def __abs__(self):
        #  Модуль вектора - длина гипотенузы с катетами:
        return math.hypot(self.x, self.y)

    def __bool__(self):
        #  Получаем булево значение вектора исходя из его модуля:
        return bool(abs(self))

    def __format__(self, format_spec):
        #  По умолчанию дандер-метод __format__ наследуется от object, возвращающий метод __str__. Дабы наш метод
        #  правильно выводился, переопределяем __format__:
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coord = (abs(self), self.angel())
            outer_tmp = "<{}, {}>"
        else:
            coord = self
            outer_tmp = "({}, {})"
        components = (format(c, format_spec) for c in coord)
        return outer_tmp.format(*components)

    def angel(self):
        #  Возвращаем угол полярных координат:
        return math.atan2(self.x, self.y)

    @classmethod
    def frombytescode(cls, octets):
        #  Преобразование из байтового представления экземпляр класса - конструирование Vector2D.
        #  Получаем typecode и декодируем его из первого байта:
        typecode = chr(octets[0])
        #  Благодаря memoryview из двоичной последовательности и привести его к типу typecode:
        memv = memoryview(octets[1:]).cast(typecode)
        #  Распаковка memoryview образовавшиеся в результате приведения типов. Создаем экземпляр класса благодаря 'cls':
        return cls(*memv)


print(format(Vector2D(1, 1), 'p'))
