from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, FloatField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class New_Property(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    num_bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    num_baths = FloatField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    prop_type = SelectField('Property Type', choices=[("Apartment", "Apartment"), ("House", "House")])
    Desc = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
