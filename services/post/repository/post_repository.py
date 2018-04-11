from flask_sqlalchemy import SQLAlchemy
from services.post.domain.post import Post
from services.post import app


db = SQLAlchemy(app)


class PostDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


class PostRepository:
    def __init__(self, app):
        self.db = SQLAlchemy(app)

    def create(self, user_id, text, date):
        post = PostDB(user_id=user_id, text=text, date=date)
        self.db.session.add(post)
        self.db.session.commit()
        return post.id

    def read(self, post_id):
        if self.exists(post_id):
            post = PostDB.query.filter_by(id=post_id).first()
            return Post(post_id=post.id, user_id=post.user_id, date=post.date, text=post.text)
        else:
            return None

    def read_all_by_criteria(self, criteria):
        posts = []
        if criteria is None:
            posts_from_db = PostDB.query.all()
        else:
            posts_from_db = PostDB.query
            if "author_id" in criteria:
                posts_from_db = posts_from_db.filter_by(user_id=criteria["author_id"]).all()
            if "title" in criteria:
                posts_from_db = posts_from_db.filter(PostDB.title.like("%"+criteria["title"]+"%")).all()
            if "after_date" in criteria:
                posts_from_db = posts_from_db.filter(PostDB.date > criteria["after_date"]).all()

        for post in posts_from_db:
            posts.append(Post(post_id=post.id, user_id=post.user_id, date=post.date, text=post.text, title=post.title))
        return posts

    def update(self, post_id, user_id, text, date):
        if self.exists(post_id):
            post_to_update = PostDB.query.filter_by(id=post_id).first()
            post_to_update.user_id = user_id
            post_to_update.text = text
            post_to_update.date = date
            self.db.session.commit()

    def delete(self, post_id):
        if self.exists(post_id):
            post_to_delete = PostDB.query.get(post_id)
            self.db.session.delete(post_to_delete)
            self.db.session.commit()

    def exists(self, post_id):
        return self.db.session.query(PostDB.query.filter(PostDB.id == post_id).exists()).scalar()
