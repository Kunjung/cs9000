from app import db
from app.models import *
import pandas as pd

df = pd.read_csv('movie_data.csv', sep=',')

db.drop_all()
db.create_all()

for d in df.values:
	name, comedy, action, romance, scifi = d[0], d[1], d[2], d[3], d[4]
	movie = Movie(name, comedy, action, romance, scifi)
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