#  Синглтон - Порождающий Паттерн. Позволяет реализовывать только ОДИН экземпляр данного класса.


class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        # Если объект еще не создан...
        if not cls._instance:
            # ... то создаем его:
            cls._instance = cls.__new__(cls, *args, **kwargs)
        # Возвращаем созданный/найденный объект:
        return cls._instance
