from collections import Counter
from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self, lista):
        list_name_company = Counter(
            [item["nome_da_empresa"] for item in lista]
        )
        for item in list_name_company:
            print(item)
        return (
            f"{super().generate(lista)}\n" f"Produtos estocados por empresa:\n"
        )
