#Using Beautiful Soup
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
#res2 = requests.get("https://news.ycombinator.com/news?p=2")
parser = BeautifulSoup(res.text, "html.parser")
# parser2 = BeautifulSoup(res2.text, "html.parser")
news = parser.select(".storylink")
subtext = parser.select(".subtext")



def sort_by_points(hn_list):
    return(sorted(hn_list, key= lambda k:k["votes"], reverse=True))



def create_custom_hackerNews(news, scores):
    hn = []                                                                         #HackerNews List
    for i, item in enumerate(news):
        title = item.get_text()
        links = item.get("href", None)               
        votes = subtext[i].select(".score")
        if len(votes):
            points = int(votes[0].getText().replace(" points", ""))
            #print(points)
            if(points >= 100):
                hn.append({"title": title, "links": links, "votes": points})
        
    return sort_by_points(hn)
    #pass


pprint.pprint(create_custom_hackerNews(news, subtext))