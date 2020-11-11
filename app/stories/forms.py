from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, FieldList, FormField
from wtforms.validators import DataRequired
from app.database import Story, StoryContent

class SingleFileForm(FlaskForm):
    text = StringField("Text")


class UploadForm(FlaskForm):
    fields = FieldList(FormField(SingleFileForm), min_entries=3, max_entries=7)
    submit = SubmitField()