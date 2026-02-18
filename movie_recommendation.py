import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
# u.data contains the ratings (user_id, movie_id, rating)
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id','movie_id','rating','timestamp'])

# u.item contains movie titles (we only need columns 0 and 1)
movies = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', usecols=[0,1], names=['movie_id','title'])

# Merge them together so we have titles and ratings in one place
data = pd.merge(ratings, movies, on='movie_id')

# 2. Create a User-Movie Matrix
# This creates a giant grid where rows are Users and columns are Movie Titles
user_movie_matrix = data.pivot_table(index='user_id', columns='title', values='rating')

# 3. Interactive Search
all_titles = user_movie_matrix.columns

search_term = input("Enter a movie name (e.g., 'Toy Story'): ")

# Find the closest match in our list of movies
matches = [title for title in all_titles if search_term.lower() in title.lower()]

if len(matches) == 0:
    print("No movie found with that name. Check your spelling!")
else:
    # Pick the first match found
    movie_name = matches[0]
    print(f"Finding movies similar to: {movie_name}...")
    
    # ... rest of your code stays the same ...
    movie_ratings = user_movie_matrix[movie_name]

# 4. Compute Similarity (Correlation)
# We compare the ratings of Star Wars against every other movie in the matrix
similar_movies = user_movie_matrix.corrwith(movie_ratings)

# Put results into a DataFrame and clean up
corr_movies = pd.DataFrame(similar_movies, columns=['correlation'])
corr_movies.dropna(inplace=True)

# Add the number of ratings so we can filter out unpopular movies (noise)
movie_stats = data.groupby('title')['rating'].count()
corr_movies = corr_movies.join(movie_stats)
corr_movies.columns = ['correlation', 'rating_count']

# 5. Filter and Sort
# We only want movies with more than 100 ratings to ensure quality
recommendations = corr_movies[corr_movies['rating_count'] > 100].sort_values('correlation', ascending=False)

# Skip the first row (because Star Wars is 100% correlated with Star Wars)
top_10 = recommendations.iloc[1:11]

# 6. Show Results
print("\nTop 10 recommendations:")
print(top_10)

# 7. Create a Plot
plt.figure(figsize=(10,6))
plt.barh(top_10.index, top_10['correlation'], color='skyblue')
plt.xlabel('Correlation Score (Similarity)')
plt.ylabel('Movie Title')
plt.title(f'Top 10 Recommendations for "{movie_name}"')
plt.gca().invert_yaxis() # Put the highest correlation at the top
plt.show()
top_10.to_csv('recommendations.csv')
print("Results saved to recommendations.csv!")