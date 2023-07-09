import typing


class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self._seconds = seconds % self.__DAY

    def get_time(self):
        second = self._seconds % 60
        minute = (self._seconds // 60) % 60
        hour = (self._seconds // 3600) % 24
        return f"{self.__get_format(hour)}:{self.__get_format(minute)}:{self.__get_format(second)}"

    @classmethod
    def __get_format(cls, time_interval):
        return str(time_interval).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Атрибут должен быть целым числом (int) и объектом класса Clock")
        if isinstance(other, int):
            self._seconds += other
        if isinstance(other, Clock):
            self._seconds += other._seconds
        return self
        # return Clock(self._seconds + other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other


clock_1 = Clock(5000)
clock_2 = Clock(3000)
print(clock_1.get_time())
clock_1 += 100
clock_3 = clock_1 + clock_2
print(clock_3.get_time())
