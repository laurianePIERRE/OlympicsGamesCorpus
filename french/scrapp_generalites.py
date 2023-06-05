
from bs4 import BeautifulSoup as bs, PageElement
import requests
import re
import os
import usual_function


LIST_OLYMPICS_GAMES= ['Athletisme', 'aviron', 'badminton', 'basketball', 'basketball3×3',
                      'boxe', 'canoe', 'canoe' ,'cyclisme-sur-piste', 'cyclisme-sur-route',
                      'BMX-freestyle', 'BMX-racing',  'escrime', 'football', 'golf',
                      'gymnastique-artistique', 'gymnastique-rythmique', 'trampoline',
                      'halterophilie', 'handball', 'hockey', 'judo', 'lutte',
                      'pentathlon-moderne', 'rugby', 'natation', 'natation-artistique',
                      'natation-marathon', 'plongeon', 'waterpolo', 'sports-equestres',
                      'taekwondo',  'tennis', 'tennis-de-table', 'tir', 'tir-a-l-arc',
                      'triathlon', 'voile', 'volleyball', 'volleyball-de-plage', 'Breaking',
                      'escalade-sportive', "skateboard"]

def pick_adress_sport_pages():
    """ pick the adress of the web pages
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://www.paris2024.org/fr/"
                                                 "sports-les-sports-olympiques/")
    soup = bs(page_source, "html.parser")
    page = soup.find("div", {"class":"container"})
    section = page.find_all("div",{"class":"block-classic-editor"})[3]
    links = section.find_all("a")
    urls = []
    names = []
    for link in links :

        url = link['href']
        urls.append(url)
        name = link.text
        name = re.sub(" ","-",name)
        name = re.sub("[!?\xa0&;,#.\'\":\n\t|]*","",name)
        names.append(name)
    return urls


