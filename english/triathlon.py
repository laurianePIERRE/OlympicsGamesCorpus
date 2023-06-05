from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://triathlon.org/news")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", {"class":"ais-hits media-list"})
    articles = section.find_all("div", {"class" : "ais-hits--item media"})
    urls=[]
    names=[]

    for article in articles:
        div = article.find('div', {'media-body'}).h1
        if div != None :
            name=div.a.text
            names.append(name)
            url=div.a['href']
            url = re.sub("\\'s"," ",url)
            url = "https://triathlon.org"+url
            urls.append(url)
    return urls,names