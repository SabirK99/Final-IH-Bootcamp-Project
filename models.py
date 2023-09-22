from datetime import datetime
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    publish_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Text content and audio file will be added later, but you can set placeholders
    # text_content = db.Column(db.Text, nullable=True)
    # audio_file_path = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.publish_date}')"
