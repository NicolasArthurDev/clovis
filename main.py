from gtts import gTTS
import pygame
import os
from modules.dialogos import Dialogos

dialogo = Dialogos()

# Função para converter texto em áudio
def converterTextoEmAudio(texto):
    tts = gTTS(text=texto, lang='pt-br')  # Usando o argumento texto
    tts.save("modules/temp/resposta.mp3")  # Salvando o áudio
    reproduzirAudio()

def printarTexto(texto):
        print(texto +"\n")
        converterTextoEmAudio(texto)
        while pygame.mixer.music.get_busy():
            pass

def reproduzirAudio():
    # Inicializando o pygame mixer para reprodução de áudio
    pygame.mixer.init()
    pygame.mixer.music.load("modules/temp/resposta.mp3")  # Carregando o arquivo de áudio
    pygame.mixer.music.play()  # Reproduzindo o áudio

os.system('clear')
print("Iniciando projeto Clovis...\n\n")

texto = dialogo.interacaoInicial()
printarTexto(texto)
while True:
    userText = input().lower()

    if userText.lower() == "sair":
        texto = dialogo.interacaoFinal()
        printarTexto(texto)
        break
    else:
        texto = dialogo.perguntasERespostas(userText)
        printarTexto(texto)

