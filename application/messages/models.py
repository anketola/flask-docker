from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(144), nullable=False)

    def __init__(self, message):
        self.message = message