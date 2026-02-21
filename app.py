from flask import Flask, render_template, request
import pickle
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from textblob import TextBlob

# Download necessary NLTK data
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

app = Flask(__name__)

# Load the models
model = pickle.load(open('model.pkl', 'rb'))
word2vec_model = Word2Vec.load('word2vec_model.bin')

def text_transform(text):
    # Spelling Correction
    text = str(TextBlob(text).correct())
    
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    text = text.split()
    text = [word for word in text if word not in stop_words]
    return text

def get_doc_vector(tokens, model, vector_size=100):
    vectors = [model.wv[w] for w in tokens if w in model.wv]
    if len(vectors) == 0:
        return np.zeros(vector_size)
    return np.mean(vectors, axis=0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_content = request.form.get('content')
        if not email_content:
            return render_template('index.html', prediction_text="Please enter some text.")
        
        # Preprocess and Vectorize
        transformed_text = text_transform(email_content)
        vector = get_doc_vector(transformed_text, word2vec_model).reshape(1, -1)
        
        # Predict
        prediction = model.predict(vector)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        
        return render_template('index.html', 
                               prediction_text=f'This email is: {result}',
                               original_text=email_content)

if __name__ == "__main__":
    app.run(debug=True)
