class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} posts)'

    def create_post(self, tltle, content):
        pass

    def json(self):
        pass