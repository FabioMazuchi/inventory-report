import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        if ".csv" not in caminho:
            raise ValueError("Arquivo inválido")
        with open(caminho, encoding="utf8") as file:
            result = csv.DictReader(file, delimiter=",", quotechar='"')
            return [row for row in result]
