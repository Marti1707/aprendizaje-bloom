import sqlite3

# Conectamos Python con la base de datos ocean.db
con = sqlite3.connect("ocean.db")

# Ejecutamos la consulta SQL y mostramos los resultados
for fila in con.execute("SELECT site, ROUND(AVG(temp), 2) FROM readings GROUP BY site;"):
    print(fila)

# Cerramos la conexión
con.close()