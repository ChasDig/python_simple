import operator
import functools
import reprlib
from array import array
import math


class Vector2D:
    typecode = 'b'
    # Для работы с позиционными образцами:
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

    def __hash__(self):
        #  Вычисляем хэш кортежа:
        return hash((self.x, self.y))

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


# print(format(Vector2D(1, 1), 'p'))


# -------------------------------------------------------------------------------------------------------------------- #
# Специальные методы для последовательностей:
class Vector:
    __match_args__ = ("x", "y", "z", "t")
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        #  Если экземпляр класса является последовательностью...
        if isinstance(item, slice):
            # ...то получаем класс экземпляра...
            cls = type(self)
            # ... вызываем класс для построения нового экземпляра по срезу массива _components:
            return cls(self._components[item])
        #  Функция operator.index вызываем специальный метод __index__. Специальная функция для получения индекса
        #  (проверка на возможность применения объекта в качестве индекса):
        index = operator.index(item)
        return self._components[index]

    def __getattr__(self, item):
        # Стр. 392:
        cls = type(self)
        try:
            pos = cls.__match_args__.index(item)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f"{cls.__name__!r} object has no attribute {item!r}"
        raise AttributeError(msg)

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.__match_args__:
                error = "readonly attribute {attr_name!r}"
            elif key.islower():
                error = "can't set attributes 'z' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)

    def __eq__(self, other):
        # Т.к. в отличие от класса Vector2D, в данной реализации количество элементов при инициализации не фиксированно,
        # то переопределяем метод:
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f"Vector({components})"


vector_1 = Vector(range(7))
print(vector_1)
print(vector_1.x)
