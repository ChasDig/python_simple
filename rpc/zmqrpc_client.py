import zerorpc

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")
result = client.sum_func(3, 4)
print(f"Sum 3 and 4 is {result}")
# 1xx
# 2xx
# 3xx
# 4xx
# 5xx
