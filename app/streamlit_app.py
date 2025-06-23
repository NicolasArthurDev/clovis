import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clovis.nlp.response_generator import stream_llm_response, set_name_system_prompt

# janela popup para o usuário preencher as informações
@st.dialog("Personalização do usuário")
def user_info(): 
    nome_usuario = st.text_input("Como você gostaria que o agente te chamasse?", value="") 
    pronomes_usuario = st.radio("Selecione seus pronomes:",
        key="pronomes_usuario",
        options=["Ele/Dele", "Ela/Dela", "Elu/Delu"],
    )
    if st.button("Salvar"):
        st.session_state.user_info = {"nome": nome_usuario, "pronomes": pronomes_usuario}
        st.success("Informações salvas com sucesso!")
        st.rerun()

if "user_info" not in st.session_state:
    user_info()
    st.stop()  # 🧠 Para a execução até o usuário preencher!

system_prompt = set_name_system_prompt(
    st.session_state.user_info["nome"],
    st.session_state.user_info["pronomes"]
)

st.title("Assistente Virtual C.L.O.V.I.S.")
st.text("Powered by Mistral LLM")

with st.chat_message(name="assistant"):
    st.write("Meu nome é **Clovis**, como posso te ajudar?")

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar o histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# mensagem do usuario
prompt = st.chat_input("Digite sua mensagem aqui")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    # limita o histórico até as ultimas N mensagens
    N = 4
    history = st.session_state.messages[-N*2:]
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        full_response = ""
        message_placeholder = st.empty()
        
        # Exibe o placeholder com a resposta em tempo real
        for chunk in stream_llm_response(prompt, system_prompt, messages=history):
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # Adiciona a resposta completa ao histórico
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center;">'
    '<p>Developed with ❤ by '
    '<a href="https://github.com/NicolasArthurDev" target="_blank" style="text-decoration: underline; color: blue;">'
    'Nicolas Arthur Raulino Oliveira</a></p>'
    '</div>',
    unsafe_allow_html=True
)
