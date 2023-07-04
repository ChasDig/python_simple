# Запросы в google chrome:
from googlesearch import search

# Запрос
query = "cats images"

# Выводим 5 первых результатов:
for item in search(query=query, num=5, stop=5, pause=2):
    print(item)
