import asyncio
from time import time

# ---------------------------------------------------------------------------------------------------------------------#
CARS_DATA = (("Mustang", 10), ("Lamborghini", 12), ("BMW", 8))


async def main():
    async with asyncio.TaskGroup() as tg:
        for car in CARS_DATA:
            tg.create_task(start_wash(car))


async def start_wash(car):
    print(f"Приступаем к очистке машины {car[0]}")
    await asyncio.sleep(car[1])
    print(f"Машина {car[0]} была очищена за {car[1]} секунд.")


# ---------------------------------------------------------------------------------------------------------------------#

COUNT_GNOME = (("Fred", 5), ("Sam", 7), ("Tod", 9), ("Tom", 11), ("Din", 13))
TIME_GO_IN_CAVE = 3


async def mining_in_cave(gnome):
    print(f"Гном {gnome[0]} начал добывать руду в пещере.")
    await asyncio.sleep(gnome[1])
    print(f"Гном {gnome[0]} добыл руду за {gnome[1]} секунд.")


async def get_in_cave(gnome):
    print(f"Гном {gnome[0]} идет к пещере.")
    await asyncio.sleep(TIME_GO_IN_CAVE)
    print(f"Гном {gnome[0]} вошел в пещеру.")
    await mining_in_cave(gnome)
    print(f"Гном {gnome[0]} вышел из пещеры.")


async def main():
    print("Гномы проснулись.")
    async with asyncio.TaskGroup() as tg:
        for gnome in COUNT_GNOME:
            tg.create_task(get_in_cave(gnome))
    print("Все гномы добыли руду.")


# if __name__ == "__main__":
#     time_0 = time()
#     asyncio.run(main())
#     print(f"Прошло времени: {time() - time_0}")
