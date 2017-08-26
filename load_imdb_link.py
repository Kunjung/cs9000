from app import db
from app.models import *
import pandas as pd

df = pd.read_csv('links.csv', sep=',')

count = 0
for d in df.values:
	count = count + 1
	movie_id,imdb_id, tmdb_id = d[0], d[1], d[2]
	movie = Movie.query.filter_by(movie_id = movie_id).first()
	movie.imdb_id = imdb_id
	db.session.add(movie)
	print('Count: ' + str(count))
	
# # p = User('puskar', 'puskar')
# # k = User('kunjung', 'kunjung')

# arrival = Movie('arrival')
# drstrange = Movie('dr strange')
# ghost = Movie('ghost in the shell')
# life = Movie('life')

# # p.rated.append(drstrange)
# # k.rated.append(arrival)
# # k.rated.append(drstrange)

db.session.commit()
print("Done loading data")