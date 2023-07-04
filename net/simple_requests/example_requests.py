# pip install requests
import requests

""" Запросы: HTTP-запросы: """
# response_get = requests.get(url="https://api.github.com/users/ChasDig/repos/")
# response_post = requests.post(url="https://httpbin.org/post", data={"key": "value"})
# response_delete = requests.delete(url="https://httpbin.org/delete")
# response_head = requests.head(url="https://httpbin.org/get")
# response_options = requests.options(url="https://httpbin.org/get")

""" Передача параметров в URL: """
# params_1 = {"key_1": "value_1", "key_2": ["value_2_1", "value_2_2"]}
# response_param = requests.get(url="https://httpbin.org/get", params=params_1)

""" Содержание ответа: """
# print(response_param.text)
# print(response_param.json())
# Encoding:
# print(response_param.encoding)
# Byte response:
# print(response_param.content)
# Status response:
# print(response_param.status_code)
# Json:
# print(response_param.json()

""" Получение необработанного сокетного ответа от сервера: """
# response_stream = requests.get(url="https://api.github.com/events", stream=True)
# Необработанный сокетный ответ:
# print(response_stream.raw)
# Потоковая передача данных обработанного и декодированного сокетного ответа в файл:
# with open("response_stream_data.txt", "wb") as file:
#     for chunk in response_stream.iter_content(chunk_size=128):
#         file.write(chunk)

""" Пользовательские заголовки: """
# url = "https://api.github.com/some/endpoint"
# headers = {"user-agent": "my-app/0.0.1"}
# response_header = requests.get(url=url, headers=headers)

""" Отправка данных в POST-запросе: """
# payload_dict = {"key_1": "value_1", "key_2": ["value_2_1", "value_2_2"]}
# payload_list = [("key_1", "value_1"), ("key_2", "value_2")]
# response_payload = requests.post(url="https://httpbin.org/post", data=payload)
# print(response_payload.text)

# Для отправки данных в формате json можно предварительно сериализовать словарь и отправить в аргументе data,
# можно на прямую через атрибут json.
# files = {"file": open("some_file.txt", "rb")}
# response_file = requests.post(url="https://httpbin.org/post", files=files)
# print(response_file.text)

""" Статус код: """
# response_status_code = requests.get('https://httpbin.org/get')
# print(response_status_code.status_code)
# print(response_status_code.status_code == requests.codes.ok)

""" Заголовки ответов: """
# response_headers = requests.get('https://httpbin.org/get')
# print(response_headers.headers)
# print(response_headers.headers.get("content-type"))

""" Статус код при неверном запросе: """
# bad_response = requests.get('https://httpbin.org/status/404')
# print(bad_response.status_code)
# Rise ошибки:
# bad_response.raise_for_status()

""" Cookies """
# Получение Cookie:
# url = 'https://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# response_cookie = requests.get(url=url, cookies=cookies)
# print(response_cookie.text)

# RequestsCookieJar - для использования в нескольких доменах или путях:
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url_1 = 'https://httpbin.org/cookies'
# response_jar_1 = requests.get(url=url_1, cookies=jar)
# print(response_jar_1.text)
# url_2 = 'https://httpbin.org/elsewhere'
# response_jar_2 = requests.get(url=url_2, cookies=jar)
# print(response_jar_2.text)

""" Перенаправление и истории """
# # digitology - осуществляет перенаправление
# response_history_1 = requests.get('http://digitology.tech/')
# print(response_history_1.url)
# print(response_history_1.status_code)
# # Получаем историю о перенаправлении:
# print(response_history_1.history)

# # allow_redirects - отключение перенаправления:
# response_history_2 = requests.get('http://digitology.tech/', allow_redirects=False)
# print(response_history_2.status_code)
# print(response_history_2.history)

""" Таймауты - прекращение ожидание ответа спустя определенное количество секунд """
# response_timeout = requests.get('https://digitology.tech/', timeout=5)
# print(response_timeout.status_code)
