from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    occupation = db.Column(db.String(100), nullable=True)
    contact_details = db.Column(db.String(100), nullable=True)
    home_address = db.Column(db.String(200), nullable=True)
    postal_code = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(100), nullable=False)
    interests = db.Column(db.String(200), nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True)  # Relationship to the Post table

    def __repr__(self):
        return '<User %r>' % self.email

class Post(db.Model):
    postId = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)  # Foreign key relationship to User table
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    images = db.Column(db.BLOB, nullable=True)  # Assuming storing images as BLOB data
    videos = db.Column(db.BLOB, nullable=True)  # Assuming storing videos as BLOB data
    likes = db.Column(db.Integer, default=0)
    comments = db.Column(db.Integer, default=0)
    shares = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Post %r>' % self.title

# Create the tables
with app.app_context():
    db.create_all()
