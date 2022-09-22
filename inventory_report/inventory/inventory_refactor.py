from collections import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, caminho, tipo):
        result = self.importer.import_data(caminho)
        for res in result:
            self.data.append(res)

    def __iter__(self):
        return InventoryIterator(self.data)
