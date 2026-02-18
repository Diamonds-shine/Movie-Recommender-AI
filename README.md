<img width="1710" height="969" alt="Screenshot 2026-02-19 at 1 17 07 AM" src="https://github.com/user-attachments/assets/e6097120-2907-4976-9691-0812bf9cb2b7" />
 🎬 Movie Recommender AI

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
