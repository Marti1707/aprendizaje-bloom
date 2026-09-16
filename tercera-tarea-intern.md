# Tu tercera semana 🌊🔎

¡Vas increíble! En la semana 2 tu programa leía datos y sacaba min/max/promedio. Esta semana das el salto a que tu programa **razone** sobre los datos: que aprenda a **filtrar**, a **decidir** (¿este día es una alerta o no?) y a **organizarse en funciones** — el primer hábito de una programadora de verdad.

Como siempre: no es carrera, y los términos técnicos van en English (function, return, dict, etc.).

---

## El objetivo de la semana

Detectar **días de alerta** en datos de temperatura del mar: días en que la temperatura de un sitio superó cierto **umbral** (threshold). Y hacerlo con el código bien ordenado en **funciones** que puedas reutilizar.

Esta semana el archivo trae **dos sitios** (dos boyas de California): `monterey` (mar más frío) y `san_pedro` (mar más cálido). Te voy a pasar `ocean-temps-2sites.csv`; tiene una columna nueva, `site`. Ponlo dentro de la carpeta del repository.

Regla de oro que ya conoces: solo **Python puro**, nada de instalar librerías todavía.

### Antes de empezar: nueva branch 🌿
Igual que la semana pasada, trabaja en el mismo repository (`mi-aprendizaje-bloom`) pero en una branch nueva:
1. `git checkout main` y `git pull` (para partir actualizada).
2. `git checkout -b semana-3-alertas`
3. Pon el `ocean-temps-2sites.csv` en la carpeta del repo.

Todo tu trabajo de esta semana vive en esa branch, y al final le hacemos **merge** a `main` con un Pull Request.

---

## Las misiones

Ritmo sugerido; ve a tu velocidad.

### Misión 1 — Ordena tu código en funciones (Día 1)
Toma la lógica de la semana 2 y guárdala dentro de **funciones**:
- Una función `leer_datos(archivo)` que lea el CSV, salte las filas `MM`, y devuelva los datos (ahora cada lectura tiene `date`, `site` y la temperatura).
- Una función `promedio(temps)` que reciba una lista de temperaturas y devuelva el promedio.
- **Aprendes:** `def`, parámetros, `return`, y por qué una función te deja **reutilizar** código en vez de repetirlo. Pregúntale a la IA qué hace exactamente `return`.

### Misión 2 — Filtra por sitio (Día 2)
El archivo tiene dos sitios mezclados. Escribe una función `temps_de_sitio(datos, sitio)` que te devuelva **solo** las temperaturas de un sitio (por ejemplo `"monterey"`).
- **Aprendes:** filtrar con un `if` dentro de un loop, construir una **lista** con los resultados, comparar textos (`==`).

### Misión 3 — Marca los días de alerta (Día 3)
Escribe una función `es_alerta(temp, umbral)` que devuelva `True` si la temperatura supera el umbral, y `False` si no. Úsala para contar los días de alerta de un sitio:
- Primero con un **umbral fijo** (por ejemplo `15.0`).
- Después con el **promedio** de ese mismo sitio (que ya sabes calcular). ¡Es la misma función, con otro número!
- **Aprendes:** `if`/`else`, valores `True`/`False` (booleans), y el poder de un **parámetro**: la misma función sirve para cualquier umbral.
- 👀 Fíjate en algo curioso: el umbral fijo de 15 °C marca poquitos días en `monterey` pero casi todos en `san_pedro`. ¿Por qué crees que pasa? Anótalo para contármelo.

### Misión 4 — Agrupa los dos sitios con un dict (Día 4)
Construye un **diccionario** (`dict`) con la forma `{ "monterey": [lista de temps], "san_pedro": [lista de temps] }`, y usa tu función `es_alerta` para reportar cuántos días de alerta tuvo cada sitio.
- **Aprendes:** qué es un `dict` (llave → valor), y recorrer un dict para trabajar cada sitio.

### Misión 5 — Súbelo con un Pull Request + dominio (Día 5)
- Idealmente ya fuiste haciendo `commit` en cada misión (varios commits pequeños > uno gigante). Repasa la sección de buenos commits/PRs de la semana pasada.
- Agrega un par de líneas a tu `README.md`: qué hace tu programa ahora, y —conectando con Bloom— por qué un "día de alerta" por **agua más cálida** podría ser una señal temprana de riesgo de floración de algas (*algal bloom*).
- Sube tu branch: `git push -u origin semana-3-alertas`, abre un **Pull Request** hacia `main` con título y descripción, y hazle **merge**.

---

## Si usas IA (Claude / Gemini / ChatGPT), hazlo así 🤖

En caso de que quieras apoyarte en alguna IA para avanzar o desatascarte, dos reglas simples que hacen que de verdad aprendas en vez de solo copiar:

1. **Escribe tú misma todo el código.** Aunque la IA te muestre la respuesta, escríbela con tus manos — nunca copies y pegues.
2. **Úsala para *entender*, no para que te haga la tarea.**
   - ✅ *"¿Qué significa `return` en una función?"*
   - ✅ *"¿Cuál es la diferencia entre una lista y un dict?"*
   - ❌ *"Escríbeme una función que detecte días de alerta."*

La IA es un buen tutor cuando le preguntas para aprender. Es una mala idea cuando le pides que piense por ti.

---

## ¿Cuándo terminaste?

Cuando tu programa:
- lea el `ocean-temps-2sites.csv` con una función (saltando los `MM`),
- filtre las temperaturas de un sitio,
- marque los días de alerta con `es_alerta`, probado con un umbral fijo **y** con el promedio,
- y agrupe los dos sitios en un `dict` reportando los días de alerta de cada uno.

Y viva en tu branch `semana-3-alertas`, con las líneas nuevas en el `README.md` y un **Pull Request** abierto y con **merge** hecho a `main`.

Entonces **avísame** y lo revisamos juntos. Te voy a pedir que me expliques con tus palabras: por qué usaste funciones y qué hace `return`, cómo funciona el parámetro `umbral`, qué guarda tu `dict`, y por qué el umbral fijo marca tan distinto a los dos sitios. No es un examen — es para asegurarnos de que de verdad lo entendiste. 🙂

¡Éxito! Cualquier duda, escríbeme a **saldivia@bloomalert.com**.
