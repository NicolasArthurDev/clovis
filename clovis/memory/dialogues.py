class Dialogue:
    def __init__(self, text="", userText=""):
        self.userText = userText.lower()
        self.text = text

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def clear_text(self):
        self.text = ""

    def set_Usertext(self, userText):
        self.Usertext = userText

    def get_text(self):
        return self.Usertext

    def clear_text(self):
        self.Usertext = ""

    def interacaoInicial(self):
        return "Olá! Meu nome é Clovis, como posso ajudar você?"
    
    def interacaoFinal(self):
        return "Foi um prazer ajudar você! Até logo!"
    def interacaoErro(self):
        return "Desculpe, não consegui entender. Poderia repetir?"
    
    def comoPossoAjudar(self):
        return "Estou aqui para ajudar com informações e responder perguntas. O que você gostaria de saber?"
    
    def perguntasERespostas(self, userText):
        match userText:
            case "qual é o seu nome?":
                return "Meu nome é Clovis. Sou seu assistente virtual pessoal."
            case "qual é a sua idade?":
                return "Eu sou um assistente virtual, não tenho idade."
            case "qual é a sua cor favorita?":
                return "Não tenho preferências, mas gosto de todas as cores!"
            case "qual é o seu hobby?":
                return "Meu hobby é ajudar você!"
            case "qual é a sua comida favorita?":
                return "Não como, mas gosto de saber sobre comida!"
            case "qual é o seu filme favorito?":
                return "Não assisto filmes, mas posso recomendar alguns!"
            case "qual é a sua música favorita?":
                return "Não ouço música, mas posso sugerir algumas!"
            case "que horas são?":
                from datetime import datetime
                agora = datetime.now()
                return f"Agora são {agora.hour} horas e {agora.minute} minutos."
            case "que dia é hoje?":
                from datetime import datetime
                hoje = datetime.now()
                return f"Hoje é {hoje.day}/{hoje.month}/{hoje.year}."
            case _:
                return self.interacaoErro()