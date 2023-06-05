
from typing import Union, Any

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []
    page = "https://www.fmesgrima.es/Noticias23.html"
    page_source = usual_function.get_page_source(page)
    soup=bs(page_source, "html.parser")
    section = soup.find("div", {"class" :"noticias listamenu"})
    links= section.find_all("a")
    for link in links:
        name = link.text
        name = re.sub(" ", "-", name)
        name = re.sub("[:\./0-9?¿]+", "", name)
        name = re.sub("Ó", "O", name)
        names.append(name)
        url_b = link['href']
        url_b = re.sub("/\.","",url_b)
        url = "https://www.fmesgrima.es/"+url_b
        urls.append(url)

    return urls, names

def scrapp_divs_page(url,file_output) :
    page_source = usual_function.get_page_source(url)
    soup = bs(page_source, "html.parser")
    plain_soup = soup.encode("UTF-8")
    paragraphs = soup.find_all("td")
    result = ""
    for paragraphe in paragraphs:
        result = result + paragraphe.text + "\n"
    url_file = file_output + ".txt"
    file = open(url_file, 'w', encoding="utf_8")
    file.write("infos provenant de" + url + "\n")
    file.write(result)
    file.close()
    url_plain_file = file_output + "_plain.txt"
    plain_file = open(url_plain_file, 'w')
    plain_file.write(str(plain_soup))
    plain_file.close()
    print("the file " + file_output + " has been created")

