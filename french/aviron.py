
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffaviron.fr/actualites")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", {"class":"plugins-content"})
    article = section.find("div", {"class":"plugin-index-large-inside"})
    liens = article.find_all("a",{"target":"_self"})
    urls=[]
    names=[]

    for lien in liens:
        url = lien["href"]
        url = "https://www.ffaviron.fr/"+url
        urls.append(url)
        div = lien.find("div", {"class":"col-left"})
        sous_div = div.find("div", {"class":"title"})

        name= lien.text
        name = re.sub('[\'\n]*','',name)
        name= re.sub("/","_",name)
        names.append(name)
    return urls,names