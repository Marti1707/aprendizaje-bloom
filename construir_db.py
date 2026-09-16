# construir_db.py — arma la base de datos ocean.db a partir del CSV de la semana 3.
#
# Este script YA lo corrí por ti: recibes ocean.db lista para usar. Está aquí
# para que lo LEAS y veas cómo se crea una base de datos y cómo entran los datos.
# (No tienes que correrlo, pero puedes: `python construir_db.py`.)
#
# Usa solo la librería estándar de Python: sqlite3 (bases de datos) y csv.
import csv
import sqlite3

CSV = "ocean-temps-2sites.csv"
DB = "ocean.db"

# Conectarse a la base de datos (si el archivo no existe, se crea).
con = sqlite3.connect(DB)
cur = con.cursor()

# Empezar de cero por si se corre dos veces.
cur.execute("DROP TABLE IF EXISTS readings")
cur.execute("DROP TABLE IF EXISTS sites")

# --- Tabla 1: readings (una fila por lectura de temperatura) ---
# CREATE TABLE define las columnas y su tipo (TEXT = texto, REAL = número decimal).
cur.execute("""
    CREATE TABLE readings (
        date TEXT,
        site TEXT,
        temp REAL
    )
""")

# Cargar las filas del CSV, saltando las que tienen MM (dato faltante) —
# igual que hiciste en Python en las semanas 2 y 3.
with open(CSV) as f:
    for row in csv.DictReader(f):
        valor = row["sea_surface_temp_c"]
        if valor == "MM":
            continue
        # El signo ? evita problemas y es la forma correcta de insertar datos.
        cur.execute(
            "INSERT INTO readings (date, site, temp) VALUES (?, ?, ?)",
            (row["date"], row["site"], float(valor)),
        )

# --- Tabla 2: sites (información de cada sitio; una fila por sitio) ---
# Esta tabla es la que vas a UNIR (JOIN) con readings por la columna site.
cur.execute("""
    CREATE TABLE sites (
        site TEXT,
        region TEXT,
        description TEXT,
        lat REAL,
        lon REAL
    )
""")

sitios = [
    ("monterey", "California central", "Boya NDBC 46042, Bahia de Monterey (afloramiento frio)", 36.79, -122.47),
    ("san_pedro", "Sur de California", "Boya NDBC 46222, Canal de San Pedro (aguas mas calidas)", 33.62, -118.32),
]
cur.executemany(
    "INSERT INTO sites (site, region, description, lat, lon) VALUES (?, ?, ?, ?, ?)",
    sitios,
)

# Guardar (commit) los cambios y cerrar.
con.commit()

# Chequeo rápido para confirmar que quedó bien.
print("readings:", cur.execute("SELECT COUNT(*) FROM readings").fetchone()[0])
print("sites:", cur.execute("SELECT COUNT(*) FROM sites").fetchone()[0])

con.close()
