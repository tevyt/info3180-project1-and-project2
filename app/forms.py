from flask.ext.uploads import UploadSet, IMAGES
from flask.ext.wtf import Form
from wtforms.fields import TextField,SelectField,IntegerField
from wtforms.validators import Required 

from flask_wtf.file import FileField, FileAllowed, FileRequired

class UserForm(Form):
    images = UploadSet('images', IMAGES)
    firstname = TextField('First Name' , validators=[Required()])
    lastname = TextField('Last Name' , validators=[Required()])
    age = IntegerField('Age' , validators=[Required()])
    sex = SelectField('Sex' , choices = [('male','Male') , ('female' , 'Female')])
    image = FileField('Profile Picture' , validators = [FileRequired() , FileAllowed(images , 'Images only!')])

            

