import streamlit as st
import pandas as pd

st.set_page_config(page_title="ECO-RUTA | Movilidad inteligente", page_icon="🚌", layout="wide")

st.markdown("""
<style>
.main {background: #0b1220;}
[data-testid="stMetric"] {background: #152236; padding: 16px; border-radius: 12px;}
</style>
""", unsafe_allow_html=True)

st.title("🚌 ECO-RUTA")
st.caption("Movilidad inteligente · Simulación urbana · Decisiones sostenibles")
st.info("Prototipo demostrativo: los resultados son estimaciones ilustrativas y no están calibrados con datos reales de Santa Marta.")

tab1, tab2, tab3 = st.tabs(["🏙️ Panel", "🧪 Simulador", "🌱 Impacto"])

with tab1:
    st.subheader("¿Qué busca ECO-RUTA?")
    st.write("Modelar el comportamiento del tráfico urbano y comparar escenarios para identificar intervenciones que puedan mejorar los tiempos de viaje usando recursos limitados.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Enfoque", "Tráfico urbano")
    c2.metric("Herramienta", "Simulación + análisis")
    c3.metric("Meta", "Intervenciones útiles")
    st.markdown("### Flujo del sistema")
    st.write("**Estudios de movilidad → Modelo urbano → Simulación → Análisis → Priorización**")
    st.markdown("### ¿Qué se podría evaluar?")
    st.markdown("- Ajustes en semáforos y cruces\\n- Cambios en rutas o paradas\\n- Prioridad al transporte compartido\\n- Horarios de operación\\n- Ubicación de infraestructura de carga")

with tab2:
    st.subheader("Simulador de escenarios")
    st.write("Modifica los parámetros para observar cómo cambiaría un escenario hipotético.")
    left, right = st.columns(2)
    with left:
        vehicles = st.slider("Vehículos en el tramo (por hora)", 100, 2000, 800, 100)
        road_capacity = st.slider("Capacidad estimada del tramo (vehículos/h)", 300, 1800, 1000, 100)
    with right:
        intervention = st.selectbox("Intervención a probar", [
            "Sin intervención", "Optimizar semáforos", "Priorizar transporte compartido",
            "Ajustar paradas", "Cambiar distribución de carriles"
        ])
        intensity = st.slider("Efectividad hipotética de la intervención (%)", 0, 40, 15, 5)

    congestion = max(0, vehicles / max(road_capacity, 1) - 0.5)
    base_minutes = 12 + congestion * 18
    reduction = 0 if intervention == "Sin intervención" else intensity / 100
    estimated_minutes = max(2, base_minutes * (1 - reduction))
    saved = base_minutes - estimated_minutes

    m1, m2, m3 = st.columns(3)
    m1.metric("Tiempo base estimado", f"{base_minutes:.1f} min")
    m2.metric("Tiempo con escenario", f"{estimated_minutes:.1f} min")
    m3.metric("Tiempo potencial ahorrado", f"{saved:.1f} min", delta=f"{reduction*100:.0f}%")

    comparison = pd.DataFrame({
        "Escenario": ["Base", intervention],
        "Tiempo estimado (min)": [base_minutes, estimated_minutes]
    })
    st.bar_chart(comparison.set_index("Escenario"))
    st.caption("Fórmula simplificada para mostrar el funcionamiento de la interfaz. Debe sustituirse por un modelo validado con datos de movilidad.")

with tab3:
    st.subheader("Indicadores que ECO-RUTA podría medir")
    st.write("Los indicadores definitivos se calcularían cuando el proyecto tenga datos reales y un modelo probado.")
    st.markdown("""
    - **Tiempo de viaje:** comparar recorridos antes y después.
    - **Congestión:** observar volumen de vehículos frente a capacidad.
    - **Energía:** estimar consumo por recorrido y aporte solar a infraestructura.
    - **Emisiones:** comparar escenarios usando factores de emisión documentados.
    - **Prioridad de intervención:** identificar lugares donde una mejora tenga mayor beneficio esperado.
    """)
    st.warning("No se presentan ahorros de energía, emisiones ni tiempos como resultados reales. Este prototipo sirve para explorar el concepto.")

st.divider()
st.caption("ECO-RUTA · Prototipo académico en desarrollo")
