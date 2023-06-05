

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    urls = []
    names = []
    urls_pages = ["https://www.ffta.fr/actualites",
                  "https://www.ffta.fr/actualites?page=1"]
    for page in urls_pages :
        page_source = usual_function.get_page_source(page)
        soup=bs(page_source, "html.parser")
        page=soup.find("div", {"id":"actualites-page"})
        links= page.find_all("div", {"class":"details"})


        for link in links :
            url_plain = link.h2.a['href']
            url = "https://www.ffta.fr"
            urls.append(url)
            name = link.h2.a.text
            name = re.sub(" ","-",name)
            name = re.sub("[!?\xa0&;,#.\'\":\n\t|]*","",name)
            names.append(name)
    return urls, names