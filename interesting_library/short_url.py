# Короткая ссылка:
import pyshorteners

pyshort_obj = pyshorteners.Shortener()
url = "https://pythonist.ru/9-poleznyh-bibliotek-python/?utm_source=telegram&utm_medium=pythonist"
print(pyshort_obj.tinyurl.short(url))
