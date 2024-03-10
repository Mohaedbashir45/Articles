class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters long.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        authors_count = {}
        for article in self._articles:
            author_name = article.author.name
            authors_count[author_name] = authors_count.get(author_name, 0) + 1
        return [author for author, count in authors_count.items() if count > 2] if authors_count else None

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None
