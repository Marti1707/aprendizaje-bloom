from bloom.config import UMBRAL_RIESGO

def calcular_promedio(valores):
    if not valores:
        return 0.0
    validos = [v for v in valores if v is not None]
    if not validos:
        return 0.0
    return sum(validos) / len(validos)

def riesgo(valores):
    prom = calcular_promedio(valores)
    return prom > UMBRAL_RIESGO