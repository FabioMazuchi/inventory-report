from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


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
