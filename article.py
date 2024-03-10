class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Article title must be a string between 5 and 50 characters long.")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
