from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter


def test_decorar_relatorio():
    d1 = "\033[36m2020-09-06\033[0m\n"
    d2 = "\033[36m2023-09-17\033[0m\n"
    empr = "\033[31mTarget Corporation\033[0m"
    fr1 = "\033[32mData de fabricação mais antiga:\033[0m " + d1
    fr2 = "\033[32mData de validade mais próxima:\033[0m " + d2
    fr3 = "\033[32mEmpresa com mais produtos:\033[0m " + empr

    string = fr1 + fr2 + fr3
    result = ColoredReport(SimpleReport).generate(
        CsvImporter.import_data("inventory_report/data/inventory.csv")
    )

    assert string == result
