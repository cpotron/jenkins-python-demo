import pytest

from demo.calculatrice import Calculatrice


@pytest.fixture
def calcul():
    return Calculatrice()


@pytest.mark.parametrize("x,y,z", [(3, 3, 6), (-3, 3, 0)])
def test_addition(calcul, x, y, z):  # pylint: disable=redefined-outer-name
    assert calcul.addition(x, y) == z


@pytest.mark.parametrize("x,y,z", [(3, 3, 0), (-3, 3, -6)])
def test_soustraction(calcul, x, y, z):  # pylint: disable=redefined-outer-name
    assert calcul.soustraction(x, y) == z


@pytest.mark.parametrize("x,y,z", [(3, 3, 9), (3, 0, 0)])
def test_multiplication(calcul, x, y, z):  # pylint: disable=redefined-outer-name
    assert calcul.multiplication(x, y) == z


@pytest.mark.parametrize("x,y,z", [(3, 3, 1), (0, 3, 0)])
def test_division(calcul, x, y, z):  # pylint: disable=redefined-outer-name
    assert calcul.division(x, y) == z
