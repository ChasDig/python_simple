from abc import ABC, abstractmethod

#  Фабрика - Порождающий Паттерн. Позволяет реализовать создание абстрактных классов с необходимым набором интерфейсов.


class AbstractSpaceShip(ABC):
    """Абстрактный Класс 'Космический Корабль'."""

    @abstractmethod
    def launch_into_space(self):
        """Запуск Космического Корабля в Космос."""
        pass


class AbstractAirplane(ABC):
    """Абстрактный Класс 'Самоле'."""

    @abstractmethod
    def launch_into_air(self):
        """Запуск Самолета в небо."""
        pass


class AbstractTransportFactory(ABC):
    """Фабрика по созданию Абстрактных Классов."""

    @abstractmethod
    def create_starship(self) -> AbstractSpaceShip:
        """Создание Абстрактного Класса 'Космический Корабль'."""
        pass

    @abstractmethod
    def create_airplane(self) -> AbstractAirplane:
        """Создание Абстрактного Класса 'Самолет'."""
        pass


class Apollo(AbstractSpaceShip):
    """Создание Класса 'Apollo' на основе Абстрактного класса 'Космический Корабль'."""

    def launch_into_space(self):
        """Запуск Космического Корабля в Космос."""
        print("Apollo send into space!")


class Boeing_737(AbstractAirplane):
    """Создание Класса 'Boeing_737' на основе Абстрактного класса 'Самолет'."""

    def launch_into_air(self):
        """Запуск Самолета в Космос."""
        print("Boeing's 737 send into air!")


class CreateTransportFactory(AbstractTransportFactory):
    """Реализация Фабрики по созданию Класса 'Космический Корабль' и 'Самолет'."""

    def create_starship(self) -> Apollo:
        """Создание 'Apollo'."""
        return Apollo()

    def create_airplane(self) -> Boeing_737:
        """Создание 'Boeing_737'."""
        return Boeing_737()


class Hangar:
    factory: AbstractTransportFactory

    def __init__(self, factory: AbstractTransportFactory):
        self.factory = factory

    def drive_with_spaceship(self):
        spaceship = self.factory.create_starship()
        spaceship.launch_into_space()

    def drive_with_airplane(self):
        airplane = self.factory.create_airplane()
        airplane.launch_into_air()


# hangar = Hangar(factory=CreateTransportFactory())
# hangar.drive_with_spaceship()
# hangar.drive_with_airplane()
