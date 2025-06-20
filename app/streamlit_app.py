import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clovis.memory.dialogues import Dialogue
import streamlit as st


dialogue = Dialogue()

# Está página ainda não está pronta e não possui integração com o Clovis

st.title("Clovis")

## Mensagem inicial pré definida (Alterar futuramete para ser dinâmica)
with st.chat_message(name="assistant"):
    st.write("Olá! Meu nome é **Clovis** e ainda estou em desenvolvimento :)")
    
# Historico
if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Envio de mensagens
prompt = st.chat_input("Seja bem-vindo! Como posso ajudar?")

if prompt:
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # adiciona ao historico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # por enquanto apenas repete
    response = dialogue.perguntasERespostas(prompt)
    
    # response = f"Você disse: {prompt}"
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
