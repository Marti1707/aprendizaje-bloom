# Proyecto Final - Semana 4: SQL

## Misión 6: Comparación de Herramientas SQL

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
´´´sql
SELECT site, date, temp
FROM readings
WHERE temp > 15;