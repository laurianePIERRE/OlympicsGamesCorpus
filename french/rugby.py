


from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffr.fr/actualites/au-coeur-du-jeu")
    soup=bs(page_source, "html.parser")
    page=soup.find("div",{"class":"col col-lg-8on9"})
    print(page)
   # section = page.find("div",{"class":"col col-lg-8on9"})
    links = page.find_all("a", {"class":"news news--list"})
    urls=[]
    names=[]

    for link in links :
            url = link['href']
            url = "https://www.ffr.fr"+url
            urls.append(url)
            title = link.find("p",{"class":"news__title ft-h3"})
            if title != None :
                name = title.text
                name = re.sub(" ","-",name)
                name = re.sub("[\xa0&;,:\n\t]*","",name)
                names.append(name)
    return urls, names