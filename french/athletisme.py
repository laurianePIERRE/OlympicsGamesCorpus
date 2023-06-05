
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.athle.fr/federation/")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", {"id":"ctnMain"})
    article = section.find("div", {"id":"ctnContent"})
    liens = article.find_all("a",{"target":"_self"})
    urls=[]
    names=[]

    for lien in liens:
        url = lien["href"]
        url = "https://www.athle.fr"+url
        urls.append(url)
        name= lien.text
        name = re.sub(" ","-",name)
        name = re.sub(":","",name)

        names.append(name)
    return urls,names