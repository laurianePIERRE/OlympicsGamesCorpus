

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://medias.ffhandball.fr/")
    soup=bs(page_source, "html.parser")
    page=soup.find("section", {"class":"container_lastNews bgBlue"})
    print (page)
    liens = page.find_all("div", {"class":"post-info"})
    urls=[]
    names=[]

    for lien in liens:
        div = lien.find("div", {"class":"text-wrapper"})
        if div != None :
            title = div.find("h3",{"class":"entry-title"})
            if title != None :
                url = title.a['href']
                urls.append(url)
                name = title.a.text
                name = re.sub("\s{2,}", "", name)
                name = re.sub(" ","-",name)
                name = re.sub("[,:\n\t]*","",name)
                names.append(name)
    return urls, names