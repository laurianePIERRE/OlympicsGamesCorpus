
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
    url_pages = ["https://www.feboxeo.es/feboxeo-noticias.php?p=2&cBusc=BOXEO&i1=0&pg=1&ap=2",
                "https://www.feboxeo.es/feboxeo-noticias.php?p=2&cBusc=BOXEO&i1=2&pg=2&ap=2",
                "https://www.feboxeo.es/feboxeo-noticias.php?p=2&cBusc=BOXEO&i1=4&pg=3&ap=2"]
    for page in url_pages:

        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        section = soup.find("div", {"id" :"caIzquierda"})
        links= section.find_all("div", {"style":"width:75%; margin-top:35%; background:#FFFFFF; "
                                                "margin-left:7.5%; padding:5%; float:left;"})

        for link in links:
            div_title = link.find("div", {"style":"width:100%; float:left; font-family:verdana; "
                                                  "font-size:36px; color:#27343d; font-weight:"
                                                  "bold; min-height:40px; line-height:40px;"})
            if div_title :
                name = div_title.text
                name = re.sub(" ", "-", name)
                name = re.sub("[:\./0-9?¿]+", "", name)
                name = re.sub("Ó", "O", name)
                names.append(name)
            div_link = link.find("a")
            if div_link:
                print (div_link)
                url_b = link.a['href']
                url = "https://www.feboxeo.es/"+url_b
                urls.append(url)

    return urls, names

def scrapp_divs_page(url,file_output) :
    page_source = usual_function.get_page_source(url)
    soup = bs(page_source, "html.parser")
    plain_soup = soup.encode("UTF-8")
    paragraphs = soup.find_all("div")
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

