import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        if ".json" not in caminho:
            raise ValueError("Arquivo inválido")
        with open(caminho, "r") as file:
            result = json.load(file)
            return result


# print(JsonImporter.import_data("inventory_report/data/inventory.json"))
