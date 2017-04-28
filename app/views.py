from flask import render_template, redirect, url_for, request, session

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Email, Length
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db, login_manager
from .models import *


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=4, max=42)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=42)])
	remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=42)])
	username = StringField('Username', validators=[InputRequired(), Length(min=4, max=42)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=42)])
	recaptcha = RecaptchaField()

class PreferenceForm(FlaskForm):
	comedy = IntegerField('Comedy', validators=[InputRequired()])
	action = IntegerField('Action', validators=[InputRequired()])
	romance = IntegerField('Romance', validators=[InputRequired()])
	scifi = IntegerField('Scifi', validators=[InputRequired()])

class RatingForm(FlaskForm):
	rating = IntegerField('Rating', validators=[InputRequired()])

@app.route('/')
def home():
	movies = Movie.query.limit(20)
	return render_template('home.html', movies=movies)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == form.password.data:
				login_user(user, remember=form.remember.data)
				return redirect(url_for('dashboard'))
		return '<h1> Wrong username or password </h1>'

	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()

	if form.validate_on_submit():
		new_user = User(form.username.data, form.password.data)
		db.session.add(new_user)
		db.session.commit()
		login_user(new_user, remember=True)
		return redirect(url_for('setpreferences'))

	return render_template('signup.html', form=form)

@app.route('/secret')	
def secret():
	return render_template('secret.html')
	
@app.route('/setpreferences', methods=['POST', 'GET'])
@login_required
def setpreferences():
	form = PreferenceForm()
	if form.validate_on_submit():
		user_id = current_user.id
		
		comedy = int(form.comedy.data) / 10
		action = int(form.action.data) / 10
		romance = int(form.romance.data) / 10
		scifi = int(form.scifi.data) / 10
		prefer = Preference(user_id=user_id, comedy=comedy, action=action, romance=romance, scifi=scifi)
		db.session.add(prefer)
		db.session.commit()
		return redirect(url_for('dashboard'))

	return render_template('setpreferences.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
	movies = Movie.query.limit(20)
	return render_template('dashboard.html', username=current_user.username, movies=movies)


@app.route('/rate/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def rate(movie_id):
	user_id = current_user.id
	# get user's rating for this movie
	form = RatingForm()
	if form.validate_on_submit():
		rating = int(form.rating.data)
		# update the ratings table and add the rating
		query = ratings.insert().values(user_id=user_id, movie_id=movie_id, rating=rating)
		db.session.execute(query)
		db.session.commit()
		return redirect(url_for('dashboard'))

	movie = Movie.query.get(movie_id)
	return render_template('rate.html', movie=movie, form=form)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))