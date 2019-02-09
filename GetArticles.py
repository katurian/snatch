import feedparser
from newspaper import Article

def getURLs(feed):
    links = []
    d = feedparser.parse(feed)
    for l in range(0, len(d['entries'])-1):
        link = d['entries'][l]['link']
        links.append(link)
    return links

def label(url):
    url_list = []
    for i in range(len(url)):
        if url[i] == "/":
            url_list.append(i)
    return url_list

def GetArticles(feed):
    rss_links = getURLs(feed)
    for i in range(0, len(rss_links)):
        url = rss_links[i]
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        parsed = label(url)
        with open(str(url[parsed[1] + 1:parsed[2]]) + "$" + str(url[parsed[len(parsed) - 1] + 1:-1]) + ".txt", "w") as c:
            c.write(text)
        print("Article is at" + " " + (str(url[parsed[1] + 1:parsed[2]]) + "$" + str(url[parsed[len(parsed) - 1] + 1:-1]) + ".txt"))


GetArticles("https://www.economist.com/leaders/rss.xml")
