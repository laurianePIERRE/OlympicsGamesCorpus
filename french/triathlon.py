

from bs4 import BeautifulSoup as bs, PageElement
import requests
import re

import usual_function


def pick_adress_sport_pages():
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.fftri.com/actualites/?wpv_"
                                                 "view_count=501&wpv_post_search=&wpv_paged=2")
    soup = bs(page_source, "html.parser")
    page = soup.find("div", {"id":"liste_actualites"})
    print  (page)
    links = page.find_all("li", {"class":"actualite"})
    urls = []
    names = []

    for link in links :
        print("link in loop: ")
        print (link)
        details_div = link.find("div", {"class" : "details_actualite"})
        if details_div != None :
            url = link.a['href']
            urls.append(url)
            name = link.h2.text
            name = re.sub(" ","-",name)
            name = re.sub("[!?\xa0&;,#.\'\":\n\t|]*","",name)
            names.append(name)
    return urls, names