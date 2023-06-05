from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ijf.org/news"
                                                 "/list?tag[0]=competition")
    soup=bs(page_source, "html.parser")
    items=soup.find_all("a", {"class":"news-item"})
    urls=[]
    names=[]

    for item in items:
        div = item.find('div', {"class":"texts"})
        if div != None :
            sous_div=div.find('div', {"class":"title"})
            name= sous_div.text
            names.append(name)
            url= item["href"]
            url = "https://www.ijf.org/"+url
            urls.append(url)
        # pick other articles
    return urls, names
