class Post:
    def __init__(self, post_id, user_id, created, updated, title, text):
        self.id = post_id
        self.user_id = user_id
        self.title = title
        self.text = text
        self.created = created
        self.updated = updated
