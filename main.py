import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Sample data
data = {
    'text': [
        'I love this product!',
        'This is the worst experience I have ever had.',
        'It was okay, not great but not terrible either.',
        'Absolutely fantastic service!',
        'I am very disappointed with this.',
        'Happy with my purchase.',
        'Not what I expected.',
        'Great quality and fast shipping.',
        'Terrible, will not buy again.',
        'I am satisfied with the results.',
        'The product is decent.',
        'I hate this product!',
        'The experience was satisfactory.',
        'Amazing! Highly recommended.',
        'Not up to the mark.',
        'Pretty good, but could be better.',
        'Completely useless, very unhappy.',
        'I will definitely buy this again.',
        'Worst purchase ever.',
        'It serves the purpose.',
    ],
    'sentiment': [
        'positive',
        'negative',
        'neutral',
        'positive',
        'negative',
        'positive',
        'neutral',
        'positive',
        'negative',
        'positive',
        'neutral',
        'negative',
        'neutral',
        'positive',
        'negative',
        'neutral',
        'negative',
        'positive',
        'negative',
        'neutral'
    ]
}

df = pd.DataFrame(data)

# Preprocess the text data
stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    text = text.lower()  # Lowercase text
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize text
    filtered_tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    return ' '.join(filtered_tokens)

df['text'] = df['text'].apply(preprocess_text)

# Split data into training and test sets
X = df['text']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Function to classify text
def classify(text):
    text = preprocess_text(text)
    text_vec = vectorizer.transform([text])
    sentiment = model.predict(text_vec)[0]
    return sentiment

# Test the model
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Test with a new sentence
test_sentence = "This product exceeded my expectations!"
print(f"\nSentiment for '{test_sentence}': {classify(test_sentence)}")