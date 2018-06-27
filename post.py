class Post:

    def __init__(self, title, content):
        self.content = content
        self.title = title

    def json(self):
        return{
            'title': self.title,
            'content': self.content,
        }
