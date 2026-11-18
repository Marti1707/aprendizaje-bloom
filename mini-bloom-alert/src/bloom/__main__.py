from bloom.config import SITIOS
from bloom.ingesta import pedir_sst
from bloom.reglas import calcular_promedio, riesgo


def main():
    for nombre, coords in SITIOS.items():
        temps_raw = pedir_sst(coords["lat"], coords["lon"])
        temps = [t for t in temps_raw if t is not None]
        print(f"--- {nombre} ---")
        if not temps:
            print("No hay datos suficientes para calcular estadísticas.\n")
            continue
        estado = "elevado" if riesgo(temps) else "normal"
        print(f"Promedio: {calcular_promedio(temps):.2f} °C")
        print(f"Máximo: {max(temps):.2f} °C")
        print(f"Riesgo: {estado}\n")


if __name__ == "__main__":
    main()