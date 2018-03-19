import flask
from flask_sqlalchemy import SQLAlchemy
from services.post.domain.post import Post


app = flask.current_app
db = SQLAlchemy(app)


class PostDB(db.Model):
    id = db.column(db.Integer, primary_key=True)
    user_id = db.column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.column(db.Text)
    date = db.column(db.DateTime, nullable=False)


class PostRepository:
    def __init__(self, app):
        self.db = SQLAlchemy(app)

    def create(self, post):
        self.db.session.add(PostDB(user_id=post.user_id, text=post.text, date=post.date))
        self.db.session.commit()

    def read(self, post_id):
        if self.exists(post_id):
            post = PostDB.query.filter_by(id=post_id).first()
            return Post(post_id=post.id, user_id=post.user_id, date=post.date, text=post.text)
        else:
            return None

    def read_all(self):
        posts = []
        for post in PostDB.query.all():
            posts.append(Post(post_id=post.id, user_id=post.user_id, date=post.date, text=post.text))
        return posts

    def update(self, post):
        if self.exists(post.id):
            post_to_update = PostDB.query.filter_by(id=post.id).first()
            post_to_update.user_id = post.user_id
            post_to_update.text = post.text
            post_to_update.date = post.date
            self.db.session.commit()

    def delete(self, post):
        if self.exists(post.id):
            post_to_delete = PostDB.query.get(post.id)
            self.db.session.delete(post_to_delete)
            self.db.session.commit()

    def exists(self, post_id):
        return self.db.session.query(PostDB.query.filter(PostDB.id == post_id).exists()).scalar()
