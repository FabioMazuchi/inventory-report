from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    produto = "refrigerante"
    empresa = "coca-cola"
    fabricacao = "01-02-2022"
    validade = "01-02-2023"
    serie = "123"
    instrucoes = "em ambiente refrigerado"

    re = f"O produto {produto} fabricado em {fabricacao}"
    sul = f"por {empresa} com validade até {validade} precisa"
    result = f"{re} {sul} ser armazenado {instrucoes}."
    product = str(
        Product(
            id,
            produto,
            empresa,
            fabricacao,
            validade,
            serie,
            instrucoes,
        )
    )
    assert result == product
