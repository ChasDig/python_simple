# import csv
#
# some_csv = [
#     ["name", "Din"],
#     ["age", 20],
#     ["profession", "demon hunter"],
# ]

# with open("winchester.csv", "wt") as cfile:
#     csvout = csv.writer(cfile)
#     csvout.writerows(some_csv)

# with open("winchester.csv", "rt") as cfile:
#     csf_data = csv.reader(cfile)
#     list_data = [data for data in csf_data]
# print(list_data)

# import json
#
# dict_struct = {
#     "name": {
#         "firstname": "Din",
#         "lastname": "Winchester",
#     },
#     "profession": "demon hunter",
# }
#
# json_struct = json.dumps(dict_struct)
# print(json_struct)
# print(type(json_struct))

# import json
# import datetime
#
# now = datetime.datetime.utcnow()
# now_json = json.dumps(now, default=str)
# print(now_json)

# import dbm
# dbm_data = dbm.open("car_dbm", "c")
# dbm_data["mustang"] = "red"
# dbm_data["astan martin"] = "black"
# print(dbm_data["mustang"])
# dbm_data.close()


# import memcache
#
# client_m = memcache.Client(["127.0.0.1:11211"])
# client_m.set("marco", "polo")
# res = client_m.get("marco")
# print(res)


# import redis
#
# connect = redis.Redis("localhost", 6379)
# connect.set("name", "Sam")
# connect.set("age", 20)
# print(connect.keys("*"))

# res = ((item_1, item_2) for item_1 in range(5) for item_2 in range(5))
# for i in range(25):
#     item = next(res)
#     print(item, type(item), sep=" ")

import multiprocessing
import os
import time


def do_this(say: str):
    print("Процесс №{} сказал {}".format(os.getpid(), say))


if __name__ == "__main__":
    for item in range(5):
        process = multiprocessing.Process(
            target=do_this,
            args=(item,),
        )
        process.start()
        print(f"Процесс {item} запущен")
        if item == 3:
            print(f"Процесс {item} был убит и не будет ожидать 5 секунд, т.к. он был равен 3.")
            process.terminate()
        else:
            time.sleep(5)
