
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls=[]
    names=[]
    ulrs_pages = ["https://www.ffboxe.com/actualites/",
                  "https://www.ffboxe.com/actualites/?_pagination=2"]
    for page in ulrs_pages:
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section=soup.find("div", {"id":"_dynamic_list-6-78811"})
        liens = section.find_all("a",{"class":"ct-link archive-bottom-item"})
        for lien in liens:
            url = lien["href"]
            urls.append(url)
            name= lien.div.text
            name = re.sub(" ","-",name)
            name = re.sub(":","",name)

            names.append(name)
    return urls, names