#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':

    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")
    author_3 = Author("Rene Acosta")

    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")

    article_3 = Article(author_1, magazine_2, "TITLE")
    article_2 = Article(author_2, magazine_2, "Dating life in NYC")
    article_5 = Article(author_3, magazine_2, "My Article")
    article_3 = Article(author_3, magazine_2, "Other title")

    article_1 = author_1.add_article(magazine_1, "How to wear a tutu with style")
    
    print(magazine_1.contributing_authors())
