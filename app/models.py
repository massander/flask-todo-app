from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(30))
    content = db.Column(db.Text)
    deadline = db.Column(db.String(30))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return f"Todo('{self.subject}', '{self.date_created}')"

    def __init__(self, subject, content, deadline):
        self.subject = subject
        self.content = content
        self.deadline = deadline
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_task(self):
        db.session.delete(self)
        db.session.commit()

    def update_task(self):
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()
