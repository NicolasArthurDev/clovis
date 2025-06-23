# Projeto Clovis

Clovis é um assistente de voz pessoal em desenvolvimento, projetado para facilitar a interação entre humanos e máquinas por meio de comandos de voz e linguagem natural. Com capacidade de reconhecimento de voz, síntese de fala, memória e reprodução de áudio diretamente no programa, o Clovis oferece uma experiência intuitiva e prática.

Criei ele inspirado nos filmes do Homem de Ferro, pois adoro seu personagem e a criação do J.A.R.V.I.S como seu mordomo pessoal.

## Como rodar o Clovis

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/clovis.git
cd clovis
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Instale o pacote Clovis em modo desenvolvimento

```bash
pip install -e .
```

### 5. (Opcional) Configure variáveis de ambiente

Se necessário, crie um arquivo `.env` com suas configurações (ex: chaves de API).

### 6. Baixe e inicie o modelo Mistral localmente

O Clovis utiliza o **Mistral LLM** rodando via [Ollama](https://ollama.com/). Instale o Ollama e baixe o modelo Mistral:

```bash
# Instale o Ollama conforme a documentação oficial
ollama pull mistral
ollama run mistral
```

> **Importante:** O modelo precisa estar rodando em `localhost:11434` para o chat funcionar.

### 7. Inicie a interface web (chatbot) com Streamlit

Sempre execute a partir da raiz do projeto:

```bash
streamlit run app/streamlit_app.py
```

Acesse pelo navegador em [http://localhost:8501](http://localhost:8501).

---

## Dicas

- Para personalizar o comportamento do Clovis, edite o `system_prompt` em `clovis/nlp/response_generator.py`.
- Para adicionar novas funcionalidades, crie módulos em `clovis/tools/` ou `clovis/agent/`.
- Para testes, utilize a pasta `tests/`.

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
├── app/                           ← Interface web com Streamlit
│   └── streamlit_app.py           ← Página do chatbot Clovis
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
├── setup.py                       ← Instalação do pacote em modo desenvolvimento
└── README.md
```

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Bibliotecas Principais**:
  - `SpeechRecognition` – Reconhecimento de voz
  - `gTTS` – Síntese de voz
  - `pygame` – Reprodução de áudio
  - `streamlit` – Interface web
- **Para NLP**:
  - `nltk`, `transformers` (opcional para uso de LLMs via API)
- **Para persistência e testes**:
  - `json`, `unittest`, `pytest`
- **Ambiente Virtual**:
  - `venv` (nativo do Python)

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

## Etapas para Construção de um Modelo de NLP com Python

Criar um modelo de NLP envolve um pipeline de etapas fundamentais:

1. Coleta de dados textuais
2. Limpeza e pré-processamento dos textos
3. Tokenização e vetorizacão
4. Treinamento de modelo
5. Avaliação de desempenho
6. Implantação e inferência
