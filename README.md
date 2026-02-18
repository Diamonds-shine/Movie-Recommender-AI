# 🎬 Movie Recommender AI

A full-stack recommendation engine that suggests movies based on user rating patterns. This project uses **Item-Based Collaborative Filtering** to find mathematical similarities between films.

## 🚀 Features
* **Fuzzy Search:** Handles partial movie titles (e.g., typing "pulp" finds "Pulp Fiction").
* **AI Logic:** Uses Pearson Correlation to find movies with similar rating "fingerprints."
* **Web Interface:** Built with Flask for an interactive, Netflix-style user experience.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Libraries:** Pandas, NumPy
* **Web Framework:** Flask
* **Dataset:** MovieLens 100k

## 📊 How it Works
The system creates a user-item matrix where rows are users and columns are movies. When you search for a movie, the AI calculates the correlation between that movie's ratings and all other movies in the dataset. Movies with the highest correlation scores are suggested.
