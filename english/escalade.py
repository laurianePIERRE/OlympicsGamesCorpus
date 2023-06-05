from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ifsc-climbing.org/index.php/news")
    soup=bs(page_source, "html.parser")
    items=soup.find_all("article", {"class":"uk-article"})
    urls=[]
    names=[]
    for item in items:
        name= item.h2.text
        names.append(name)
        url= item.h2.a["href"]
        url="https://www.ifsc-climbing.org"+url
        urls.append(url)
    # pick other articles


    return urls, names
