from bs4 import BeautifulSoup as bs
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://uww.org/")
    soup=bs(page_source, "html.parser")
    section = soup.find('div',{"id" : "c-column--main"})
    links=section.find_all("section")
    links = links + section.find_all("li",{"class":"list-group-item"})
    urls=[]
    names=[]
    for link in links:
        div_link = link.find('a')
        if div_link :
            name = link.a.text
            name = re.sub("[\n#]","",name)
            names.append(name)
            url = link.a['href']
            url = "https://uww.org"+url
            urls.append(url)
    return urls,names

    # pick other articles
"""
    other_section = soup.find_all("li", {"class":"list-group-item"})
    for element in other_section:
        name = element.a.text
        name = re.sub("\n", "", name)
        names.append(names)
        url = element.a['href']
        url = "https://uww.org/"+url
        urls.append(url)
    return urls, names
"""