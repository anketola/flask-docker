from flask import render_template
from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm

@app.route("/")
def index():
    return render_template("index.html", messages = Message.query.all(), form = MessageForm())
