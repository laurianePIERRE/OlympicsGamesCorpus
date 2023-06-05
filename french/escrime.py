

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.escrime-ffe.fr/fr/actualites/"
                                                 "toutes-les-actualites.html")
    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"class":"infinite-scroll"})
    news = page.find("div",{"class":"new_actus_listing"})
    liens = news.find_all("div",{"class":"actus_article_container grid-md-1-3 grid-sm-1-2 grid-1-1"})
    urls=[]
    names=[]

    for lien in liens:
        sous_div = lien.find('div', {"class":"actu-article-titre txt-noir gras"})
        if (sous_div != None) :

            url = sous_div.a["href"]
            urls.append(url)
            name= sous_div.a.text

            name = re.sub(" ","-",name)
            name = re.sub("[:\n\t]*","",name)
            names.append(name)
    return urls,names