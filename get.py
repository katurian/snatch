import newspaper
from newspaper import Article
from newspaper import fulltext
import requests


def GetArticle(url, publication):
    article = Article(url)
    article.download()
    article.parse()
    html = requests.get(url).text
    text = article.text
    title = article.title
    date = str(article.publish_date)[0:10]
    authors = article.authors
    with open("raw" + "_" + publication + "_" + date + ".txt", "w") as c:
        c.write(text)
        print("Article is at" + " " + ("raw" + "_" + publication + "_" + date + ".txt"))
    image = article.top_image
    video = article.movies
    keywords = article.nlp()
    summary = article.summary

GetArticle('https://www.vox.com/future-perfect/2019/2/7/18215586/india-man-suing-parents-giving-birth-antinatalism-raphael-samuel', 'vox')

