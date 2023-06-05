

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffgolf.org/Actus/Pro")
    soup=bs(page_source, "html.parser")
    page=soup.find("section", {"class":"filtered"})
    actu = page.find("div", {"class":"actu-container"})
    liens = actu.find_all("div",{"class":"col-sm-4 col-xs-12 bloc-actu bloc"})
    urls=[]
    names=[]

    for lien in liens:
        print (lien)
        url = lien.a['href']
        url = "https://www.ffgolf.org"+ url
        urls.append(url)
        sous_div = lien.find('div', {"class":"contenu"})
        if (sous_div != None) :
            print ("la")
            name = sous_div.find('div',{"class":"title"}).text
            print (name)
            name = re.sub(" ","-",name)
            name = re.sub("[,:\n\t]*","",name)
            names.append(name)
    return urls, names