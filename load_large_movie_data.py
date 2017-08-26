from app import db
from app.models import *
import pandas as pd
import random

df = pd.read_csv('movies.csv', sep=',')

db.drop_all()
db.create_all()

COUNTER = 1

def normalize(val):
	return val * 2 - 1

def estimated_value(val):
	r = random.random() # from 0 to 0.5
	b = (val + r)/2  # returns value from (val, val+r)
	return normalize(b)

for d in df.values:
	COUNTER = COUNTER + 1
	movieId, title, genres = d[0], d[1], d[2]
	list_of_genres = genres.split('|')
	comedy, action, romance, scifi = estimated_value(0), estimated_value(0), estimated_value(0), estimated_value(0)
	for g in list_of_genres:
		if g == 'Comedy':
			comedy = estimated_value(1)
		elif g == 'Action':
			action = estimated_value(1)
		elif g == 'Romance':
			romance = estimated_value(1)
		elif g == 'Scifi':
			scifi = estimated_value(1)
	
	print('Count: ' + str(COUNTER))
	movie = Movie(movieId, title, comedy, action, romance, scifi)
	db.session.add(movie)
	
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