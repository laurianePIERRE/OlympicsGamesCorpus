

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.ffgym.fr/Liste_d_actualites?"
                                                 "news_list_search%5Bfirst_submit%5D=&news_"
                                                 "list_search%5Byear%5D=&news_list_search%5B"
                                                 "disciplineIds%5D%5B%5D=gymnastique_artisti"
                                                 "que_feminine&news_list_search%5Bdiscipline"
                                                 "Ids%5D%5B%5D=gymnastique_artistique_mascul"
                                                 "ine&news_list_search%5BgeographicAreaIds%5"
                                                 "D%5B%5D=international&news_list_search%5B"
                                                 "geographicAreaIds%5D%5B%5D=national")
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