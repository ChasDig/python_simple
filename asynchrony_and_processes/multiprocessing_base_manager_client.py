from multiprocessing.managers import BaseManager

BaseManager.register("get")
manager = BaseManager(address=("127.0.0.1", 4444), authkey=b"qwe")
manager.connect()
print("Client connected!")

result = manager.get()
print(f"Result: {result}")
