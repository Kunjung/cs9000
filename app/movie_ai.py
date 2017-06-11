# Mid-course Happiness Score: 23
from .models import *
LEARNING_RATE = 0.005

def calculate_error(real_rating, predicted_rating):
	error = (real_rating - predicted_rating) ** 2
	return error / 2

def calculate_predicted_rating(user, movie):
	preference = Preference.query.filter_by(user_id=user.id).first()
	comedy, action, romance, scifi = preference.comedy, preference.action, preference.romance, preference.scifi

	if movie.comedy == None or movie.action == None or movie.romance == None or movie.scifi == None:
		return 0.0

	else:
		#predicted_rating = (1 - abs(comedy - movie.comedy)) + (1 - abs(action - movie.action)) + \
		#					(1 - abs(romance - movie.romance)) + (1 - abs(scifi - movie.scifi))
		predicted_rating = comedy * movie.comedy + \
						   action * movie.action + \
						   romance * movie.romance + \
						   scifi * movie.scifi

		predicted_rating = predicted_rating / 4.0 * 5.0
		return predicted_rating

def calculate_real_rating(user_id, movie_id):
	query = ratings.select('rating').where(ratings.c.user_id==user_id).where(ratings.c.movie_id==movie_id)
	values = db.session.execute(query).first()
	real_rating = values[2]
	return real_rating

def calculate_error_for_user(user):
	error = 0
	for movie in user.rated:
		real_rating = calculate_real_rating(user.id, movie.id)
		predicted_rating = calculate_predicted_rating(user, movie)
		error += calculate_error(real_rating, predicted_rating)
	return error

def calculate_total_error():
	users = User.query.all()
	total_error = 0
	for user in users:
		total_error += calculate_error_for_user(user)
	return total_error

def calculate_gradient_part(predicted_rating, real_rating, movie_feature):
	gradient = (predicted_rating - real_rating) * movie_feature
	gradient = gradient * LEARNING_RATE
	return gradient

def update_user_preferences(user):
	preference = Preference.query.filter_by(user_id=user.id).first()
	comedy, action, romance, scifi = preference.comedy, preference.action, preference.romance, preference.scifi

	for movie in user.rated:
		predicted_rating = calculate_predicted_rating(user, movie)
		real_rating = calculate_real_rating(user.id, movie.id)
		
		for _ in range(50):
			# 1 - comedy
			comedy = comedy - calculate_gradient_part(predicted_rating, real_rating, movie.comedy)
			comedy = limit(comedy)
			# 2 - action
			action = action - calculate_gradient_part(predicted_rating, real_rating, movie.action)
			action = limit(action)
			# 3 - romance
			romance = romance - calculate_gradient_part(predicted_rating, real_rating, movie.romance)
			romance = limit(romance)
			# 4 - scifi
			scifi = scifi - calculate_gradient_part(predicted_rating, real_rating, movie.scifi)
			scifi = limit(scifi)

			# Re-Calculate the predicted rating
			predicted_rating = comedy * movie.comedy + \
						   action * movie.action + \
						   romance * movie.romance + \
						   scifi * movie.scifi

			predicted_rating = predicted_rating / 4.0 * 5.0
	preference.comedy, preference.action, preference.romance, preference.scifi =  comedy, action, romance, scifi
	db.session.commit()
	
def limit(val):
	if val < -1.0:
		return -1.0
	elif val > 1.0:
		return 1.0
	else:
		return val


			