from forms import ChatForm
import google.generativeai as palm
from flask import flash, render_template


def main_chat():
    form = ChatForm()
    if form.validate_on_submit():
        user_message = form.message.data
        response = palm.chat(messages=user_message)
        flash(response.last)
    else:
        flash("Invalid Input")
    return render_template("chat.html", form=form)
