class ThreadData:

    __shared_attrs = {
        "name": "thread",
        "id": 2,
    }

    def __int__(self):
        self.__dict__ = self.__shared_attrs
