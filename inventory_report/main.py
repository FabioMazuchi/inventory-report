from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def escreva(caminho, tipo):
    reporter = SimpleReport
    if tipo != "simples":
        reporter = CompleteReport

    importer = XmlImporter
    if ".csv" in caminho:
        importer = CsvImporter
    elif ".json" in caminho:
        importer = JsonImporter

    inventory = InventoryRefactor(importer)
    inventory.import_data(caminho, tipo)
    print(str(reporter.generate(inventory.data)), end="")


def main():
    try:
        _, caminho, tipo = sys.argv
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        escreva(caminho, tipo)
