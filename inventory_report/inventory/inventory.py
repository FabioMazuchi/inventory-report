# import inventory_report.reports.simple_report as inv
# from ...inventory_report.reports.simple_report import SimpleReport
from collections import Counter
import csv
from datetime import date
import json
from xml.dom import minidom


class SimpleReport:
    @classmethod
    def generate(cls, lista):
        today = date.today().strftime("%Y-%m-%d")
        venc_date_list = [item["data_de_validade"] for item in lista]
        venc_date_list.append(today)
        venc_date_list.sort()

        next_date_venc = ""
        for n in range(len(venc_date_list)):
            if today == venc_date_list[n]:
                next_date_venc = venc_date_list[n + 1]

        old_date_fabr = min([item["data_de_fabricacao"] for item in lista])
        list_name_company = Counter(
            [item["nome_da_empresa"] for item in lista]
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {old_date_fabr}\n"
            f"Data de validade mais próxima: {next_date_venc}\n"
            f"Empresa com mais produtos: {list_name_company}"
        )


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        list_name_company = Counter(
            [item["nome_da_empresa"] for item in lista]
        )

        string = ""
        for item in list_name_company:
            string += f"- {item}: {list_name_company[item]}\n"

        return (
            f"{super().generate(lista)}\n"
            f"Produtos estocados por empresa:\n{string}"
        )


class Inventory(CompleteReport, SimpleReport):
    @classmethod
    def xml_list(cls, caminho):
        with open(caminho, "r") as file:
            xml = minidom.parse(file)
            print(xml)

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

        if tipo == "simples":
            return SimpleReport.generate(lista)
        return CompleteReport.generate(lista)
