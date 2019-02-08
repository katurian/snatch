import newspaper
from newspaper import Article
from newspaper import fulltext
import requests


def GetArticle(url, publication):
    def label(url):
        url_list = []
        for i in range(len(url)):
            if url[i] == "/":
                url_list.append(i)
        return url[url_list[len(url_list)-1] + 1:-1]

    if publication.lower() == "nyt" or publication.lower() == "new york times" or publication.lower() == "the new york times" or publication.lower() == "atlantic" or publication.lower() == "the atlantic" or publication.lower() == "breitbart" or publication.lower() == "breitbart news":
        print("GetArticle() cannot retrieve all article content for this publication.")
    article = Article(url)
    article.download()
    article.parse()
    html = requests.get(url).text
    text = article.text
    label = label(url)
    if label == None:
        label = "notitle"
    with open(publication + "$" + str(label) + ".txt", "w") as c:
        c.write(text)
        print("Article is at" + " " + (publication + "$" + str(label) + ".txt"))


GetArticle('https://www.nytimes.com/2001/09/12/us/us-attacked-hijacked-jets-destroy-twin-towers-and-hit-pentagon-in-day-of-terror.html', 'nyt')
