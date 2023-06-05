
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """

    urls_pages = ["http://www.ffbb.com/edf/equipes-france-masculines-actus",
                  "http://www.ffbb.com/edf/equipes-france-masculines-actus?page=1"]

    urls = []
    names = []
    for page in urls_pages:
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        article= soup.find("section", {"id": "content"})
        liens = article.find_all("a",{"class":"actus-details"})
        div_names = article.find_all("span", {"class":"title"})


        for lien,divn in zip(liens,div_names) :
            # We limit on ten links"
            url = lien["href"]
            url = "https://www.ffbb.com"+url
            urls.append(url)
            name= divn.text
            name = re.sub("[\n\t:\"]","",name)
            name = re.sub("\s{2,}" ," ",name)
            names.append(name)

    return urls,names


def scrapp_paragraph(url,ourpath,ourpath_plain):
    """

    :param url: url to scrap article
    :return:  text file which content article from url
    """

    page_source = usual_function.get_page_source(url)
    soup = bs(page_source, "html.parser")
    with open(ourpath_plain, mode="w", encoding="utf-8") as file:
        file.write(str(soup))

    sous_div = soup.find("div", {"id":"content-area"})
    paragraphs = sous_div.find_all("div")
    result=""
    for paragraphe in paragraphs:
        result = result + paragraphe.text + "\n"
    with open(ourpath, mode="w", encoding="utf-8") as file:
        file.write(str(result))
    print("the file ",ourpath,' has been create')