from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("http://m.worldtaekwondo.org/wtnews/"
                                                 "list.html?mcd=C02")
    soup=bs(page_source, "html.parser")
    section = soup.find("ul", {"class":"news_list"})
    liens=section.find_all("li")
    urls=[]
    names=[]
    for lien in liens:
        sous_div = lien.find("dl")
        div = sous_div.find("dd")
        if div != None :
            name= div.a.text
            names.append(name)
            url= sous_div.a["href"]
            url = "http://www.worldtaekwondo.org"+url
            urls.append(url)
    return urls, names
