class Post:
    def __init__(self, post_id, user_id, date, title, text):
        self.id = post_id
        self.user_id = user_id
        self.title = title
        self.text = text
        self.date = date