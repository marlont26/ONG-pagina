import pytest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(3.5, 2.5) == 6.0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(-1, 1) == -2
    assert resta(0, 0) == 0
    assert resta(3.5, 2.5) == 1.0

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(0, 5) == 0
    assert multiplicacion(3.5, 2) == 7.0

def test_division():
    assert division(6, 3) == 2
    assert division(-4, 2) == -2
    assert division(7, 2) == 3.5
    with pytest.raises(ValueError):
        division(5, 0)