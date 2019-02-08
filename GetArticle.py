from newspaper import Article

def GetArticle(url):
    def label(url):
        url_list = []
        for i in range(len(url)):
            if url[i] == "/":
                url_list.append(i)
        return url_list
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    label = label(url)
    with open(str(url[label[1] + 1:label[2]]) + "$" + str(url[label[len(label)-1] + 1:-1]) + ".txt", "w") as c:
        c.write(text)
    print("Article is at" + " " + (str(url[label[1] + 1:label[2]]) + "$" + str(url[label[len(label)-1] + 1:-1]) + ".txt"))


GetArticle('https://www.nytimes.com/2001/09/12/us/us-attacked-hijacked-jets-destroy-twin-towers-and-hit-pentagon-in-day-of-terror.html')
