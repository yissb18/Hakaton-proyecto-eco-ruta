import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="ECO-RUTA", page_icon="🟢", layout="wide")

st.markdown("""
<style>
:root { --bg:#0B1220; --panel:#142238; --panel2:#182941; --lime:#A6F06A; --teal:#75DCC5; --muted:#AAB8CC; }
.stApp { background: radial-gradient(ellipse at 20% 0%, #152841 0%, #0B1220 50%); color:#F4F7FB; }
.block-container { padding-top: 1.4rem; max-width: 1320px; }
[data-testid="stSidebar"] { background:#0E1829; border-right:1px solid #25364D; }
h1,h2,h3 { letter-spacing:-.035em; }
p,li { color:#B7C3D4; }
div[data-testid="stMetric"] { background:#142238; border:1px solid #263951; border-radius:16px; padding:16px; }
div[data-testid="stMetricLabel"] { color:#AAB8CC; }
div[data-testid="stMetricValue"] { color:#F4F7FB; }
.stButton>button { border-radius:12px; border:1px solid #A6F06A; background:#A6F06A; color:#0B1220; font-weight:700; padding:.65rem 1rem; }
.stButton>button:hover { border-color:#75DCC5; background:#75DCC5; color:#0B1220; }
.stSlider [data-baseweb="slider"] { color:#A6F06A; }
hr { border-color:#263951; }
.hero { padding:2.2rem 2.1rem; border-radius:24px; background:linear-gradient(120deg,rgba(22,41,65,.96),rgba(14,24,41,.93)); border:1px solid #263951; position:relative; overflow:hidden; }
.kicker { color:#A6F06A; letter-spacing:.15em; font-size:.78rem; font-weight:700; }
.hero h1 { font-size:clamp(2.3rem,5vw,4.2rem); line-height:1.02; color:#F4F7FB; margin:.6rem 0 1rem; }
.hero h1 span { color:#75DCC5; }
.hero p { max-width:720px; font-size:1.05rem; line-height:1.65; color:#B7C3D4; }
.card { background:linear-gradient(145deg,#16263D,#111D30); border:1px solid #263951; border-radius:18px; padding:1.1rem 1.2rem; height:100%; }
.card .eyebrow { font-size:.72rem; color:#75DCC5; letter-spacing:.12em; font-weight:700; }
.card h3 { margin:.35rem 0 .45rem; color:#F4F7FB; }
.card p { font-size:.92rem; margin:0; line-height:1.55; }
.pill { display:inline-block; padding:.35rem .7rem; border-radius:99px; border:1px solid #37506A; background:#15263D; color:#75DCC5; font-size:.75rem; }
.route-art { background:#101C2D; border:1px solid #263951; border-radius:18px; padding:1rem; min-height:230px; }
.smallnote { font-size:.8rem; color:#8495AC; }
</style>
""", unsafe_allow_html=True)

def header():
    st.markdown("""
    <div style="display:flex;align-items:center;justify-content:space-between;padding:.25rem 0 1rem;">
      <div style="font-weight:800;font-size:1.15rem;letter-spacing:.04em;color:#F4F7FB;">🟢 ECO-RUTA</div>
      <div style="font-size:.72rem;letter-spacing:.14em;color:#75DCC5;">SMART MOBILITY SYSTEM</div>
    </div>
    """, unsafe_allow_html=True)

header()
page = st.radio("NAVEGACIÓN", ["Inicio", "Simulador", "Metodología", "Impacto"], horizontal=True, label_visibility="collapsed")

