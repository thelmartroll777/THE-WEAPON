import streamlit as st
import pandas as pd
import os
from openai

# Título de la aplicación
st.title("🔍 Chatbot Analista de Datos (con OpenAI)")

# Entrada de la API Key
api_key = st.text_input("🔑 Ingresa tu clave de API de OpenAI:", type="password")

# Cargar el dataset
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(r"D:\Mario\7mo-8vo semestre\IA\Labs\LAB 9\VS LAB9\FuelConsumption (1).csv")
        return df
    except Exception as e:
        st.error(f"No se pudo cargar el dataset: {e}")
        return None

df = load_data()

# Mostrar vista previa
if df is not None:
    st.subheader("📊 Vista previa del dataset")
    st.dataframe(df.head(100))

# Ingreso de pregunta
question = st.text_area("✍️ Escribe tu pregunta sobre el dataset:")

# Procesar si hay clave y pregunta
if st.button("💬 Preguntar al chatbot"):
    if not api_key:
        st.warning("⚠️ Por favor ingresa tu clave de API.")
    elif not question:
        st.warning("⚠️ Por favor escribe una pregunta.")
    else:
        try:
            # Usar la clave directamente
            client = OpenAI(api_key=api_key)

            # Convertir dataframe a string
            df_string = df.head(100).to_string()

            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "Eres un analista de datos, pero cualquier pregunta que no esté relacionado con el data set, sus columnas y elementos tan solo responde 'Por ahora solo me centro en responder preguntas del dataset':\n" + df_string},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            st.success("✅ Respuesta del chatbot:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ Error al consultar la API: {e}")
 #streamlit run THE_WEAPON.py
 #D:\Mario\7mo-8vo semestre\IA\Labs\LAB 9\VS LAB9
 #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
