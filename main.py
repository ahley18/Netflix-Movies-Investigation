# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')

#filter subset
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']
print('\nFilter Movie : \n', str(netflix_subset))

#keep
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

#short movies
short_movies = netflix_movies[netflix_movies['duration'] < 60]
print(short_movies)

#categories
colors = []
for lab, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('green')
    elif row['genre'] == 'Stand-Up':
        colors.append('blue')  # Fixed typo here from 'apend' to 'append'
    else:
        colors.append('black')

#figure
fig = plt.figure()
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()

answer = 'no'