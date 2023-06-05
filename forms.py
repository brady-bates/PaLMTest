from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class ChatForm(FlaskForm):
    message = StringField(label = "Message",
                          validators  = [InputRequired()],
                          render_kw={"placeholder": "Your message here"})

    submit = SubmitField(label = "Submit")
