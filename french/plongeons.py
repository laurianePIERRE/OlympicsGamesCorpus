

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffnatation.fr/actualites/plongeon")
    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"id":"block-system-main"})
    links = page.find_all("div",{"class":"views-field views-field-title"})
    print ("links : ",links)
    urls=[]
    names=[]

    for link in links :
        url_plain = link.a['href']
        url = "https://www.ffnatation.fr"+url_plain
        urls.append(url)
        name = link.a.text
        name = re.sub(" ","-",name)
        name = re.sub("[,:.\"\n\t]*","",name)
        names.append(name)
    return urls, names
