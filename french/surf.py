

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.surfingfrance.com/disciplines.html")
    soup=bs(page_source, "html.parser")
    page=soup.find("div",{"class":"tm-block tm-block-light"})
    table = page.find("ul", {"id" : "itemListLeading"})
    links = page.find_all("li")
    urls=[]
    names=[]

    for link in links :
            div = link.find("div", {"class":"catItemHeader"})
            if div != None :
                url = div.h2.a['href']
                url = "https://www.surfingfrance.com"+url
                urls.append(url)
                name = div.h2.text
                name = re.sub(" ","-",name)
                name = re.sub("[\xa0&;,:\n\t]*","",name)
                names.append(name)
    return urls, names