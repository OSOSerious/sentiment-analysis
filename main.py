import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download NLTK data files
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Sample data (increased size and diversity)
data = {
    'text': [
        'I love this product!', 'This is the worst experience I have ever had.',
        'It was okay, not great but not terrible either.', 'Absolutely fantastic service!',
        'I am very disappointed with this.', 'Happy with my purchase.',
        'Not what I expected.', 'Great quality and fast shipping.',
        'Terrible, will not buy again.', 'I am satisfied with the results.',
        'The product is decent.', 'I hate this product!',
        'The experience was satisfactory.', 'Amazing! Highly recommended.',
        'Not up to the mark.', 'Pretty good, but could be better.',
        'Completely useless, very unhappy.', 'I will definitely buy this again.',
        'Worst purchase ever.', 'It serves the purpose.',
        'Excellent quality!', 'Very bad product.',
        'Mediocre at best.', 'Outstanding experience!',
        'Not pleased with this.', 'Content with the service.',
        'Awful experience, never again.', 'Best purchase I have made.',
        'Not worth the money.', 'Reasonably good.',
        'This exceeded my expectations!', 'I regret buying this.',
        'Neither good nor bad.', 'Impressive performance!',
        'Disappointed with the quality.', 'Does the job well enough.',
        'Horrible customer service.', 'I\'m thrilled with this purchase!',
        'Below average product.', 'Meets my needs adequately.'
    ],
    'sentiment': [
        'positive', 'negative', 'neutral', 'positive', 'negative',
        'positive', 'neutral', 'positive', 'negative', 'positive',
        'neutral', 'negative', 'neutral', 'positive', 'negative',
        'neutral', 'negative', 'positive', 'negative', 'neutral',
        'positive', 'negative', 'neutral', 'positive', 'negative',
        'neutral', 'negative', 'positive', 'negative', 'neutral',
        'positive', 'negative', 'neutral', 'positive', 'negative',
        'neutral', 'negative', 'positive', 'negative', 'neutral'
    ]
}

df = pd.DataFrame(data)

# Preprocess the text data
stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

df['text'] = df['text'].apply(preprocess_text)

# Split data into training and test sets
X = df['text']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize text data using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Logistic Regression classifier
model = LogisticRegression(random_state=42, max_iter=1000, multi_class='ovr')
model.fit(X_train_vec, y_train)

# Evaluate the model
y_pred = model.predict(X_test_vec)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print(f'Classification Report:\n{classification_report(y_test, y_pred)}')

# Predict sentiment of new text
def predict_sentiment(text):
    text = preprocess_text(text)
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]

def analyze_sentiment():
    text = text_entry.get("1.0", "end-1c")
    sentiment = predict_sentiment(text)
    result = f"Sentiment: {sentiment}"
    result_label.config(text=result)

def save_text():
    text = text_entry.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)

def load_text():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_entry.delete("1.0", tk.END)
            text_entry.insert(tk.END, text)

def clear_text():
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Sentiment Analysis")

text_label = tk.Label(root, text="Enter text to analyze:")
text_label.pack()

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

analyze_button = tk.Button(button_frame, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(side=tk.LEFT)

save_button = tk.Button(button_frame, text="Save Text", command=save_text)
save_button.pack(side=tk.LEFT)

load_button = tk.Button(button_frame, text="Load Text", command=load_text)
load_button.pack(side=tk.LEFT)

clear_button = tk.Button(button_frame, text="Clear Text", command=clear_text)
clear_button.pack(side=tk.LEFT)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
