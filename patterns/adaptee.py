from abc import ABC, abstractmethod
import json

# Адаптер - Структурный Паттерн. Позволяет изолировать определенную часть интерфейса и определять его работу в
# зависимости от выбранного характера применяемой логики.
# - Пример: Адаптер может реализовать разную логику подключения к БД в зависимости от типа БД.
# - Промежуточная прослойка, позволяющая избавиться от жесткой связке между элементами архитектуры проекта.

some_csv_source = "Name;Color;\nSnow;White"
some_json_source = '{"data": [{"Name": "Happy1", "Color": "Grey1"}, {"Name": "Happy2", "Color": "Grey2"}]}'


class Adapter(ABC):

    @abstractmethod
    def get_data(self, source: str) -> list:
        pass


class CSVReader(Adapter):

    def get_data(self, source: str) -> list:
        lines = self._get_lines(source=source)
        header, data = self._get_header_with_data(lines=lines)
        return self._format_data(header=header, data=data)

    def _get_lines(self, source: str) -> list[str]:
        return source.split("\n")

    def _get_header_with_data(self, lines: list[str]) -> tuple[list[str], list[list[str]]]:
        return lines[0].split(";"), [line.split(";") for line in lines[1:]]

    def _format_data(self, header: list[str], data: list[list[str]]) -> list:
        result = list()
        for item in data:
            result.append(dict(zip(header, item)))
        return result


class JSONReader(Adapter):

    def get_data(self, source: str) -> list:
        return json.loads(source)["data"]


class Printer(Adapter):

    def __init__(self, adapter: Adapter):
        self.adapter = adapter
        self.data = []

    def get_data(self, source: str) -> None:
        self.data = self.adapter.get_data(source=source)

    def print(self, source):
        self.get_data(source=source)
        for item in self.data:
            print(f"{item.get('Name')} - {item.get('Color')}")


# printer_csv = Printer(adapter=CSVReader())
# printer_json = Printer(adapter=JSONReader())
#
# printer_csv.print(source=some_csv_source)
# printer_json.print(source=some_json_source)
