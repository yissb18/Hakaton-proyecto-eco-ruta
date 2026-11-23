# ECO-RUTA

**Movilidad inteligente · Simulación urbana · Decisiones sostenibles**

ECO-RUTA es un prototipo conceptual para estudiar el tráfico urbano, comparar escenarios y apoyar la priorización de intervenciones de movilidad con recursos limitados.

## Funcionalidades del prototipo
- Panel de presentación del concepto.
- Simulador de escenario con parámetros ajustables.
- Comparación de tiempo estimado base y escenario.
- Sección de indicadores de movilidad y sostenibilidad.

> Los cálculos actuales son ilustrativos. No representan resultados de campo ni un modelo validado. Para una versión real se necesitan datos de movilidad, calibración y validación.

## Ejecutar localmente

1. Instala Python 3.10 o superior.
2. Descarga o clona este repositorio.
3. Abre una terminal dentro de la carpeta del proyecto.
4. Instala dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecuta:

```bash
streamlit run app.py
```

## Publicar en Streamlit Community Cloud

1. Sube este proyecto a un repositorio de GitHub.
2. Entra a Streamlit Community Cloud e inicia sesión con GitHub.
3. Selecciona **Create app**.
4. Elige el repositorio, la rama (normalmente `main`) y el archivo principal `app.py`.
5. Pulsa **Deploy**.

## Próximas mejoras
- Importar datos reales desde CSV.
- Incorporar mapa y red vial.
- Modelar interacciones entre vehículos.
- Comparar escenarios con métricas calibradas.
- Integrar análisis asistido por IA de los resultados.
- Estudiar energía y carga solar para infraestructura.

## Estructura

```text
ECO-RUTA/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
