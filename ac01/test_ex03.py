from ex_03 import promocao

def test_01():
    assert promocao(500.00, 50.00) == 450.00

def test_02():
    assert promocao(10500.00, 500.00) == 10000.00

def test_03():
    assert promocao(90.00, 0.80) == 89.20
