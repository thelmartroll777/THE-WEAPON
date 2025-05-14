
import streamlit as st
import pandas as pd
from openai import OpenAI

# Título
st.title("🔍 Chatbot Analista de Datos con OpenAI")

# Obtener API key desde Streamlit secrets
api_key = st.secrets["openai"]["api_key"]

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("FuelConsumption (1).csv")
    return df

df = load_data()

# Mostrar datos
st.subheader("📊 Vista previa del Dataset")
st.dataframe(df.head(100))

# Entrada de pregunta
question = st.text_area("✍️ Escribe tu pregunta sobre el dataset:")

# Procesar
if st.button("💬 Preguntar"):
    if not question.strip():
        st.warning("Por favor escribe una pregunta.")
    else:
        # Preparar cliente
        client = OpenAI(api_key=api_key)
        df_string = df.head(100).to_string()

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a data analyst. Here is the data:\n" + df_string},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            st.success("✅ Respuesta del chatbot:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ Error al consultar la API: {e}")
