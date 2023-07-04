from xmlrpc.client import ServerProxy

HOST_PORT = ("localhost", 6789)
NUM = 7

proxy = ServerProxy(f"http://{HOST_PORT[0]}:{HOST_PORT[1]}/")
result_double_func = proxy.double_func(NUM)
print(f"Double {NUM} is {result_double_func}")
