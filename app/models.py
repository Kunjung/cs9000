from app import db

class Movie(db.Model):
	__tablename__ = 'movie'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, unique=True)
	genre = db.Column(db.Text)
	# box_office = db.Column(db.Integer)
	# rating = db.Column(db.Integer)


	def __init__(self, name, genre):
		self.name = name
		self.genre = genre


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)