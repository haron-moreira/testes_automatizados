from ex_04 import fechar_conta

def test_01():
    assert fechar_conta(75.00)["total"] == 82.50
    assert fechar_conta(75.00)["gorjeta"] == 7.50

def test_02():
    assert fechar_conta(125)["total"] == 137.50
    assert fechar_conta(125)["gorjeta"] == 12.50

def test_03():
    assert fechar_conta(350.87)["total"] == 385.96
    assert fechar_conta(350.87)["gorjeta"] == 35.09