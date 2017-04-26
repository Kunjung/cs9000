from app import db
from flask_login import UserMixin

ratings = db.Table('ratings',
		db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
		db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
		db.Column('rating', db.Integer)
	)

class Preference(db.Model):
	__tablename__ = 'preferences'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	comedy = db.Column(db.Float)
	action = db.Column(db.Float)
	romance = db.Column(db.Float)
	scifi = db.Column(db.Float) 

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(42), unique=True)
	password = db.Column(db.String(42))
	rated = db.relationship('Movie', secondary=ratings, backref='raters', lazy='dynamic')
	

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username

class Movie(db.Model):
	__tablename__ = 'movies'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(42), unique=True)
	comedy = db.Column(db.Float)
	action = db.Column(db.Float)
	romance = db.Column(db.Float)
	scifi = db.Column(db.Float) 


	def __init__(self, name, comedy, action, romance, scifi):
		self.name = name
		self.comedy = comedy
		self.action = action
		self.romance = romance
		self.scifi = scifi

	def __repr__(self):
		return '<Movie %r>' % self.name

# use this to update or get data from ratings table
######################
# query = ratings.update().where(
#     ratings.c.user_id == user1.id
# ).where(
#     ratings.c.movie_id == movie1.id
# ).values(rating=new_rating)
#
# db.session.execute(query)
# val = db.session.execute(query).first()[2]