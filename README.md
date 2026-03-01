# 📚 Book Recommender System

A **Book Recommendation System** built using **Machine Learning (K-Nearest Neighbors)** and deployed with **Streamlit**.  
This system suggests similar books based on a selected book from the dataset and displays their covers.

---

## 🛠 Technologies Used
- **Python**  
- **Streamlit** – For interactive web app  
- **scikit-learn** – KNN model for recommendations  
- **NumPy & Pandas** – Data processing  
- **Pickle** – Model & dataset serialization  

---

## ⚡ Features
- Real-time book recommendations using **KNN** (`n_neighbors=6`)  
- Displays book **title and cover image**  
- Interactive **Streamlit interface**  
- Handles missing book covers with default placeholder images  

---

## 🧠 How It Works

-Load the pre-trained KNN model (model.pkl) and datasets (book_names.pkl, final_rating.pkl, book_pivot.pkl).

-User selects a book from the dropdown.

-The model finds nearest neighbors (similar books) in the feature space.

-Recommendations are displayed along with their cover images.

-The KNN model uses n_neighbors=6, so it finds the 5 most similar books plus the selected one.


---

## 💻 How to Run
1. Clone the repository:
```bash
git clone https://github.com/Rou-maissa/Book_recommendation_system.git
