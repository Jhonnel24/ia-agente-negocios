import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="IA Agent Pro", page_icon="🤖")
st.title("🤖 IA Business Agent")

# Configuración de API Key en la barra lateral
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

text = st.text_area("Mensaje del cliente o problema a resolver:")

if st.button("Generar Solución"):
    if not api_key:
        st.error("Introduce tu API Key en la barra lateral izquierda.")
    else:
        client = OpenAI(api_key=api_key)
        with st.spinner('Analizando...'):
            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "Analiza y responde profesionalmente en español."},
                          {"role": "user", "content": text}]
            )
            st.success("Respuesta de la IA:")
            st.write(res.choices[0].message.content)
