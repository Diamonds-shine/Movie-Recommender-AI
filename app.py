from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# --- LOAD DATA (Runs once when server starts) ---
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id','movie_id','rating','timestamp'])
movies = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', usecols=[0,1], names=['movie_id','title'])
data = pd.merge(ratings, movies, on='movie_id')
user_movie_matrix = data.pivot_table(index='user_id', columns='title', values='rating')

def get_recommendations(movie_name):
    # Find closest title match
    all_titles = user_movie_matrix.columns
    matches = [t for t in all_titles if movie_name.lower() in t.lower()]
    
    if not matches:
        return None, "No movie found with that name!"
    
    target_movie = matches[0]
    movie_ratings = user_movie_matrix[target_movie]
    similar_movies = user_movie_matrix.corrwith(movie_ratings)
    
    corr_df = pd.DataFrame(similar_movies, columns=['correlation'])
    corr_df.dropna(inplace=True)
    
    movie_stats = data.groupby('title')['rating'].count()
    corr_df = corr_df.join(movie_stats)
    corr_df.columns = ['correlation', 'rating_count']
    
    # Filter and get top 5 results
    res = corr_df[corr_df['rating_count'] > 100].sort_values('correlation', ascending=False)
    return res.iloc[1:6].index.tolist(), target_movie

# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    matched_title = ""
    
    if request.method == 'POST':
        user_input = request.form.get('movie_name')
        recommendations, matched_title = get_recommendations(user_input)
        
    return render_template('index.html', recs=recommendations, movie=matched_title)

if __name__ == '__main__':
    app.run(debug=True)