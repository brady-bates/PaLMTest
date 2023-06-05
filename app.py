import random

from flask import Flask, render_template, flash, request, url_for
import google.generativeai as palm

from forms import ChatForm
from famousNameList import nameList
from chatMethods import main_chat
from config import api_key


name = random.choice(nameList)

app = Flask(__name__)
app.config['SECRET_KEY'] = "TOPSECRETKEY"

palm.configure(api_key=api_key)

@app.route('/', methods=["GET", "POST"])
def chat():
    return main_chat()

@app.route("/guess_who", methods=["GET", "POST"])
def guess_who():
    form = ChatForm()

    if form.validate_on_submit():
        user_message = form.message.data
        response = palm.chat(context=f"You will adopt the personality of the celebrity's name that you are given. Your "
                                     f"goal is to answer all of the players questions truthfully and accurately. For "
                                     f"this game your name will be {name}. DO NOT RESPOND WITH YOUR NAME IF ASKED. If "
                                     f"your name is guess correctly, the game is over.",
                             messages=user_message,
                             temperature=0.2)
        flash(response.last + "\nName: " + name)
    else:
        flash("Invalid Input")
    return render_template("guess_who.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
