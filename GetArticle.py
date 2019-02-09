from newspaper import Article

def label(url):
    url_list = []
    for i in range(len(url)):
        if url[i] == "/":
            url_list.append(i)
    return url_list
    
def GetArticle(url):
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    parsed = label(url)
    with open(str(url[parsed[1] + 1:parsed[2]]) + "$" + str(url[parsed[len(parsed)-1] + 1:-1]) + ".txt", "w", encoding='utf8', errors='ignore') as c:
        c.write(text)
    print("Article is at" + " " + (str(url[parsed[1] + 1:parsed[2]]) + "$" + str(url[parsed[len(parsed)-1] + 1:-1]) + ".txt"))

GetArticle("https://www.theatlantic.com/magazine/archive/2018/01/putins-game/546548")
