# Class to represent an Article with attributes for author, magazine, and title
class Article:
    # Class variable to store all instances of Article
    all = []

    def __init__(self, author, magazine, title):
        # set the author of the article, set the magazine where the article is published, set the title of the article, add the article to the class variable all
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    # decorator to get the author of the article
    @property
    def author(self):
        return self._author

    # settter decorator to set the author of the article 
    @author.setter
    def author(self, new_author):
        # Check if the new_author is an instance of Author class
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            return None

    # decorator to get the magazine where the article is published
    @property
    def magazine(self):
        return self._magazine

    # setter to set the magazine where the article is published
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            return None
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance (title, str) and 5 <= len(title) <= 50 and not hasattr(self, "_title"):
            self._title = title
        else:
            return None

class Author:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return f"Author('{self.name}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str)and 0 < len(new_name) and not hasattr(self, "_name"):
            self._name = new_name

    # method to get all articles written by the author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    #method to get all magazines where the author has contributed 
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    # method to add a new article to the authors list of articles 
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # method to get all topic areas where the author has contributed
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and 0 < len(new_category):
            self._category = new_category

    #method to get all articles published in the magazine 
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # method to get all contributors to the magazine 
    def contributors(self):
        return list({article.author for article in self.articles()})

    # method to get all article titles published in the magazine
    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    # method to get contributing authors who have contributed more than 2 articles 
    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None