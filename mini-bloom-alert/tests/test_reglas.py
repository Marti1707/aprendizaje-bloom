from bloom.reglas import calcular_promedio, riesgo

def test_promedio_lista_normal():
    assert calcular_promedio([10, 20, 30]) == 20.0

def test_promedio_con_none():
    assert calcular_promedio([10, None, 30]) == 20.0

def test_promedio_lista_vacia():
    assert calcular_promedio([]) == 0.0

def test_riesgo_en_umbral():
    assert riesgo([18.0]) is False
    assert riesgo([18.1]) is True