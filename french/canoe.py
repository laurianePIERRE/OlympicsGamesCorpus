

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffck.org/nos-actualites/")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", {"class":"main_wapper"})
    print (section)

    liens = section.find_all("div",{"class":"actus_box_second"})
    print ("liens")
    print (liens)
    urls=[]
    names=[]

    for lien in liens:
        name_div = lien.find("div", {"class":"details_box"})
        if name_div != None :
            link = name_div.find("h3")
            url = link.a["href"]
            urls.append(url)
            name= link.a.text
            name = re.sub(" ","-",name)
            name = re.sub(":","",name)
            names.append(name)
    return urls,names