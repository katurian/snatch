import newspaper
from newspaper import Article
from newspaper import fulltext
import requests


def GetArticle_in():
    url = input("Enter the article's url: ")
    url = url[0:len(url)-1]
    publication = input("Enter the publication your article is sourced from: ")
    def label(url):
        url_list = []
        for i in range(len(url)):
            if url[i] == "/":
                url_list.append(i)
        return url[url_list[len(url_list)-1] + 1:-1]

    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    label = label(url)
    if label == None:
        label = "notitle"
    with open(publication + "$" + str(label) + ".txt", "w") as c:
        c.write(text)
        print("Article is at" + " " + (publication + "$" + str(label) + ".txt"))


GetArticle_in()
