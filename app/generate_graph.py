## Machine Learning 

import matplotlib.pyplot as plt


def get_avg_predicted_rating(num_of_movies_to_use):
	user = User.query.get(1)
	movies = Movie.query.limit(num_of_movies_to_use)
	avg_predicted_rating = 0
	count = 0
	for movie in movies:
		count = count + 1
		predicted_rating = calculate_predicted_rating(user, movie)
		avg_predicted_rating += predicted_rating

	avg_predicted_rating = avg_predicted_rating / count
	return avg_predicted_rating

def graph():
	movie_numbers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
	avg_predicted_ratings = [2.175568022126464, 2.5047060022568033, 2.682246390040447, 2.7262357936917128, 2.9135448965324144, 2.9135448965324144, 2.9135448965324144, 2.9135448965324144, 2.9135448965324144, 2.9135448965324144]
	plt.plot(movie_numbers, avg_predicted_ratings, 'g^')
	plt.xlabel('number of movies used')
	plt.ylabel('avg ratings taken from top 10 recommendations')
	plt.show()
	return "Done"

graph()