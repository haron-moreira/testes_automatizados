from pytest_bdd import given, when, then, scenario
from pytest import fixture
from src.carrinho_compras import CarrinhoCompras

@fixture
def contexto():
    return CarrinhoCompras()

@scenario('carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""

@scenario('carrinho.feature', 'Remover itens ao carrinho')
def test_remover_itens_ao_carrinho():
    """Remover itens ao carrinho."""

@given('que tenho um carrinho de compras com o item "Camiseta" e preco de R$ 29.99')
def carrinho_compras_com_item_e_preco(contexto):
    contexto.adicionar_item("Camiseta", 29.99)

@when('eu adiciono o item "Calca" com o preco R$ 49.99')
def adicionar_item_ao_carrinho(contexto):
    contexto.adicionar_item("Calca", 49.99)

@when('eu removo o item do carrinho')
def remover_item_do_carrinho(contexto):
    contexto.remover_item()

@then('o carinho de compras deve estar vazio')
def verificar_carrinho_vazio(contexto):
    assert contexto.esta_vazio()

@then('o total do carrinho de compras deve ser R$ 79.98')
def verificar_total_do_carrinho(contexto):
    assert contexto.total() == 79.98
