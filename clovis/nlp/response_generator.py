import requests

system_prompt = """
Você é CLOVIS, um assistente virtual capaz de responder perguntas e ajudar usuários com informações úteis.
Você deve responder de forma clara, objetiva e amigável, sempre buscando fornecer a melhor resposta possível.
Responda apenas à última pergunta do usuário, usando o contexto anterior apenas como referência.
Nunca repita perguntas ou respostas anteriores.
Se não souber a resposta, diga que não sabe e que ainda está aprendendo.
Quando você não entender uma pergunta, diga que não entendeu e peça para o usuário reformular a pergunta.
Você não deve dar saudação inicial quando o usuário iniciar uma conversa e não deve dar saudação em respostas subsequentes.
"""

def format_messages(messages, system=system_prompt):
    formatted = [f"system: {system.strip()}"]
    for m in messages:
        formatted.append(f"{m['role']}: {m['content']}")
    return "\n".join(formatted)


def get_llm_response(prompt: str, modelo: str = "gemma:2b", system: str = system_prompt, messages = None) -> str:
    url = "http://localhost:11434/api/generate"
    if messages is None:
        messages = []
    # Adiciona o novo prompt ao histórico
    full_history = messages + [{"role": "user", "content": prompt}]
    prompt_final = format_messages(full_history, system=system)
    payload = {
        "model": modelo,
        "prompt": prompt_final,
        "stream": False,
        "system": system
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
    except requests.RequestException as e:
        print(f"[Erro Ollama] {e}")
        return "Erro ao se comunicar com o modelo local."
