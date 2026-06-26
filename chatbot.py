import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("faq.csv")

questions = data["Question"]

answers = data["Answer"]

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)

def chatbot_response(user_question):

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(user_vector,question_vectors)

    score = similarity.max()

    index = similarity.argmax()

    if score < 0.20:
        return "😕 Sorry! I couldn't find a relevant answer."

    return answers.iloc[index]
