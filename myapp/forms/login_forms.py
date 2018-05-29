from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,ValidationError

from ..users import exists_username


class LoginForm(FlaskForm):

	username = StringField(id='username',validators=[DataRequired(message="Username is required")])
	passwd = PasswordField(id='passwd',validators=[DataRequired(message="Password is required")])



class RegisterForm(FlaskForm):
	
	username = StringField(id='username',validators=[DataRequired(message="Username is required")])
	passwd = PasswordField(id='passwd',validators=[DataRequired(message="Password is required")])
	passwd2 = PasswordField(id='passwd2',validators=[DataRequired(message="Password re-typing is required"),
												     EqualTo('passwd',message="Re-typed password does not match")])

	def validate_username(self,username):
		""" a custom validator for username, raising error
		if username already exists in user db """
		
		if exists_username(username.data):
			raise ValidationError("Username already exists") 
			
