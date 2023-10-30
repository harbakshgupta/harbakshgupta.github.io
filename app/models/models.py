from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    """Table for Admin"""
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __repr__(self) -> str:
        return f"{self.username}"

class blogPosts(db.Model):
    """Table for Blog Posts"""
    __tablename__ = "blogPosts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.String(100), nullable=True)
    visible = db.Column(db.Boolean, nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    short_desc = db.Column(db.String(1000), nullable=False)

    def __init__(self, title, image, content, date, visible, slug, short_desc):
        self.title = title
        self.image = image
        self.content = content
        self.date = date
        self.visible = visible
        self.slug = slug
        self.short_desc = short_desc

    def __repr__(self) -> str:
        return f"{self.title}"