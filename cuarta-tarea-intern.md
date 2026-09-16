# Tu cuarta semana 🌊🗄️

¡Gran avance! Hasta ahora leíste datos y los procesaste con Python. Esta semana aprendes **SQL**, el idioma con el que se le hacen preguntas a una **base de datos**. Es una de las herramientas más importantes que vas a usar en Bloom: nuestros datos viven en bases de datos (Postgres, BigQuery) y les preguntamos con SQL.

Y hay una sorpresa buena: vas a ver cómo una sola línea de SQL hace lo que la semana pasada te tomó un `dict` y varios loops. 😎

Como siempre: no es carrera, y los términos técnicos van en English (query, table, JOIN, etc.).

---

## El objetivo de la semana

Responder preguntas reales sobre los datos del océano usando **SQL**, y hacerlo de **tres formas distintas** con la misma base de datos, para que veas que a un mismo resultado se llega por varios caminos (cada uno con sus pros y contras).

Te voy a pasar dos archivos:
- **`ocean.db`** — una base de datos **SQLite** ya armada, con los datos de las dos boyas.
- **`construir_db.py`** — el script con el que armé esa base. **No tienes que correrlo**; está para que lo LEAS y veas cómo se crea una tabla y cómo entran los datos.

`ocean.db` tiene **dos tablas**:
- `readings` — una fila por lectura: `date`, `site`, `temp`.
- `sites` — info de cada sitio: `site`, `region`, `description`, `lat`, `lon`.

### Antes de empezar: nueva branch 🌿
Mismo repository (`mi-aprendizaje-bloom`), branch nueva:
1. `git checkout main` y `git pull`
2. `git checkout -b semana-4-sql`
3. Pon `ocean.db` y `construir_db.py` en la carpeta del repo.

Todo el trabajo vive en esa branch, y al final le hacemos **merge** a `main` con un Pull Request.

---

## Las misiones

Ritmo sugerido; ve a tu velocidad.

### Misión 1 — Abre la base y mira (GUI) — Día 1
- Instala **DB Browser for SQLite** (gratis): https://sqlitebrowser.org/
- Abre `ocean.db`. Mira las dos tablas (`readings` y `sites`): sus columnas y sus filas.
- En la pestaña "Execute SQL", escribe tu primer query:
  ```sql
  SELECT date, temp FROM readings WHERE site = 'monterey';
  ```
- **Aprendes:** qué es una tabla (filas y columnas), `SELECT ... FROM`, y filtrar con `WHERE`.

### Misión 2 — Pregunta con GROUP BY — Día 2
- ¿Cuántas lecturas válidas tiene cada sitio?
  ```sql
  SELECT site, COUNT(*) FROM readings GROUP BY site;
  ```
- ¿Cuál es la temperatura **promedio** de cada sitio?
  ```sql
  SELECT site, ROUND(AVG(temp), 2) FROM readings GROUP BY site;
  ```
- **Aprendes:** funciones de agregado (`COUNT`, `AVG`) y `GROUP BY`.
- 👀 Fíjate: ¡ese promedio es exactamente lo que calculaste la semana pasada con un `dict` y un loop! Compara los números con tu programa de la semana 3.

### Misión 3 — Filtra y ordena — Día 3
- Días de "alerta" (temperatura sobre 15°C) por sitio:
  ```sql
  SELECT site, COUNT(*) FROM readings WHERE temp > 15 GROUP BY site;
  ```
- El día más caluroso de todos:
  ```sql
  SELECT date, site, temp FROM readings ORDER BY temp DESC LIMIT 1;
  ```
- **Aprendes:** combinar `WHERE` con `GROUP BY`, y ordenar con `ORDER BY` + `LIMIT`.

### Misión 4 — Une dos tablas con JOIN — Día 4
Las dos tablas se conectan por la columna `site`. Únelas para ver el promedio de cada sitio junto con su región legible:
```sql
SELECT s.region, s.description, ROUND(AVG(r.temp), 2)
FROM readings r
JOIN sites s ON r.site = s.site
GROUP BY r.site;
```
- **Aprendes:** `JOIN ... ON`, y por qué los datos se guardan repartidos en varias tablas (una para lecturas, otra para la info de cada sitio).

### Misión 5 — Las mismas consultas, en CLI y en Python — Día 5
Elige 2 o 3 de tus consultas y córrelas también:
- **En la terminal**, con el CLI de SQLite:
  ```
  sqlite3 ocean.db
  ```
  (y adentro escribes tus queries; en Mac ya viene instalado). Para salir: `.quit`
- **Desde Python**, con el módulo `sqlite3` (viene incluido). Es la forma en que una app real —como las de Bloom— le pregunta a la base:
  ```python
  import sqlite3
  con = sqlite3.connect("ocean.db")
  for fila in con.execute("SELECT site, AVG(temp) FROM readings GROUP BY site;"):
      print(fila)
  ```
- **Aprendes:** que una misma consulta se puede correr con distintas herramientas.

### Misión 6 — README (comparación) + dominio + PR — Día 6
- En tu `README.md`, agrega una **tabla comparando las tres formas** (GUI / CLI / Python): un pro, un contra, y cuándo usarías cada una. Es la parte más importante de la semana: que entiendas que hay varias herramientas y cuál conviene según la situación.
- Agrega una línea de dominio: cómo un sistema de alertas real (como BloomAlert) le preguntaría a su base de datos "¿qué sitios tienen agua más cálida de lo normal?" — justo lo que hiciste con SQL.
- Guarda todo con commits, sube la branch (`git push -u origin semana-4-sql`), abre un **Pull Request** hacia `main` con título y descripción, y hazle **merge**.

---

## Si usas IA (Claude / Gemini / ChatGPT), hazlo así 🤖

En caso de que quieras apoyarte en alguna IA, dos reglas simples para de verdad aprender y no solo copiar:

1. **Escribe tú misma cada query.** Aunque la IA te muestre el SQL, escríbelo con tus manos — nunca copies y pegues.
2. **Úsala para *entender*, no para que te haga la tarea.**
   - ✅ *"¿Qué hace `GROUP BY` en SQL?"*
   - ✅ *"¿Cuál es la diferencia entre `WHERE` y `HAVING`?"*
   - ❌ *"Escríbeme las consultas de esta tarea."*

La IA es un buen tutor cuando le preguntas para aprender. Es una mala idea cuando le pides que piense por ti.

---

## ¿Cuándo terminaste?

Cuando hayas:
- corrido consultas con `SELECT`, `WHERE`, `GROUP BY` (con `COUNT`/`AVG`), `ORDER BY` y un `JOIN` de las dos tablas,
- corrido al menos una de esas consultas en las **tres** formas (GUI, CLI y Python),
- y escrito en tu `README.md` la **tabla comparando las tres herramientas** + la línea de dominio.

Y todo esté en tu branch `semana-4-sql`, con un **Pull Request** abierto y con **merge** hecho a `main`.

Entonces **avísame** y lo revisamos juntos. Te voy a pedir que me expliques con tus palabras: la diferencia entre `WHERE` y `GROUP BY`, qué devuelve un `AVG`, qué hace el `ON` de tu `JOIN`, y qué herramienta usarías para un reporte automático (y por qué). No es un examen — es para asegurarnos de que de verdad lo entendiste. 🙂

¡Éxito! Cualquier duda, escríbeme a **saldivia@bloomalert.com**.
