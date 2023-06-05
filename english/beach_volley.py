from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import usual_function


def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = get_page_source("https://www.fivb.com/en/about/news")
    soup=bs(page_source, "html.parser")
    articles=soup.find("div", {"class": "grid-content news-gallery"})
    links = articles.find_all("div", {"class" :"white-box list"})
    urls=[]
    names=[]

    for link in links :
        url = link.a["href"]
        url = "https://www.fivb.com" + url
        urls.append(url)
        div_name = link.find("h3", {"class":"ng-binding"})
        if div_name :
            name = div_name.text
            name = re.sub("\s {,2}", " ", name)
            name = re.sub("\n", "", name)
            name = re.sub("[“”|]+", "", name)
            names.append(name)
    return urls, names


def get_page_source (url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(10)
        button_category_beachvolley = driver.find_element(By.XPATH,
                                                          "/html/body/div[1]/article/section[3]/div/div/div/div/nav/a[4]")
        driver.execute_script("arguments[0].click();",button_category_beachvolley)
        sleep(10)
        return driver.page_source
    finally:
        driver.quit()

