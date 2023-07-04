from multiprocessing.managers import BaseManager
import time


def get_item():
    return time.time()


BaseManager.register("get", callable=get_item)
manager = BaseManager(address=("", 4444), authkey=b"qwe")
server = manager.get_server()
print("Server started")
server.serve_forever()
