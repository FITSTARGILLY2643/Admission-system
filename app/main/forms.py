from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Programme', validators=[DataRequired()])
    institution = StringField('Institution', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ApplicationForm(FlaskForm):
    institution = SelectField('Institution',choices=[('Moringa School','Moringa School'),('Zetech University','Zetech University'),('Moi University','Moi University')],validators=[Required()])
    programme = SelectField('Programme',choices=[('Data Science','Data Science'),('Artificial Intelligence','Artificial Intelligence'),('Software Development','Software Development')],validators=[Required()])
    intake = SelectField('Intake',choices=[('January Intake','January Intake'),('August Intake','August Intake')],validators=[Required()])
    submit = SubmitField('Submit')