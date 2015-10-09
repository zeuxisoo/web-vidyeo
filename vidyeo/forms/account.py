from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp
from .base import BaseForm
from ..models import Account

class SignupForm(BaseForm):
    username = TextField(
        'Username',
        validators=[
            DataRequired(message='Please enter username'),
            Length(min=3, max=20),
            Regexp(r'^[a-z0-9A-Z]+$', message='Username must english characters only.')
        ]
    )

    email = TextField(
        'Email',
        validators=[
            DataRequired(message='Please enter email'),
            Email(message='Invalid email format')
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Please enter password'),
            Length(message="Password must more than 8 length", min=8),
        ]
    )

    def validate_username(self, field):
        if Account.query.filter_by(username=field.data.lower()).count():
            raise ValueError('This username has been registered.')

    def validate_email(self, field):
        if Account.query.filter_by(email=field.data.lower()).count():
            raise ValueError('This email has been registered.')

    def save(self):
        data = self.data
        data.pop('confirm_password', None)

        user = Account(**data)
        user.save()

        return user
