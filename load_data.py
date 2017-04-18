from app import db
from app.models import *

db.drop_all()
db.create_all()

p = User('puskar', 'p')
k = User('kunjung', 'k')

arrival = Movie('arrival')
drstrange = Movie('dr strange')
ghost = Movie('ghost in the shell')
life = Movie('life')

p.rated.append(drstrange)
k.rated.append(arrival)
k.rated.append(drstrange)

db.session.add_all([p, k, arrival, drstrange, ghost, life])
db.session.commit()