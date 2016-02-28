from flask.ext.wtf import Form
from wtforms.fields import TextField,SelectField,IntegerField
from wtforms.validators import Required 

from flask_wtf.file import FileField, FileAllowed, FileRequired


def age_validator(form , field):
    try:
        age = int(field.data)
        if not age in range(5,130):
            field.errors.append('Age is outside valid range')
            return False
        return True
    except TypeError:
        field.errors.append('Age must be an integer')
        return False


class UserForm(Form):
    firstname = TextField('First Name' , validators=[Required()])
    lastname = TextField('Last Name' , validators=[Required()])
    age = IntegerField('Age' , validators=[age_validator,Required()])
    sex = SelectField('Sex' , choices = [('male','Male') , ('female' , 'Female')])
    image = FileField('Profile Picture' , validators=[Required()])


            

