import pytest


def suma(a, b):
    return a + b


def test_suma():
    resultado = suma(2, 3)
    assert resultado == 5  # La prueba pasará ✅
