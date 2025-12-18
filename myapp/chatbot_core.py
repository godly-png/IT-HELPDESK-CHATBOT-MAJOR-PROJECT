import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# -------------------------------
# Download required NLTK data
# -------------------------------
nltk.download('punkt')
nltk.download('stopwords')

# -------------------------------
# Load dataset
# -------------------------------
data = pd.read_csv('aa_dataset-tickets-multi-lang-5-2-50-version.csv')

# Ensure no NaN values
data = data.dropna(subset=['body', 'answer'])

questions = data['body'].astype(str).tolist()
answers = data['answer'].astype(str).tolist()

# -------------------------------
# Text cleaning function
# -------------------------------
def clean_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = nltk.word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

cleaned_questions = [clean_text(q) for q in questions]

# -------------------------------
# TF-IDF vectorization
# -------------------------------
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(cleaned_questions)

# -------------------------------
# Chatbot reply function
# -------------------------------
def reply(user_input):
    cleaned_input = clean_text(user_input)
    user_vec = vectorizer.transform([cleaned_input])
    similarity = cosine_similarity(user_vec, tfidf)
    index = similarity.argmax()
    score = similarity[0][index]

    # DEBUG: check which question is matched
    print("DEBUG: matched question:", questions[index])
    print("DEBUG: similarity score:", score)

    # Threshold for unknown questions
    if score < 0.1:  # lowered threshold for short questions
        return "Sorry, I didn't know the answer. Can you ask something different?"
    
    return answers[index]

# -------------------------------
# Command-line chat loop
# -------------------------------
if __name__ == "__main__":
    print("Chatbot is running! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if user.lower() == 'bye':
            print("Bot: Bye!")
            break
        print("Bot:", reply(user))
