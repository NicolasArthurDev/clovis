from clovis.agent.clovis import Clovis
from clovis.memory.dialogues import Dialogue

def main():
    clovis = Clovis()
    texto = clovis.dialogo.interacaoInicial()

    print(texto)
    
    while True:
        user_input = input().strip().lower()
        
        if user_input == "sair":
            print(Dialogue.interacaoFinal())
            break
        else:
            response = Dialogue.perguntasERespostas(user_input)
            print(response)