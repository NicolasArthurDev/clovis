import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clovis.nlp.response_generator import get_llm_response
import streamlit as st

st.title("Clovis")

## Mensagem inicial pré definida (Alterar futuramete para ser dinâmica)
with st.chat_message(name="assistant"):
    st.write("Olá! Meu nome é **Clovis**, como posso ajudar?")
    
# Historico
if "messages" not in st.session_state:
    st.session_state.messages = []


    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Envio de mensagens
prompt = st.chat_input("Boas vindas! Digite sua mensagem aqui:")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    # Limite o histórico para as últimas 2 interações
    N = 4
    history = st.session_state.messages[-N*2:]

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_llm_response(prompt, messages=history)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
