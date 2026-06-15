# 🤖 AI Chatbot with Ollama & Streamlit

A modern AI chatbot built with Python, Ollama, and Streamlit that provides a ChatGPT-like experience in the browser. The application supports real-time streaming responses, conversation persistence, multiple AI model selection, and chat history management.

## 🚀 Features

* 🌐 Browser-based chat interface using Streamlit
* ⚡ Real-time streaming AI responses
* 💾 Persistent chat history saved locally
* 🧠 Context-aware conversations
* 🔄 Multiple model selection
* 🗑 Clear chat functionality
* 🔒 Fully local execution using Ollama
* 🚫 No external API keys required

## 📸 Preview

```text
🤖 AI Chatbot
----------------------------------

Choose Model:
✓ llama3.2

You: Explain React Hooks

AI:
React Hooks are functions that allow...
```

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Models

* Ollama
* Llama 3.2
* Mistral
* Gemma
* DeepSeek-R1

### Libraries

* requests
* streamlit

---

## 📁 Project Structure

```text
ai_chatbot/
│
├── app.py
├── conversation.py
├── llm_client.py
├── chat_history.json
├── requirements.txt
│
└── .streamlit/
    └── config.toml
```

---

## 📂 File Overview

### `app.py`

Responsible for:

* Streamlit user interface
* Chat input handling
* Streaming AI responses
* Model selection
* Clear chat functionality

### `conversation.py`

Handles:

* Conversation history management
* Saving conversations
* Loading previous chats
* Clearing chat history

### `llm_client.py`

Responsible for:

* Communicating with Ollama
* Sending chat requests
* Streaming model responses

### `chat_history.json`

Stores:

* User messages
* Assistant responses
* Conversation context

---

## ⚙️ Prerequisites

Before running the project, install:

* Python 3.10+
* Ollama

---

## 📥 Install Ollama

Download Ollama from:

https://ollama.com

Verify installation:

```bash
ollama --version
```

---

## 📦 Download AI Models

### Llama 3.2

```bash
ollama pull llama3.2
```

### Mistral

```bash
ollama pull mistral
```

### Gemma

```bash
ollama pull gemma
```

### DeepSeek-R1

```bash
ollama pull deepseek-r1
```

Verify installed models:

```bash
ollama list
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd ai_chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

```txt
requests==2.32.5
streamlit==1.48.0
```

---

## ▶️ Running the Application

### Step 1: Start Ollama

```bash
ollama serve
```

### Step 2: Launch Streamlit

```bash
streamlit run app.py
```

The application will automatically open in your browser:

```text
http://localhost:8501
```

---

## 🎯 Supported Models

The chatbot currently supports:

| Model       | Description                          |
| ----------- | ------------------------------------ |
| llama3.2    | General-purpose conversational model |
| mistral     | Fast and lightweight model           |
| gemma       | Google's open-weight model           |
| deepseek-r1 | Strong reasoning model               |

Models can be switched from the sidebar without changing code.

---

## 💬 Conversation Persistence

All conversations are automatically stored in:

```text
chat_history.json
```

Benefits:

* Continue previous conversations
* Preserve context across restarts
* No database required

---

## 🗑 Clear Chat

The sidebar includes a **Clear Chat** button.

When clicked:

* All conversation history is removed
* A fresh session starts
* `chat_history.json` is reset

---

## ⚡ Streaming Responses

Instead of waiting for the entire response to complete, the chatbot streams tokens in real time.

Example:

```text
You: What is Python?

AI:
Python is a high-level programming language...
```

This creates a smoother and more interactive user experience.

---

## 🎨 Optional Dark Theme

Create:

```text
.streamlit/config.toml
```

Add:

```toml
[theme]
base="dark"
```

---

## 🔮 Future Enhancements

Potential improvements:

* User authentication
* PDF document upload
* RAG (Retrieval-Augmented Generation)
* Vector database integration
* Voice input/output
* Chat export feature
* Multi-user support
* FastAPI backend
* Next.js frontend
* Docker deployment

---

## 🐞 Troubleshooting

### Ollama Not Running

Start the server:

```bash
ollama serve
```

### Model Not Found

Download the model:

```bash
ollama pull llama3.2
```

### Port Already In Use

Run Streamlit on another port:

```bash
streamlit run app.py --server.port 8502
```

---

## 📚 Learning Objectives

This project demonstrates:

* Python development
* REST API integration
* Local LLM deployment
* Streamlit UI development
* Conversation management
* Streaming responses
* State management
* AI application development

---

## 📄 License

This project is intended for educational and learning purposes. Feel free to modify and extend it for personal projects, experimentation, or portfolio development.

---

## 👨‍💻 Author

Developed as a local AI chatbot using Ollama and Streamlit to explore conversational AI, local LLM deployment, and modern Python application development.
