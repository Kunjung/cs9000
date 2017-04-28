# Mid-course Happiness Score: 23
from models import *

def calculate_error(rating, predicted_rating):
	error = (rating - predicted_rating) ** 2
	return error / 2

def calculate_error_for_user(user):
	error = 0
	for movie in user.rated:
		user_rating = ratings.select(rating).where(user_id == user_id).where(movie_id == movie.id)
		predicted_rating = (1 - abs(user.comedy - movie.comedy)) + (1 - abs(user.action - movie.comedy)) + \
							(1 - abs(user.romance - movie.romance)) + (1 - abs(user.scifi - movie.scifi))			

		error += calculate_error(rating, predicted_rating)

	return error

def calculate_total_error():
	users = User.query.all()
	total_error = 0
	for user in users:
		total_error += calculate_error_for_user(user)
	return total_error

def calculate_gradients():
	pass