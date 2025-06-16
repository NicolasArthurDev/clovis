import random
from memory.dialogues import DIALOGUES

class ResponseGenerator:
    def gerar_resposta(self, mensagem):
        mensagem = mensagem.lower()

        for topico, dados in DIALOGUES.items():
            for palavra_chave in dados["intencao"]:
                if palavra_chave in mensagem:
                    return random.choice(dados["resposta"])

        return "Desculpe, não entendi. Pode repetir?"