if page == "Inicio":
    st.markdown("""
    <div class="hero">
      <div class="kicker">MOVILIDAD URBANA · NUEVA GENERACIÓN</div>
      <h1>La ciudad se mueve.<br><span>Nosotros la entendemos.</span></h1>
      <p>Simulamos el tráfico urbano para explorar mejores soluciones de movilidad, comprender los puntos críticos y priorizar intervenciones con recursos limitados.</p>
      <span class="pill">SIMULACIÓN · DATOS · DECISIONES</span>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><div class="eyebrow">01 / OBSERVAR</div><h3>Comprender la ciudad</h3><p>Usar estudios de movilidad para conocer flujos, tiempos, velocidades y zonas de congestión.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><div class="eyebrow">02 / SIMULAR</div><h3>Probar escenarios</h3><p>Modelar vehículos, vías y condiciones para comparar alternativas antes de intervenir.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><div class="eyebrow">03 / PRIORIZAR</div><h3>Decidir con evidencia</h3><p>Analizar resultados y orientar recursos hacia acciones con mayor beneficio potencial.</p></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("### El sistema, en una mirada")
    st.markdown("""
    <div class="route-art">
    <div style="color:#75DCC5;font-weight:700;letter-spacing:.12em;font-size:.75rem;margin-bottom:.8rem;">FLUJO ECO-RUTA</div>
    <div style="display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;">
      <div style="background:#1B2C45;border:1px solid #304965;border-radius:12px;padding:1rem;color:#F4F7FB;">Estudios de movilidad</div>
      <div style="color:#A6F06A;font-size:1.4rem;">→</div>
      <div style="background:#1B2C45;border:1px solid #304965;border-radius:12px;padding:1rem;color:#F4F7FB;">Modelo urbano</div>
      <div style="color:#A6F06A;font-size:1.4rem;">→</div>
      <div style="background:#1B2C45;border:1px solid #304965;border-radius:12px;padding:1rem;color:#F4F7FB;">Simulación</div>
      <div style="color:#A6F06A;font-size:1.4rem;">→</div>
      <div style="background:#1B2C45;border:1px solid #304965;border-radius:12px;padding:1rem;color:#F4F7FB;">Análisis</div>
      <div style="color:#A6F06A;font-size:1.4rem;">→</div>
      <div style="background:#1B2C45;border:1px solid #304965;border-radius:12px;padding:1rem;color:#F4F7FB;">Priorizar</div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("### ¿Por qué ECO-RUTA?")
    st.write("Las decisiones de movilidad suelen involucrar muchas variables. ECO-RUTA busca ofrecer un entorno para estudiar cómo se relacionan y experimentar con posibles soluciones antes de llevarlas al mundo real.")

elif page == "Simulador":
    st.markdown('<div class="kicker">LABORATORIO DE MOVILIDAD</div>', unsafe_allow_html=True)
    st.title("Simulador de escenarios")
    st.write("Explora cómo cambian los resultados en un tramo urbano hipotético.")
    left, right = st.columns([1,1.35], gap="large")
    with left:
        st.markdown('<div class="card"><div class="eyebrow">PARÁMETROS DEL ESCENARIO</div>', unsafe_allow_html=True)
        vehicles = st.slider("Flujo de vehículos por hora", 100, 2000, 800, 100)
        capacity = st.slider("Capacidad estimada del tramo", 300, 1800, 1000, 100)
        intervention = st.selectbox("Escenario de intervención", ["Sin intervención", "Optimizar semáforos", "Priorizar transporte compartido", "Ajustar paradas", "Cambiar distribución de carriles"])
        strength = st.slider("Efecto hipotético de la intervención (%)", 0, 40, 15, 5)
        st.markdown('</div>', unsafe_allow_html=True)
    ratio = vehicles / max(capacity,1)
    base_time = 10 + max(0, ratio - .35) * 24
    improvement = 0 if intervention == "Sin intervención" else strength/100
    scenario_time = max(2, base_time*(1-improvement))
    saved = base_time-scenario_time
    with right:
        st.markdown('<div class="card"><div class="eyebrow">LECTURA DEL ESCENARIO</div><h3>Comparación estimada</h3>', unsafe_allow_html=True)
        m1,m2,m3 = st.columns(3)
        m1.metric("Tiempo base", f"{base_time:.1f} min")
        m2.metric("Tiempo escenario", f"{scenario_time:.1f} min")
        m3.metric("Diferencia", f"{saved:.1f} min", delta=f"{improvement*100:.0f}%")
        chart=pd.DataFrame({"Tiempo estimado (min)":[base_time,scenario_time]},index=["Base","Escenario"])
        st.bar_chart(chart, color="#75DCC5")
        st.markdown('</div>', unsafe_allow_html=True)
    st.warning("Este cálculo es una demostración conceptual, no un modelo de tráfico calibrado. La próxima etapa sería reemplazarlo por simulación de vehículos y datos reales.")
    st.markdown("#### ¿Qué significa?")
    if intervention == "Sin intervención":
        st.write("Este escenario sirve como referencia para comparar alternativas.")
    else:
        st.write(f"Se está representando una intervención de **{intervention.lower()}** con una reducción hipotética. Su efecto real dependería de datos, diseño y validación.")

elif page == "Metodología":
    st.markdown('<div class="kicker">DEL DATO A LA DECISIÓN</div>', unsafe_allow_html=True)
    st.title("Cómo funciona ECO-RUTA")
    steps = [
        ("01","Estudios de movilidad","Conteos, tiempos, velocidades, origen-destino y puntos de congestión."),
        ("02","Modelo urbano","Representación de vías, cruces, semáforos, paradas y condiciones."),
        ("03","Simulación","Vehículos virtuales interactúan bajo reglas y condiciones configurables."),
        ("04","Análisis asistido","Herramientas analíticas o IA ayudan a comparar resultados y detectar patrones."),
        ("05","Priorización","Se ordenan intervenciones por impacto esperado, costo, viabilidad y recursos.")
    ]
    for n,title,desc in steps:
        st.markdown(f"""
        <div class="card" style="margin-bottom:.7rem;display:flex;gap:1rem;align-items:flex-start;">
          <div style="color:#A6F06A;font-size:1.35rem;font-weight:800;min-width:3rem;">{n}</div>
          <div><h3 style="margin:.1rem 0 .35rem;">{title}</h3><p>{desc}</p></div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("### Intervenciones que se podrían probar")
    st.write("Cambios en semáforos, rutas, paradas, horarios, prioridad de transporte compartido o distribución de carriles. ECO-RUTA no decide por la ciudad: organiza evidencia para apoyar decisiones.")

elif page == "Impacto":
    st.markdown('<div class="kicker">MOVILIDAD · EFICIENCIA · SOSTENIBILIDAD</div>', unsafe_allow_html=True)
    st.title("Medir el impacto, no asumirlo")
    st.write("El proyecto necesitará indicadores y una línea base para evaluar si las alternativas mejoran la movilidad.")
    cards = [
        ("TIEMPO","Duración de recorridos y esperas"),
        ("FLUJO","Volumen, capacidad y congestión"),
        ("ENERGÍA","Consumo estimado y eficiencia"),
        ("AMBIENTE","Emisiones estimadas frente a una línea base"),
        ("RECURSOS","Costo y viabilidad de cada intervención"),
        ("EQUIDAD","Quién se beneficia y qué zonas se priorizan")
    ]
    cols=st.columns(3)
    for i,(title,desc) in enumerate(cards):
        with cols[i%3]:
            st.markdown(f'<div class="card" style="margin-bottom:.8rem;"><div class="eyebrow">{title}</div><p style="margin-top:.5rem;">{desc}</p></div>',unsafe_allow_html=True)
    st.markdown("### Energía limpia: una línea complementaria")
    st.write("La energía solar podría estudiarse para apoyar infraestructura, como puntos de carga o estaciones, según el consumo, la disponibilidad solar y la viabilidad técnica. No se asume que un panel pueda alimentar por sí solo toda la movilidad.")
    st.caption("Los indicadores se deberán calcular con datos documentados, metodología transparente y pruebas.")

st.divider()
st.markdown('<div style="display:flex;justify-content:space-between;color:#8294AC;font-size:.75rem;letter-spacing:.08em;"><span>ECO-RUTA · PROTOTIPO EN DESARROLLO</span><span>SIMULACIÓN · DATOS · MOVILIDAD SOSTENIBLE</span></div>', unsafe_allow_html=True)
