

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffhaltero.fr/Actualites")
    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"class":"pageContentWrapper"})
    print (page)
    liens = page.find_all("div", {"class":"item"})
    urls=[]
    names=[]

    for lien in liens:
        div = lien.find("div", {"class":"details"})
        if div != None :
            url = div.a['href']
            url = "https://www.ffhaltero.fr"+url
            urls.append(url)
            name = div.h3.text
            name = re.sub(" ","-",name)
            name = re.sub("[,:\n\t]*","",name)
            names.append(name)
    return urls, names