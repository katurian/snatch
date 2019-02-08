from newspaper import Article

def GetArticle_in():
    url = input("Enter the article's url: ")
    url = url[0:len(url)-1]
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
    if label == None:
        label = "notitle"
    with open(str(url[label[1] + 5:label[3]-13]) + "$" + str(url[label[len(label)-1] + 1:-1]) + ".txt", "w") as c:
        c.write(text)
    print("Article is at" + " " + ("$" + str(url[label[len(label)-1] + 1:-1]) + ".txt"))

GetArticle_in()
