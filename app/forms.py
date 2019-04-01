from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(),Email()])
	about_me = TextAreaField('About me',validators=[Length(min=0,max=140)])
	password = PasswordField('Password',validators=[DataRequired()])
	password2 = PasswordField('Repeat password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Use different username(Already in use)')

	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Use different email address(Already registered)')


class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	password = PasswordField('password',validators=[DataRequired()])
	remember_me = BooleanField('remember_me')
	submit = SubmitField('Sign In')

class EditProfileForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	about_me = TextAreaField('About me',validators=[Length(min=0,max=140)])
	submit = SubmitField('Submit')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Use different username')
