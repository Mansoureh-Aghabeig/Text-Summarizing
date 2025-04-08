# 📝 Text Summarization using Transformers

This project demonstrates how to perform automatic text summarization using two different transformer-based approaches. The goal is to condense long-form text into meaningful summaries, using state-of-the-art NLP models.

---

## 💡 Project Overview

The notebook showcases:

1. **Custom Transformer Model** – more customizable and flexible.
2. **Hugging Face Transformers Pipeline** – fast and easy-to-use summarization method.

---

## 🛠️ Technologies Used

- **Python**
- **Hugging Face Transformers**
- **PyTorch**
- **NLTK**
- **Scikit-learn**
- **Google Colab / Jupyter Notebook**

Optional (for deployment):

- **Docker**
- **FastAPI**
- **AWS EC2 / ECR**
- **GitHub Actions (for CI/CD)**

---

## 🚀 How It Works

### 🔧 Technique 1: Manual Transformer Summarization
- Load model/tokenizer manually (e.g., `facebook/bart-large-cnn`)
- Tokenize input and generate summaries
- Decode generated token IDs into readable text

### ⚡ Technique 2: Hugging Face Summarization Pipeline
- Simplified interface with `pipeline("summarization")`
- Instantly generates summaries with minimal setup

---

## 📦 Dockerization & Cloud Deployment

You can deploy this summarization model as a **REST API** using Flask/FastAPI, containerize it with **Docker**, and then push to the cloud:

### ✅ Docker Setup
1. Create a `Dockerfile` to define your image.
2. Expose a port and serve the model via Flask/FastAPI.
3. Build and run locally:
   ```bash
   docker build -t text-summarizer .
   docker run -p 8000:8000 text-summarizer
