

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page = "https://www.ffc.fr/lactualite-de-la-federation/" \
           "?fwp_disciplines=vtt&fwp_load_more=2"
    page_source = usual_function.get_page_source(page)
    soup=bs(page_source, "html.parser")
    section=soup.find("section", {"id":"content"})
    links = section.find_all("article",{"class":"card-post card-post--simple reveal"})
    urls=[]
    names=[]

    for link in links:
        url = link.a["href"]
        urls.append(url)
        div_title = link.find("div", {"class":"card-post__content"})
        if div_title :
            name = div_title.h1.text
            name = re.sub("[\n\t]*","",name)
            name = re.sub("Ü","U",name)
            name = re.sub(" ","-",name)
            name = re.sub(":","",name)
            names.append(name)
    return urls,names