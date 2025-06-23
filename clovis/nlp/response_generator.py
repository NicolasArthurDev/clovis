import requests
import json
import streamlit as st

def set_name(nome: str, pronomes: str):
    if pronomes.lower() == "ele/dele":
        nome_usuario = f"Senhor {nome}"
    elif pronomes.lower() == "ela/dela":
        nome_usuario = f"Senhora {nome}"
    else:
        nome_usuario = nome
    return nome_usuario

# Essa função é para rodar no streamlit_app para obtermos o nome do usuário e o agente poder se referir a ele corretamente
def set_name_system_prompt(nome: str, pronomes: str):
    nome_usuario = set_name(nome, pronomes)
    return f"""
Você é Clovis, um mordomo virtual que responde com gentileza, formalidade e objetividade.

Trate o usuário com respeito e sempre se refira a ele como "{nome_usuario}". Na maioria das vezes, responda o usuário chamando ele apenas com a senioridade.
Nunca use saudações desnecessárias.
Se não souber uma resposta, diga que ainda está aprendendo.

Seja direto, educado e útil em todas as respostas.
"""

# Formata mensagens no estilo de chat normal

def format_messages(messages, system: str, modelo="mistral"):
    formatted = ""
    # Só inclui o system_prompt se for a primeira mensagem
    if not messages or messages[0]["role"] != "system":
        formatted += f"system: {system.strip()}\n\n"
    for m in messages:
        role = "user" if m["role"] == "user" else "assistant"
        formatted += f"{role}: {m['content'].strip()}\n"
    formatted += "assistant:"
    return formatted.strip()

# Streaming (resposta em tempo real)
def stream_llm_response(prompt: str, system: str, modelo: str = "mistral", messages=None):
    url = "http://localhost:11434/api/generate"
    if messages is None:
        messages = []

    full_history = messages + [{"role": "user", "content": prompt}]
    prompt_final = format_messages(full_history, system=system, modelo=modelo, )

    payload = {
        "model": modelo,
        "prompt": prompt_final,
        "stream": True
    }

    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    yield data["response"]

    except requests.RequestException as e:
        print(f"[Erro Ollama - stream] {e}")
        yield "Erro ao se comunicar com o modelo local."


# Versão tradicional (resposta completa) stream = false
def get_llm_response(prompt: str, system: str, modelo: str = "mistral", messages=None) -> str:
    url = "http://localhost:11434/api/generate"
    if messages is None:
        messages = []

    full_history = messages + [{"role": "user", "content": prompt}]
    prompt_final = format_messages(full_history, system=system, modelo=modelo)

    payload = {
        "model": modelo,
        "prompt": prompt_final,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
    except requests.RequestException as e:
        print(f"[Erro Ollama] {e}")
        return "Erro ao se comunicar com o modelo local."
