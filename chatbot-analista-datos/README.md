
# 🤖 Chatbot Analista de Datos (con Streamlit + OpenAI)

Este proyecto es una aplicación web hecha en Streamlit que actúa como un chatbot analista de datos. Puedes hacerle preguntas sobre un dataset de consumo de combustible.

## 🚀 Cómo usar

1. Sube tu archivo `FuelConsumption (1).csv` en la misma carpeta del código.
2. Agrega tu clave de API en `.streamlit/secrets.toml` así:

```toml
[openai]
api_key = "sk-tu-clave-aquí"
```

3. Ejecuta con:
```bash
streamlit run app.py
```

O despliega gratis en [Streamlit Cloud](https://streamlit.io/cloud).
