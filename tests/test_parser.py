"""Pruebas del parser: de los tokens al AST."""
import pytest
from mini_interprete.errores import ErrorDeSintaxis
from mini_interprete.ast import Numero, OperacionBinaria
from mini_interprete.lexer import tokenizar
from mini_interprete.parser import Parser


def arbol_de(texto):
    return Parser(tokenizar(texto)).parsear()


def test_construye_el_arbol_de_una_suma():
    assert arbol_de("3 + 4") == OperacionBinaria("+", Numero(3), Numero(4))


def test_la_multiplicacion_se_agrupa_antes_que_la_suma():
    # 3 + 4 * 2  debe agruparse como  3 + (4 * 2)
    assert arbol_de("3 + 4 * 2") == OperacionBinaria(
        "+", Numero(3), OperacionBinaria("*", Numero(4), Numero(2))
    )


def test_los_parentesis_cambian_la_agrupacion():
    # (3 + 4) * 2  debe agruparse al reves
    assert arbol_de("(3 + 4) * 2") == OperacionBinaria(
        "*", OperacionBinaria("+", Numero(3), Numero(4)), Numero(2)
    )

def test_menos_unario_invalido():
    tokens = tokenizar("-3")
    parser = Parser(tokens)

    with pytest.raises(ErrorDeSintaxis):
        parser.parsear()

def test_parentesis_invalidos():
    tokens = tokenizar("3 * (2 + ())")
    parser = Parser(tokens)

    with pytest.raises(ErrorDeSintaxis):
        parser.parsear()
