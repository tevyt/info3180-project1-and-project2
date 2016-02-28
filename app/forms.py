from flask.ext.wtf import Form
from wtforms.fields import TextField,ImageField,SelectField
from wtforms.validators import Required

class UserForm(Form):
    firstname = TextField('First Name' , validators=[Required()])
    lastname = TextField('Last Name' , validators=[Required()])
    age = TextField('Age' , validators=[Required() , validate_age])
    sex = SelectField('Sex' , choices = ['Male' , 'Female'])

    def validate_age(self ,field):
        try:
            int(field.data)
        except ValueError:
            self.age.errors.append('Age Must be an integer value')
            return False
            

