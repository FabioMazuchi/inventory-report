from collections import Counter
from datetime import date


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
