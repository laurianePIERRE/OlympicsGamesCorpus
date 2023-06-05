
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("http://federemo.org/category/noticias/")
    soup=bs(page_source, "html.parser")
    section=soup.find("div", { "id":"cat-blog-wrapper"})
    links = section.find_all("li")
    urls=[]
    names=[]

    for link in links:
        # limit to  20 links
       if len(names) != 50:
            print(link)
            url = link.a['href']
            url = "https://www.rfea.es/noticias/"+url
            urls.append(url)
            name= link.a['title']
            name = re.sub(" ","-",name)
            name = re.sub(":","",name)
            name = re.sub("<[A-Za-z]*>",'',name)
            name = re.sub("</[A-Za-z]*>", '', name)
            names.append(name)
    return urls, names