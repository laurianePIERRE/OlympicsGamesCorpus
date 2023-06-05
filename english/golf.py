from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.golfchannel.com/news/golf-central")
    soup=bs(page_source, "html.parser")
    items=soup.find_all("div", {"role":"article"})
    urls=[]
    names=[]
    for item in items:
        name= item.h1.a.text
        names.append(name)
        url= item.h1.a["href"]
        url="https://www.golfchannel.com"+url
        urls.append(url)
    # pick other articles


    return urls, names
