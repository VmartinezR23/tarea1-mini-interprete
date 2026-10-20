"""Pruebas del evaluador: del AST a un numero."""
import pytest
from mini_interprete.errores import ErrorDeEvaluacion
from mini_interprete.cli import interpretar


def test_suma():
    assert interpretar("3 + 4") == 7


def test_resta():
    assert interpretar("10 - 3") == 7


def test_multiplicacion():
    assert interpretar("6 * 7") == 42


def test_division():
    assert interpretar("10 / 2") == 5


def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11


def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14

def test_division_por_cero():
    with pytest.raises(ErrorDeEvaluacion):
        interpretar("10/0")

def test_division_resultado_menor_que_uno():
    assert interpretar("1/5") == 0.2

def test_jerarquia_operaciones():
    assert interpretar("10 / 5 + 3 * 4") == 14

def test_asociatividad_izquierda():
    assert interpretar("10 - 2 - 3 - 1") == 4  





