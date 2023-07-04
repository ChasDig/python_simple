import msgpackrpc

NUM = 10

client = msgpackrpc.Client(msgpackrpc.Address("localhost", 6789))
response = client.call("double_func", NUM)
print(f"Double {NUM} is {response}")
