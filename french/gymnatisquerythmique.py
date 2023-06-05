

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffgym.fr/Liste_d_actualites?"
                                                 "news_list_search%5Byear%5D=&news_list_sear"
                                                 "ch%5BdisciplineIds%5D%5B%5D=gymnastique_"
                                                 "rythmique&news_list_search%5BgeographicAre"
                                                 "aIds%5D%5B%5D=international&news_list_sear"
                                                 "ch%5BgeographicAreaIds%5D%5B%5D=national&n"
                                                 "ews_list_search%5Bsubmit%5D=")
    soup=bs(page_source, "html.parser")
    page=soup.find("div", {"class":"body-section"})
    actu = page.find("section", {"class":"content-list"})
    liens = actu.find_all("li")
    urls=[]
    names=[]

    for lien in liens:
        div = lien.find("h1")
        if div != None :
            url = div.a['href']
            url = re.sub("//www.ffgym.fr","https://www.ffgym.fr",url)
            urls.append(url)
            name = div.a.text
            name = re.sub(" ","-",name)
            name = re.sub("[,:\n\t]*","",name)
            names.append(name)
    return urls, names