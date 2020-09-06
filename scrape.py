#Using Beautiful Soup
import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
parser = BeautifulSoup(res.text, "html.parser")
news = parser.select(".storylink")
subtext = parser.select(".subtext")

def create_custom_hackerNews(news, scores):
    hn = []                                                                         #HackerNews List
    for i, item in enumerate(news):
        title = item.get_text()
        links = item.get("href", None)               
        votes = subtext[i].select(".score")
        if len(votes):
            points = int(votes[0].getText().replace(" points", ""))
            print(points)
            hn.append({"title": title, "links": links, "votes": points})
        
    return hn
    #pass


print(create_custom_hackerNews(news, subtext))