from app import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, firstname, lastname, email, address, phonenumber, user_id):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.phonenumber = phonenumber
        self.user_id = user_id

    def __repr__(self):
        return f'<Post | {self.title}>'