# 🛡️ SpamAI: Advanced Email Intelligence

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**SpamAI** is a high-performance, semantic email classifier that combines **Word2Vec** embeddings with a **Random Forest Ensemble** to identify spam with industrial-grade precision. Featuring a modern, "zero-scroll" interface and real-time spelling correction, it brings advanced NLP directly to your local environment.

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
pip install flask gensim nltk textblob scikit-learn numpy
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

## 🖥️ Preview

> **SpamAI Interface**
> The dashboard features a responsive two-column grid. Paste your content on the left, and view semantic insights and classification results on the right—all without scrolling.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---
<p align="center">
  Built with ❤️ by <a href="https://github.com/sukku">Ahmed n Raza</a>
</p>
