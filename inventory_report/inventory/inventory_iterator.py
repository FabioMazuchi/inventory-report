from collections import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.count = 0

    def __next__(self):
        try:
            result = self.data[self.count]
        except IndexError:
            raise StopIteration
        self.count += 1
        return result
