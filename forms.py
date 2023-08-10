from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired,EqualTo


class RegisterForm(FlaskForm):
    Name = StringField(label='Name',validators=[Length(min=2,max=30),DataRequired()])
    password1 = PasswordField(label='Passoword',validators=[Length(min=6,max=30),DataRequired()])
    password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Submit!')

class LoginForm(FlaskForm):
    Name = StringField(label='Name',validators=[DataRequired()])
    Password = PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label='Log in!')