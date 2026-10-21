# Semana 1 - Terminal, Git y GitHub
## Preguntas:
### ¿Qué es un algal bloom y por qué puede ser un problema?
Un algal bloom es un crecimiento rápido y desproporcionado de algas o fitoplancton (conjunto de organismos acuáticos de carácter vegetal y microscópico que viven flotando en la columna de agua de océanos, mares, lagos y ríos) en el agua. Es un problema porque, al multiplicarse en exceso, pueden agotar el oxígeno del agua, bloquear la luz solar para otros organismos y, en muchos casos, liberar toxinas dañinas para la salud de los animales y los seres humanos.  

### ¿Por qué le importaría a la industria acuícola o al océano?
A la industria acuícola le afecta de manera directa porque las floraciones tóxicas o la escasez de oxígeno provocan la muerte masiva de salmones, peces o mariscos en cultivo, causando pérdidas económicas críticas. Para el océano, alteran profundamente el equilibrio ecológico, generando zonas donde la vida marina no logra sobrevivir.

### ¿Qué hace BloomAlert?
BloomAlert funciona como una herramienta de monitoreo y advertencia temprana que detecta o predice la aparición de floraciones algales dañinas. Esto permite anticiparse al problema para tomar medidas preventivas en los centros de cultivo y cuidar el ecosistema.

# Semana 2 - Primer script en Python

## Análisis de Temperatura Marina

### ¿Qué hace el programa?
Este script procesa datos de temperatura del mar desde el archivo `ocean-temps.csv` Lee cada registro, filtra los datos no válidos (como lecturas registradas como `NN`), y calcula:
- Temperatura mínima
- Temperatura máxima
- Temperatura promedio

### Relación de la temperatura del mar con las floraciones de algas
La temperatura del agua es un factor clave en el surgimiento y desarrollo de las floraciones algales. Temperaturas más cálidas suelen acelerar el metabolismo y la reproducción del fitoplancton, favoreciendo la aparición rápida e intensa de floraciones algales dañinas. Monitorear estos cambios de temperatura permite predecir condiciones de riesgo.

# Semana 3 - Funciones, filtros y diccionarios

## Análisis Modular y Días de Alerta por Sitio

### ¿Qué hace el programa actual?
El programa organiza el procesamiento de datos utilizando funciones modulares y diccionarios para agrupar las temperaturas de distintos sitios (`monterey` y `san_pedro`), evaluando mediante una función de alerta cuáles días superan un umbral de temperatura determinado.

### ¿Por qué un día de alerta por agua más cálida podría ser una señal temprana de riesgo de floración de algas?
porque el incremento de la temperatura acelera de forma directa la tasa metabólica y la velocidad de reproducción del fitoplancton. Cuando el agua se calienta por encima de lo normal, se crean las condiciones ideales para que las algas crezcan masivamente en poco tiempo.

# Semana 4 — SQL: las mismas consultas de tres formas distintas

## Comparación de Herramientas SQL

### Comparación entre GUI, CLI y Python (Pros, Contras y cuando utilizar)
- **GUI (DB Browser for SQLite):** 
*Pro:* Es muy intuitiva y visual, no se necesita escribir codigo para explorar las tablas; puede ver las filas, columnas y nombres y datos como si fuera una planilla de exel. Facilita hacer inspecciones rapidas, revisar la estructura de datos o detectar errores.
*Contra:* No es automatizable, siempre requiere que se abra el programa, se hagan clicks y presionen botones manualmente, por eso no sirve para construir sistemas automaticos, ademas al tener que procesar ventanas, botones y renderizar tablas graficas consume mas memoria RAM y procesador que la terminal.
*Cuando utilizar:* La utilizaria para explorar los datos visualmente, probar consultas SQL antes de utilizarlas en codigo y hacer correcciones manuales rapidas.

- **CLI (Terminal):** 
*Pro:* Es liviana y rapida, funciona en cualquier servidor o equipo sin la necesidad de instalar entornos graficos ni gastar memoria RAM.
*Contra:* No es visual, tienes que memorizar los comandos y sintaxis SQL y ver las tablas en texto plano.
*Cuando utilizar:* Se utiliza para hacer consultas rapidas o revisiones directamente en la terminal especialmente al trabajar en servidores remotos, donde no hay interfaz grafica disponible.

- **Python:**
*pro:* Es 100% automatizable, permite integrar la base de datos con la logica de la forma en que se aplica, procesa informacion de forma masiva y conecta con otros servicios.
*contra:* Requiere escribir codigo, hay que gestionar conecciones, 
*Cuando utilizar:* Es la mejor opción para integrar las consultas a un sistema real (como BloomAlert), permitiendo procesar datos y tomar decisiones automáticas.

### Aplicacion al dominio (Bloom Alert)
En un sistema real como  **Bloom Alert**, la base de datos almacena las lecturas marinas y la logica del programa en python procesa los rsultados automaticamente.
Por ejemplo una consulta SQL como:
 ```sql
SELECT site, date, temp
FROM readings
WHERE temp > 15;
 ```
# Semana 5 — APIs: datos del océano en vivo
## Dominio del Proyecto
El proyecto se enfoca en la oceanografía y biología marina. Evalúa las fluctuaciones térmicas en el océano para detectar posibles riesgos de floración algal o estrés en ecosistemas marinos en los sitios Monterey y San Pedro.

### Monitoreo de Temperatura y Riesgo Ambiental
El script `misiones.py` consulta en tiempo real la API de Open-Meteo Marine para calcular la temperatura promedio y máxima de la superficie del mar (SST) en Monterey y San Pedro.

#### ¿Qué es un "sitio de riesgo elevado" y por qué se asocia al algal bloom?
- **Umbral crítico:** Un sitio se clasifica con **riesgo elevado** cuando la temperatura promedio de la superficie del mar supera los **18.0 °C**.
- **Fundamento oceanográfico:** Las temperaturas superficiales más cálidas reducen la solubilidad del oxígeno en el agua y generan condiciones de estabilidad térmica óptimas para la multiplicación exponencial de microalgas. Estas floraciones masivas pueden agotar el oxígeno disuelto (generando hipoxia) y liberar toxinas nocivas para la fauna marina, de ahí la importancia de que el sistema automatice esta alerta temprana.

## Funcionalidades
- **Extracción de datos:** Peticiones HTTP a la API pública de Open-Meteo.
- **Procesamiento JSON:** Decodificación y formateo de la respuesta estructurada.
- **Análisis estadístico:** Cálculo de temperatura promedio y máxima para una semana definida.
- **Evaluación de riesgo:** Clasificación automática del sitio en riesgo "elevado" o "normal" según el umbral de 18°C.

## Ajustes finales - Review Semana 5

- **Enlace al comentario de review:** https://github.com/Marti1707/aprendizaje-bloom/pull/24#issuecomment-review

#### ¿Qué se cambió?
1. **Archivo personal:** Se removió del seguimiento de Git el documento `.docx` que se había colado por error.
2. **README.md:** Se unificaron las secciones repetidas y se corrigió el bloque de código SQL.
3. **misiones.py:** Se implementó `timeout=10`, manejo de excepciones específicas (`URLError`, `JSONDecodeError`) y filtrado de nulos.

#### Pruebas realizadas:
- Se ejecutó el script localmente para verificar el cálculo de las temperaturas y la clasificación de riesgo en Monterey y San Pedro.

