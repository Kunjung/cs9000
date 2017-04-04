from flask import render_template, redirect, url_for, request, session
from app import app
from .models import Movie

@app.route('/')
def home():
	movies = Movie.query.all()
	return render_template('home.html', movies=movies)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['password'] == '':
			session['user'] = request.form['username']
			return redirect(url_for('secret'))

	return render_template('login.html')

@app.route('/secret')
def secret():
	return render_template('secret.html')
	