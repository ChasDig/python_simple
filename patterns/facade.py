from patterns.adaptee import Printer, CSVReader, JSONReader

# Фасад - Структурный Паттерн. Позволяет фильтровать методы встроенных классов, выдавая Пользователю строго определенный
# набор интерфейсов.

some_csv_source = "Name;Color;\nSnow;White"
some_json_source = '{"data": [{"Name": "Happy1", "Color": "Grey1"}, {"Name": "Happy2", "Color": "Grey2"}]}'


class Facade:

    def __init__(self):
        self._csv_printer = Printer(CSVReader())
        self._json_printer = Printer(JSONReader())
        self._csv_data = []
        self._json_data = []

    def fill_csv_data(self, *args):
        self._csv_data = args

    def fill_json_data(self, *args):
        self._json_data = args

    def _print_csv_data(self):
        for item in range(len(self._csv_data)):
            print(f"CSV read line {item + 1}")
            self._csv_printer.print(source=self._csv_data[item])

    def _print_json_data(self):
        for item in range(len(self._json_data)):
            print(f"JSON read line {item + 1}")
            self._json_printer.print(source=self._json_data[item])

    def printer(self):
        self._print_csv_data()
        self._print_json_data()


# facade = Facade()
# facade.fill_csv_data(some_csv_source)
# facade.fill_json_data(some_json_source)
#
# facade.printer()
