from ex_02 import desconto

def test_01():
    assert desconto(100) == 91.00

def test_02():
    assert desconto(1500) == 1365.00

def test_03():
    assert desconto(60000) == 54600.00
