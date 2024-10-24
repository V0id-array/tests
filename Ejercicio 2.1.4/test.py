import pytest
from app import es_par

def test_es_par():
    assert es_par(2) == True
    assert es_par(4) == True
    assert es_par(0) == True
    assert es_par(-2) == True

def test_es_impar():
    assert es_par(1) == False
    assert es_par(3) == False
    assert es_par(-1) == False
    assert es_par(101) == False

def test_cero():
    assert es_par(0) == True

def test_negativo():
    assert es_par(-4) == True
    assert es_par(-3) == False
