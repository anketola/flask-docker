from application import app, db
from flask import redirect, render_template, request, url_for
from application.messages.models import Message
from application.messages.forms import MessageForm

@app.route("/messages/new", methods=["POST"])
def messages_create():
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("index.html", messages = Message.query.all(), form = form)

    m = Message(form.message.data)
  
    db.session().add(m)
    db.session().commit()
    
    return redirect(url_for("index"))