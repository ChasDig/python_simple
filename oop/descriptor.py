"""
    Дескрипторы:
        - non-data descriptor:
            только считывают значения (не имеют таких методов обработки, как __set__ или __del__).
        !!  ВАЖНО: имеют тот же приоритет атрибутов, что и ОБЫЧНЫЕ АТРИБУТЫ КЛАССОВ (пример class InterfaceX).
        - data sescriptor:
            считывает и присваивает значения.
            приоритет обращения к ДЕСКРИПТОРУ ДАННЫХ ВЫШЕ, чем к области видимости ЛОКАЛЬНОГО АТРИБУТА КЛАССА.
"""


class InterfaceX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class ObjectStateCoordinateInterface:
    """Класс дескриптора для создания интерфейся взаимодействия с координатами объекта."""
    def __set_name__(self, owner, name):
        """
        Метод обработки создания экземпляров класса дескриптора ObjectStateCoordinateInterface.
        :param owner: ссылка на класс, в котором создаются экземпляры ObjectStateCoordinateInterface (ObjectState).
        :param name: имя экземпляра класса ObjectStateCoordinateInterface (в данном случае координаты x, y, z).
        :return: None
        """
        self.name = "_" + name
        print("__set_name__: ", self.name)

    def __get__(self, instance, owner):
        print(f"__get__: {instance}, {owner}, {self.name}")
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        Метод обработки значений и их присваивание при инициализации атрибутов в основном класса (ObjectState).
        :param instance: ссылается на экземпляр класса, в котором объявлен дескриптор (simple_object=ObjectState(...))
        :param value: присваиваемое значение в экземпляре
        :return:
        """
        print(f"__set__: {instance}, {self.name}, {value}")
        setattr(instance, self.name, value)


class ObjectState:

    # Дескрипторы для работы с координатами объекта:
    x = ObjectStateCoordinateInterface()
    y = ObjectStateCoordinateInterface()
    z = ObjectStateCoordinateInterface()

    xr = InterfaceX()

    def __init__(self, x, y, z):
        # Создание атрибутов экземпляра класса с применением дескрипторов:
        self.x = x
        self.y = y
        self.z = z


simple_object = ObjectState(1, 2, 3)

# В связи с приоритетностью, создается новый локальный атрибут класса ObjectState, в обход дескриптору. Т.к. он является
# non-data descriptor
simple_object.xr = 5

print(simple_object.xr, "\n", simple_object.__dict__)
