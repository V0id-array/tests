from app import debe_tributar

def test_debe_tributar_menor_de_edad():
    assert not debe_tributar(15, 1500), 

def test_debe_tributar_edad_exacta():
    assert debe_tributar(16, 1500), 

def test_debe_tributar_ingresos_bajos():
    assert not debe_tributar(20, 900), 

def test_debe_tributar_condiciones_correctas():
    assert debe_tributar(20, 1500), 

def test_debe_tributar_limite_ingresos():
    assert debe_tributar(17, 1000), 
