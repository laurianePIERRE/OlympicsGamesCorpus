from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fivb.com/en/about/news")
    soup=bs(page_source, "html.parser")
    section=soup.find("section", {"class":"section-content"})
    print(section)
 #   div = section.find("div", {"class" : "col-md-4 news-gallery-item ng-scope clearleft"})
    articles = section.find_all("div", {"class":"white-box list"})
    print ("articles")
    urls=[]
    names=[]

    for article in articles:
        print("article in loop :")
        print(article)
        url = article.a['href']
        url = "https://www.fivb.com"+url
        urls.append(url)
        title_div = article.find('h3', {"class":"ng-binding"})
        name = title_div.text
        names.append(name)
    return urls,names