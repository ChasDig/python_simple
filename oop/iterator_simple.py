class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            print("@@")
            raise StopIteration


class FRange2:
    def __init__(self, start, stop, step, row):
        self.fp = FRange(start, stop, step)
        self.row = row

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.row:
            self.value += 1
            return iter(self.fp)
        else:
            raise StopIteration


my_range = FRange2(0, 5, 1, 4)

for i in my_range:
    for j in i:
        print(j, end=" ")
    print()
