

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fff.fr/voir_plus/dernieres_actualites.html")
    soup=bs(page_source, "html.parser")
    page=soup.find("main", {"class": "flex flex_wrap margin_b30 container main--toute-lactu"})
    section = page.find("div",{"class":"actualities-container"})
    liens = section.find_all("a")
    print(" liens")
    print(liens)
    urls=[]
    names=[]

    for lien in liens:
        if len(urls) != 20 :
            url = lien["href"]
            url = "https://www.fff.fr"+url
            urls.append(url)
            sous_div = lien.find('figcaption')
            if (sous_div != None) :
                name= sous_div.h3.text
                name = re.sub(" ","-",name)
                name = re.sub("[:\n\t]*","",name)
                names.append(name)
    return urls, names