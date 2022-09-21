from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xmltodict
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def xml_list(cls, caminho):
        with open(caminho) as f:
            res = xmltodict.parse(f.read())["dataset"]["record"]
            result = []
            for record in res:
                result.append(record)
            return result

    @classmethod
    def csv_list(cls, caminho):
        with open(caminho, encoding="utf8") as file:
            result = csv.DictReader(file, delimiter=",", quotechar='"')
            return [row for row in result]

    @classmethod
    def json_list(cls, caminho):
        with open(caminho, "r") as file:
            result = json.load(file)
            return result

    @classmethod
    def import_data(cls, caminho, tipo):
        lista = []
        if ".csv" in caminho:
            lista = cls.csv_list(caminho)

        if ".json" in caminho:
            lista = cls.json_list(caminho)

        if ".xml" in caminho:
            lista = cls.xml_list(caminho)

        if tipo == "simples":
            return SimpleReport.generate(lista)
        return CompleteReport.generate(lista)
