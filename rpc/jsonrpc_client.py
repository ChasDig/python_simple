from jsonrpcclient import request

num = 20

result_request = request("http://localhost:5000", "double_func", num=num)
print(f"Double {num} is {result_request.data.result}")
