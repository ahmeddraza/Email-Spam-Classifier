# 🔮 SpamAI - Advanced Email Intelligence System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**AI-Powered Email Spam Classification with Word2Vec Semantic Embeddings, Random Forest Prediction, and Real-time Spelling Correction.**

[Features](#-key-features) • [Installation](#-getting-started) • [Usage](#-usage) • [Architecture](#-tech-stack) • [Pipeline](#-performance-metrics)

---

## 🌐 Live Demo
### [👉 Click Here to Access Live Application 👈](https://spam-ai-31fab0a8fd2a.herokuapp.com/predict)
**🎯 Try it now - Fully deployed and ready to use!**

---

## ✨ Key Features

-   **🧠 Semantic Understanding**: Uses a custom-trained **Word2Vec** model to map words into a 100-dimensional vector space, capturing context and meaning rather than just keywords.
-   **🪄 Auto-Correction**: Integrated **TextBlob** engine automatically fixes spelling errors and typos—neutralizing common spam tactics meant to bypass traditional filters.
-   **⚡ Real-Time Analysis**: Instant classification powered by a **Random Forest** ensemble of 100 decision trees.
-   **💎 Premium UI**: A glassmorphism-inspired, dark-themed dashboard designed for a "Single-Page" terminal experience.
-   **🔒 Privacy Centric**: 100% local processing. Your email content is analyzed in-memory and never leaves your machine.

---

## 🛠️ Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 (Modern Glassmorphism), Vanilla JavaScript |
| **Backend** | Flask (Python), NLTK |
| **Intelligence** | Gensim (Word2Vec), Scikit-Learn (Random Forest) |
| **NLP Utilities** | TextBlob (Spelling Correction), Regex |

---

## 📊 Performance Metrics

The model was trained on a comprehensive dataset of **83,000+** emails, achieving state-of-the-art results:

-   **Accuracy**: `98.45%`
-   **Precision**: `0.99` (Non-Spam) / `0.98` (Spam)
-   **Recall**: `0.98` (Non-Spam) / `0.99` (Spam)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/spam-ai.git
cd spam-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize NLTK Data
```python
import nltk
nltk.download('stopwords')
```

### 4. Run the Application
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---
<p align="center">
  Built with ❤️ by <a href="https://github.com/sukku">Ahmed n Raza</a>
</p>
