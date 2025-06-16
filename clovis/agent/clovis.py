from gtts import gTTS
import pygame
import os
from clovis.memory.dialogues import Dialogue

class Clovis:
    def __init__(self):
        self.dialogo = Dialogue()

# Função para converter texto em áudio
def converterTextoEmAudio(texto):
    tts = gTTS(text=texto, lang='pt-br')  # Usando o argumento texto
    tts.save("clovis/memory/temp/answer.mp3")  # Salvando o áudio
    reproduzirAudio()

def printarTexto(texto):
        print(texto +"\n")
        converterTextoEmAudio(texto)
        while pygame.mixer.music.get_busy():
            pass

def reproduzirAudio():
    # Inicializando o pygame mixer para reprodução de áudio
    pygame.mixer.init()
    pygame.mixer.music.load("clovis/memory/temp/answer.mp3")  # Carregando o arquivo de áudio
    pygame.mixer.music.play()  # Reproduzindo o áudio

os.system('clear')
print("Iniciando projeto Clovis...\n\n")

clovis = Clovis()  # Crie a instância

texto = clovis.dialogo.interacaoInicial()
printarTexto(texto)
while True:
    userText = input().lower()

    if userText.lower() == "sair":
        texto = clovis.dialogo.interacaoFinal()
        printarTexto(texto)
        break
    else:
        texto = clovis.dialogo.perguntasERespostas(userText)
        printarTexto(texto)

