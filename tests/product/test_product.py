from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    produto = "refrigerante"
    empresa = "coca-cola"
    fabricacao = "01-02-2022"
    validade = "01-02-2023"
    serie = "123"
    instrucoes = "em ambiente refrigerado"

    product1 = Product(
        id,
        produto,
        empresa,
        fabricacao,
        validade,
        serie,
        instrucoes,
    )
    assert product1.id == id
    assert product1.nome_do_produto == produto
    assert product1.nome_da_empresa == empresa
    assert product1.data_de_fabricacao == fabricacao
    assert product1.data_de_validade == validade
    assert product1.instrucoes_de_armazenamento == instrucoes
