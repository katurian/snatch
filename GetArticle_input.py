from newspaper import Article

def label(url):
    url_list = []
    for i in range(len(url)):
        if url[i] == "/":
            url_list.append(i)
    return url_list
    
def GetArticle_in():
    url = input("Enter the article's url: ")
    url = url[0:len(url)-1]
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    parsed = label(url)
    with open(str(url[parsed[1] + 1:parsed[2]]) + "$" + str(url[parsed[len(parsed)-1] + 1:-1]) + ".txt", "w", encoding='utf8', errors='ignore') as c:
        c.write(text)
    print("Article is at" + " " + (str(url[parsed[1] + 1:parsed[2]]) + "$" + str(url[parsed[len(parsed)-1] + 1:-1]) + ".txt"))

GetArticle_in()
