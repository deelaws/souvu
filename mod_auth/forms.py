from wtforms import Form, BooleanField, StringField, SelectField, DateTimeField, validators
from wtforms.fields.html5 import DateField, EmailField

class SignupForm(Form):
    user_name = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    password = StringField('Password', [validators.Length(min=10, max=30)])

    def validate_email(self, field):
        print("validating email")
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


    # @@ TODO: add first and last name as well.
    #          maybe not needed when facebook login integration is done.