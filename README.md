# Semana 5 — APIs: datos del océano en vivo
Este proyecto en Python consulta la API de Open-Meteo Marine para extraer datos de temperatura de la superficie del mar en coordenadas específicas y realizar un análisis de riesgo ambiental.

## Dominio del Proyecto
El proyecto se enfoca en la oceanografía y biología marina. Evalúa las fluctuaciones térmicas en el océano para detectar posibles riesgos de floración algal o estrés en ecosistemas marinos en los sitios Monterey y San Pedro.

## Funcionalidades
- **Extracción de datos:** Peticiones HTTP a la API pública de Open-Meteo.
- **Procesamiento JSON:** Decodificación y formateo de la respuesta estructurada.
- **Análisis estadístico:** Cálculo de temperatura promedio y máxima para una semana definida.
- **Evaluación de riesgo:** Clasificación automática del sitio en riesgo "elevado" o "normal" según el umbral de 18°C.