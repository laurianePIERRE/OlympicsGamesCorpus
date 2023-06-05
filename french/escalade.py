

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffme.fr/")
    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"id":"main"})
    news = page.find("div",{"class":"ffme-actualites"})
    liens = news.find_all("a",{"class":"ffme-actualites__post"})
    urls=[]
    names=[]

    for lien in liens:
        url = lien["href"]
        urls.append(url)
        name= lien.h3.text
        name = re.sub(":", "", name)
        name = re.sub(" ", "-", name)
        names.append(name)
    return urls,names