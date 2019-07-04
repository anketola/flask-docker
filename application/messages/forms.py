from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MessageForm(FlaskForm):
    message = StringField("Your message", [validators.Length(min=1, max=144)])
 
    class Meta:
        csrf = False