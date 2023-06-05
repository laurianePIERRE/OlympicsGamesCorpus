from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = get_page_source("https://www.fei.org/stories?&content=1")
    soup=bs(page_source, "html.parser")
    articles=soup.find("div",{"class":"region region-content"})
    links = articles.find_all("div", {"class": "title"})
    urls=[]
    names=[]

    for link in links :
        name = link.a.text
        name = re.sub("\s {,2}", " ", name)
        name = re.sub(" ", "-", name)
        name = re.sub("\n", "", name)
        name = re.sub("[“”\-|?]+", "", name)
        names.append(name)
        url = link.a["href"]
        url = "https://www.fei.org"+url
        urls.append(url)
    return urls, names


def get_page_source (url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(60)

    finally:
        driver.quit()


