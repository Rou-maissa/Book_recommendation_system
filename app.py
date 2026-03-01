import pickle
import streamlit as st
import numpy as np

st.header('Book Recommender System Using Machine Learning')

# Load all data
model = pickle.load(open('model.pkl','rb'))
book_names = pickle.load(open('book_names.pkl','rb'))
final_rating = pickle.load(open('final_rating.pkl','rb'))
book_pivot = pickle.load(open('book_pivot.pkl','rb'))

def fetch_poster(suggestion):
    poster_url = []
    for book_id in suggestion.flatten()[1:]:  # skip the first one (itself)
        book_name = book_pivot.index[book_id]
        # Get image URL, provide default if missing
        matches = final_rating[final_rating['title'] == book_name]
        if not matches.empty:
            poster_url.append(matches.iloc[0]['image_url'])
        else:
            poster_url.append("https://via.placeholder.com/150")  # default image
    return poster_url

def recommend_book(book_name, n_recommendations=5):
    if book_name not in book_pivot.index:
        return [], []
    
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1),
        n_neighbors=n_recommendations+1
    )
    
    recommended_books = [book_pivot.index[i] for i in suggestions.flatten()[1:]]
    poster_url = fetch_poster(suggestions)
    
    return recommended_books, poster_url

selected_book = st.selectbox("Type or select a book", book_names)

if st.button('Show Recommendations'):
    recommended_books, poster_url = recommend_book(selected_book)
    
    if recommended_books:
        cols = st.columns(len(recommended_books))
        for i, col in enumerate(cols):
            col.text(recommended_books[i])
            col.image(poster_url[i])
    else:
        st.warning("Book not found in database!")
