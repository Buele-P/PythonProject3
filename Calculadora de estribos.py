
import streamlit as st
import math

# CONFIGURACION
st.set_page_config(
    page_title="Calculadora de Estribos",
    page_icon="🏗️",
    layout="centered"
)

# DISEÑO
st.markdown("""
<style>
.stApp {
    background-color: #172B3A;
}
h1, h2, h3, p, label {
    color: white !important;
}
.stButton button {
    background-color: #16A085;
    color: white;
    font-weight: bold;
    width: 100%;
    height: 50px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# TITULO
st.title("🏗️ CALCULADORA DE ESTRIBOS")
st.subheader("Cálculo para vigas y columnas")

st.write(
    "Ingresa las dimensiones del elemento estructural "
    "y la separación de diseño entre estribos."
)

st.markdown("---")

# TIPO DE ELEMENTO
tipo = st.selectbox(
    "Selecciona el elemento:",
    ["Viga", "Columna"]
)

# DIMENSIONES
st.subheader("📐 Dimensiones del elemento")

largo = st.number_input(
    "Longitud de la viga o altura de la columna (m)",
    min_value=0.10,
    max_value=30.0,
    value=4.0,
    step=0.10
)

ancho = st.number_input(
    "Ancho de la sección (cm)",
    min_value=10.0,
    max_value=200.0,
    value=25.0,
    step=5.0
)

alto = st.number_input(
    "Alto de la sección (cm)",
    min_value=10.0,
    max_value=200.0,
    value=40.0,
    step=5.0
)

# SEPARACION
st.markdown("---")
st.subheader("📏 Separación de estribos")

separacion = st.number_input(
    "Distancia máxima entre estribos (cm)",
    min_value=1.0,
    max_value=100.0,
    value=15.0,
    step=1.0
)

# CALCULO
if st.button("CALCULAR ESTRIBOS"):

    longitud_cm = largo * 100

    # Número de intervalos y estribos
    intervalos = math.ceil(longitud_cm / separacion)
    numero_estribos = intervalos + 1

    # Separación real uniforme
    separacion_real = longitud_cm / intervalos

    # RESULTADOS
    st.markdown("---")
    st.subheader("📊 RESULTADOS")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Cantidad de estribos",
            f"{numero_estribos}"
        )

    with c2:
        st.metric(
            "Separación real",
            f"{separacion_real:.2f} cm"
        )

    st.success(
        f"Para el elemento seleccionado se necesitan "
        f"{numero_estribos} estribos."
    )

    st.markdown("### Dimensiones de la sección")

    st.write(f"**Elemento:** {tipo}")
    st.write(f"**Ancho:** {ancho:.1f} cm")
    st.write(f"**Alto:** {alto:.1f} cm")
    st.write(f"**Longitud:** {largo:.2f} m")

    # DISTRIBUCION
    st.markdown("---")
    st.subheader("📍 Distribución de estribos")

    posiciones = []

    for i in range(numero_estribos):
        posicion = i * separacion_real
        posiciones.append({
            "Estribo": i + 1,
            "Distancia desde el inicio (cm)": round(
                posicion, 2
            )
        })

    st.dataframe(
        posiciones,
        use_container_width=True,
        hide_index=True
    )

    # ESQUEMA
    st.markdown("### Esquema de distribución")

    dibujo = "🔴" + " ─── " * min(intervalos, 15) + "🔴"

    st.markdown(
        f"""
        <div style="
        background-color:#FFFFFF;
        color:#172B3A;
        padding:20px;
        border-radius:12px;
        text-align:center;
        font-size:18px;
        font-weight:bold;">
        {dibujo}
        <br>
        <small>Representación ilustrativa de los estribos</small>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "La separación ingresada debe provenir del diseño "
        "estructural. El programa calcula la cantidad "
        "y distribución uniforme, pero no determina "
        "si esa separación es segura."
    )

st.markdown("---")
st.caption("Calculadora académica de Ingeniería Civil")
