from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(16), nullable=False)

    idea = db.relationship("Idea", backref='idea', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    activity = db.Column(db.String(100), nullable=False)
    accessibility = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Idea {self.first_name} {self.last_name}>"
