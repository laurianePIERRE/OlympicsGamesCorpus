
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffbad.org/la-ffbad/"
                                                 "toutes-les-actualites/")
    soup=bs(page_source, "html.parser")
    article= soup.find("div", {"class": "mduid3"})
    liens = article.find_all("div",{"class":"mduActualiteListContainer"})
    urls=[]
    names=[]
    compteur =0

    for lien in liens :
        # We limit on ten links"
        sous_div = lien.find("div", {"class":"cmsTitre2Container"})
        url = lien.a["href"]
        url = "https://www.ffbad.org"+url
        urls.append(url)
        name= lien.img["alt"]
        names.append(name)
        compteur = compteur +1
        if compteur == 20:
            break
    return urls,names


def scrapp_paragraph(url,ourpath,ourpath_plain):
    """

    :param url: url to scrap article
    :return:  text file which content article from url
    """

    page_source = usual_function.get_page_source(url)
    soup = bs(page_source, "html.parser")
    with open(ourpath_plain, mode="w", encoding="utf-8") as file:
        file.write(str(soup))
    divs= "div"
    sous_div = soup.find("div", {"class":"mduid3"})
    article = sous_div.find("div", {"class" : "mduActualiteContainer"})
    paragraph = article.text
    with open(ourpath, mode="w", encoding="utf-8") as file:
        file.write(str(paragraph))
    print("the file ",ourpath,' has been create')