from collections import Counter
from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, lista):
        today = date.today()
        venc_date_list = min([date.fromisoformat(item["data_de_validade"]) for item in lista if date.fromisoformat(item["data_de_validade"]) > today])

        old_date_fabr = min([date.fromisoformat(item["data_de_fabricacao"]) for item in lista])
        list_name_company = Counter(
            [item["nome_da_empresa"] for item in lista]
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {old_date_fabr}\n"
            f"Data de validade mais próxima: {venc_date_list}\n"
            f"Empresa com mais produtos: {list_name_company}"
        )
