
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.badminton.es/news/148285/Kike"
                                                 "-Penalver-cae-peleando-ante-el-indio-Maisn"
                                                 "am-en-su-debut-en-el-Swiss-Open")
    soup=bs(page_source, "html.parser")
    section=soup.find_all("div", {"class":"block"})[0]
    links = section.find_all("a")
    urls=[]
    names=[]

    for link in links:
        # limit to  20 links

       if len(names) != 20:
           print(link)
           url = link['href']
           url = "https://www.badminton.es"+url
           urls.append(url)
           name= link.text
           print (name)
           name = re.sub(" ","-",name)
           name = re.sub("[:\./0-9]+","",name)
           names.append(name)
    return urls, names