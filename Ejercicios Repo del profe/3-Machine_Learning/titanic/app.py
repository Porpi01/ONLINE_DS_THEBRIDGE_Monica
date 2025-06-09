import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ----------------------
# Cargar el modelo
# ----------------------
with open("mimodelo.pkl", "rb") as file:
    mi_modelo = pickle.load(file)

# ----------------------
# Función de preprocesamiento
# ----------------------
def preprocess_input(Pclass, sex, Age, Fare, embarked):
    Sex = 1 if sex == "male" else 0
    c = 1 if embarked == "C" else 0
    q = 1 if embarked == "Q" else 0
    s = 1 if embarked == "S" else 0

    data = {
        'Pclass': [Pclass],
        'Sex': [Sex],
        'Age': [Age],
        'Fare': [Fare],
        'C': [c],
        'Q': [q],
        'S': [s]
    }

    return pd.DataFrame(data)

# ----------------------
# Configuración de la página
# ----------------------
st.set_page_config(
    page_title="Predicción Titanic",
    page_icon="https://www.schiffsmodell.net/uploads/gallery/album_519/gallery_10389_519_469842.jpg",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Titanic Predictor App 🚢 - predicción con modelo.pkl"
    }
)

# ----------------------
# Menú lateral
# ----------------------
menu = st.sidebar.selectbox("Navegación", ["Predicción", "Información"])
# ----------------------
# Estilo personalizado
# ----------------------
st.markdown("""
    <style>
    .main {
        background-color: #f4f9ff;
    }

    h1 {
        color: #003566;
    }

    .stForm {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }

    .stSelectbox, .stSlider, .stNumberInput {
        color: #000000;
    }

    button[kind="primary"] {
        background-color: #0077b6;
        color: white;
        border-radius: 8px;
    }

    .stAlert-success {
        background-color: #d8f3dc;
        color: #1b4332;
    }

    .stAlert-error {
        background-color: #ffe5ec;
        color: #800f2f;
    }

    .stAlert-info {
        background-color: #e0f7fa;
        color: #004d40;
    }

    .stAlert-warning {
        background-color: #fff3cd;
        color: #856404;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------
# Sección Predicción
# ----------------------
if menu == "Predicción":
    st.title("Predicción de Supervivencia en el Titanic")
    st.markdown("Introduce los datos del pasajero para saber si **sobrevivirá o no**.")

    with st.form("formulario_prediccion"):
        st.markdown("### Formulario")
        Pclass = st.selectbox("Clase del pasajero", [1, 2, 3], index=None)
        sex = st.selectbox("Sexo", ["male", "female"], index=None)
        Age = st.slider("Edad", 0, 80, 30)
        Fare = st.slider("Tarifa (Fare)", 0.0, 512.3, 32.2)
        embarked = st.selectbox("Puerto de embarque", ["C", "Q", "S"], index=None)
        enviar = st.form_submit_button("Predecir")

    if enviar:
        if Pclass is None or sex is None or embarked is None:
            st.warning("Por favor, completa todos los campos obligatorios (Clase, Sexo, Puerto).")
        else:
            entrada = preprocess_input(Pclass, sex, Age, Fare, embarked)
            pred = mi_modelo.predict(entrada)[0]
            proba = mi_modelo.predict_proba(entrada)[0][1]

            st.markdown("---")
            st.write(f"**Probabilidad de supervivencia:** `{proba*100:.2f}%`")

            if pred == 1:
                st.success("Sobrevive")
            else:
                st.error("No sobrevive.")

            # Comentarios adicionales
            if Pclass == 1:
                st.info("Los pasajeros de primera clase tenían más probabilidades de sobrevivir.")
            elif Pclass == 3:
                st.warning("Los pasajeros de tercera clase tenían menos probabilidades de sobrevivir.")

# ----------------------
# Sección Información
# ----------------------
elif menu == "Información":
    st.title("📜 Historia del RMS Titanic")
    st.markdown("""
    El **RMS Titanic** fue un transatlántico británico que se hundió en la madrugada del 15 de abril de 1912, después de chocar contra un iceberg durante su viaje inaugural de Southampton a Nueva York.

    - Construido en Belfast, Irlanda del Norte.
    - Tenía capacidad para más de 2200 pasajeros y tripulación.
    - Solo se disponía de botes salvavidas para aproximadamente la mitad de los ocupantes.
    - Murieron más de 1500 personas, convirtiéndose en uno de los desastres marítimos más trágicos de la historia.

    Esta aplicación usa datos históricos y un modelo predictivo para estimar la supervivencia de pasajeros basándose en ciertas características.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg", use_container_width=True)

    st.markdown("---")
    st.title("🎬 El Titanic en el Cine")
    st.markdown("""
    En 1997, el director **James Cameron** estrenó la película _Titanic_, una superproducción protagonizada por **Leonardo DiCaprio** y **Kate Winslet**.

    - Ganó **11 premios Óscar**, incluyendo Mejor Película y Mejor Director.
    - Mezcla hechos históricos con una historia de amor ficticia entre Jack y Rose.
    - Se convirtió en una de las películas más taquilleras de todos los tiempos.
    - Destaca por sus efectos visuales, la reconstrucción del barco y su banda sonora con la canción **"My Heart Will Go On"** de Celine Dion.

    La película generó un gran interés mundial por la historia real del Titanic y contribuyó a mantener viva su memoria en la cultura popular.
    """)
    st.image("https://pics.filmaffinity.com/Titanic-733113285-large.jpg", caption="Cartel oficial de la película Titanic (1997)", use_container_width=True)

    st.markdown("---")
    VIDEO_URL = "https://www.youtube.com/watch?v=9bFHsd3o1w0"
    st.video(VIDEO_URL)
    st.markdown("""La película *Titanic* de 1997 cuenta con una de las bandas sonoras más icónicas del cine y una historia épica de amor en medio del 
                desastre marítimo más famoso de la historia moderna.""")