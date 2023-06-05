from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.gymnastics.sport/site/"
                                                 "discipline.php?disc=4")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", {"id":"sportnews"})
    articles = section.find_all("div", {"class" : "news-teaser news-teaser--smaller"})
    urls=[]
    names=[]

    for article in articles:
        url = article.a['href']
        url = re.sub("./","/",url)
        url = re.sub("/new/","/news/",url)
        url = "https://www.gymnastics.sport/site"+url
        urls.append(url)
        div = article.find ("div", {"class":"news-teaser__body"})
        if div != None :
            name = div.h3.text
            names.append(name)
    return urls,names