# Projeto Clovis

## Descrição

Clovis é um assistente de voz pessoal em desenvolvimento, projetado para facilitar a interação entre humanos e máquinas por meio de comandos de voz e linguagem natural. Com capacidade de reconhecimento de voz, síntese de fala, memória e reprodução de áudio diretamente no programa, o Clovis oferece uma experiência intuitiva e prática.

Criei ele inspirado nos filmes do Homem de Ferro, pois adoro seu personagem e a criação do J.A.R.V.I.S como seu mordomo pessoal.

---

## Funcionalidades

- **Reconhecimento de Voz**: Interpreta comandos de voz em tempo real.
- **Síntese de Voz**: Responde aos usuários por meio de áudio.
- **Processamento de Linguagem Natural (NLP)**: Compreensão e resposta baseada em intenção.
- **Memória Persistente**: Aprende com as interações passadas.
- **Reprodução de Áudio Direta**: Utiliza o `pygame` para respostas auditivas.
- **Interação Natural**: Se adapta ao estilo de comunicação do usuário.
- **Modular e Extensível**: Estrutura orientada a objetos, organizada em domínios.

---

## Estrutura do Projeto

```

clovis/
├── .venv/                         ← Ambiente virtual
├── clovis/                        ← Código-fonte e Pacote principal da aplicação
│   ├── main.py                    ← Ponto de entrada do assistente
│   ├── config.py                  ← Configuração e variáveis do sistema
│
│   ├── agent/                     ← Responsável por controlar o comportamento geral do assistente
│   │   ├── clovis_agent.py        ← Classe principal do assistente
│   │   └── interface.py           ← Lógica de entrada/saída
│
│   ├── memory/                    ← Tudo relacionado à memória do Clovis — salvar, carregar, lembrar, esquecer.
│   │   ├── memory_manager.py
│   │   └── storage.py
│
│   ├── nlp/                       ← Processamento de linguagem natural — como entender e responder
│   │   ├── tokenizer.py
│   │   ├── intent_classifier.py
│   │   └── response_generator.py
│
│   ├── tools/                     ← Ferramentas acessíveis pelo Clovis — calculadora, navegador, dicionário, alarmes, etc.
│   │   ├── calculator.py
│   │   └── browser.py
│
│   └── utils/                     ← Funções auxiliares e comuns a vários módulos
│       └── helpers.py
│
├── tests/                         ← Testes automatizados
│   ├── agent/
│   ├── nlp/
│   ├── memory/
│   └── tools/
│
├── notebooks/                     ← Área para testes, análises e protótipos rápidos com Jupyter.
│   └── experimento_nlp.ipynb
│
├── data/                          ← Dados persistentes (ex: memória JSON)
│   └── memory.json
│
├── .env                           ← Variáveis de ambiente (API Keys, etc)
├── .gitignore
├── requirements.txt
└── README.md

````

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Bibliotecas Principais**:
  - `SpeechRecognition` – Reconhecimento de voz
  - `gTTS` – Síntese de voz
  - `pygame` – Reprodução de áudio
- **Para NLP**:
  - `nltk`, `transformers` (opcional para uso de LLMs via API)
- **Para persistência e testes**:
  - `json`, `unittest`, `pytest`
- **Ambiente Virtual**:
  - `venv` (nativo do Python)

---

## Como Começar

### 1. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
````

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o assistente

```bash
python clovis/main.py
```

### 4. Rodar os notebooks

```bash
jupyter notebook
```

---

## Próximas Etapas

* ✅ Captura de comando de voz
* ✅ Geração de voz com resposta falada
* ✅ Execução de áudio diretamente no programa com `pygame`
* 🔄 Integração com memória persistente (aprendizado contínuo)
* 🔬 Treinamento de modelo leve para NLP
* 🌐 Integração futura com API de LLM (ex: OpenRouter, Gemini, Mistral)

---

## Licença

Este projeto é de código aberto. Sinta-se à vontade para contribuir e melhorá-lo!

📩 Qualquer ideia, feedback ou sugestão: entre em contato comigo pelas redes sociais no meu perfil!

---

## Começar por

1. main.py + ClovisAgent (fluxo básico de I/O)
2. interface.py com input() e print() ou voz (SpeechRecognition + gTTS + pygame)
3. IntentClassifier simples com if/elif ou scikit-learn
4. ResponseGenerator com respostas básicas
5. MemoryManager que salva num JSON
6. Prototipar tudo isso no experimento_nlp.ipynb
7. Só depois pensar em integrar uma LLM com API
