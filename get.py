import newspaper
from newspaper import Article
from newspaper import fulltext
import requests


def GetArticle(url, publication):
    def label(url):
        count = 0
        for i in range(len(url)):
            if url[i] == "/":
                count = count + 1
            if count == 5:
                return url[i + 1:-1]
    if publication.lower() == "nyt" or publication.lower() == "new york times" or publication.lower() == "the new york times" or publication.lower() == "atlantic" or publication.lower() == "the atlantic":
        print("GetArticle() cannot retrieve all article content for this publication.")
    article = Article(url)
    article.download()
    article.parse()
    html = requests.get(url).text
    text = article.text
    label = label(url)
    if label == None:
        label = "succ"
    with open(publication + "_" + str(label) + ".txt", "w") as c:
        c.write(text)
        print("Article is at" + " " + (publication + "_" + str(label) + ".txt"))


GetArticle('https://www.bbc.com/news/world-us-canada-47166938', 'bbc')
