from ex_01 import salario_liquido

def test_01():
    assert salario_liquido(6.25, 160, 1.3) == 987.00

def test_02():
    assert salario_liquido(20.5, 240, 1.7) == 4836.36

def test_03():
    assert salario_liquido(13.9, 200, 6.48) == 2599.86
