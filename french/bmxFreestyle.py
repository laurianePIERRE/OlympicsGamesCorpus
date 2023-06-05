
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function




def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffc.fr/lactualite-de-la-fede"
                                                 "ration/?fwp_disciplines=freestyle&fwp"
                                                 "_load_more=3")
    soup=bs(page_source, "html.parser")
    article= soup.find("section", {"id": "content"})

    liens = article.find_all("article")

    urls=[]
    names=[]

    for lien in liens :
        # We limit on ten links"
        ref = lien.find("a", {"class":"card-post__link"})
        div = lien.find("h1", {"class":"card-post__title dove"})
        if div != None:
            url = ref["href"]
            urls.append(url)
            name = div.text
            name = re.sub("[\n\t]*","",name)
            name = re.sub(" ", "-", name)
            name = re.sub(":", "", name)
            names.append(name)

    return urls,names
