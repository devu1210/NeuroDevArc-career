# backend/ml_matcher.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_careers(user_skills, careers_data):
    # Convert career skills to strings
    career_names = list(careers_data.keys())
    skills_list = [" ".join(v["skills"]) for v in careers_data.values()]
    
    # Add user skills
    skills_list.append(" ".join(user_skills))
    
    # Vectorize & compute similarity
    vectorizer = CountVectorizer().fit_transform(skills_list)
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity(vectors)
    
    sim_scores = cosine_matrix[-1][:-1]  # last row is user
    top_idx = sim_scores.argsort()[::-1]  # descending order
    
    recommendations = [career_names[i] for i in top_idx]
    scores = [sim_scores[i] for i in top_idx]
    
    return recommendations[:3], scores[:3]  # top 3 careers
