# Task 4 - Recommendation System
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset
data = {
    "Title": ["The Matrix", "John Wick", "Inception", "Interstellar", "Tenet"],
    "Genre": ["Sci-Fi", "Action", "Sci-Fi Thriller", "Sci-Fi Drama", "Time Travel Sci-Fi"]
}
df = pd.DataFrame(data)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["Genre"])

# Cosine Similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend(title):
    idx = df[df["Title"] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]
    return df["Title"].iloc[movie_indices]

print(recommend("Inception"))
