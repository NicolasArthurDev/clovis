import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clovis.nlp.response_generator import stream_llm_response, set_name_system_prompt

# Pega as informações do usuário
@st.dialog("Personalização do usuário")
def user_info() -> dict: 
    nome_usuario = st.text_input("Como você gostaria de o agente te chamasse?", value="") 
    pronomes_usuario = st.radio("Selecione seus pronomes:",
        key="pronomes_usuario",
        options=["Ele/Dele", "Ela/Dela", "Elu/Delu"],
    )
    if st.button("Submit"):
        st.session_state.user_info = {"nome": nome_usuario, "pronomes": pronomes_usuario}
        st.success("Informações salvas com sucesso!")
        st.rerun()
    
if "user_info" not in st.session_state:
    user_info()

# Gera o prompt do sistema com base nas informações do usuário 
system_prompt = set_name_system_prompt(
    st.session_state.user_info["nome"],
    st.session_state.user_info["pronomes"]
)

if system_prompt:

    st.title("Assistente Virtual C.L.O.V.I.S.")
    st.text("Powered by Mistral LLM")

    with st.chat_message(name="assistant"):
        st.write("Meu nome é **Clovis**, como posso te ajudar?")

    # Histórico de mensagens
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": system_prompt}]
        
    # Mostrar o histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input do usuário
    prompt = st.chat_input("Digite sua mensagem aqui")

    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)

        # Pega as últimas interações para manter passar o contexto para o modelo
        N = 4
        history = st.session_state.messages[-N*2:]

        st.session_state.messages.append({"role": "user", "content": prompt})

        # Mostrar resposta enquanto é gerada (stream = true)
        with st.chat_message("assistant"):
            full_response = ""
            message_placeholder = st.empty()

            for chunk in stream_llm_response(prompt, system_prompt, messages=history):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌") # Mostar a barra piscando

            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
