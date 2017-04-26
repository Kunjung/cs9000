# Mid-course Happiness Score: 23
def calculate_error(ratings, predicted_ratings):
	error = 0
	for r, p in zip(ratings, predicted_ratings):
		e = (r - p)**2
		error += e
	return error / 2

def calculate_error_for_user(user_id):
	rated_movies = None
	user = User.query.get(user_id)
	user_rating = None
	for movie in rated_movies:




def calculate_gradients():
	pass