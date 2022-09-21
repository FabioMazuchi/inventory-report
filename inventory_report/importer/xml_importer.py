from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        if ".xml" not in caminho:
            raise ValueError("Arquivo inválido")
        with open(caminho) as f:
            res = xmltodict.parse(f.read())["dataset"]["record"]
            result = []
            for record in res:
                result.append(record)
            return result


# print(XmlImporter.import_data("inventory_report/data/inventory.xml"))
