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
    urls_pages = ["https://www.world.rugby/news", "https://www.world.rugby/news?p=2"]
    urls = []
    names = []
    for page in urls_pages :
        page_source = get_page_source(page)
        soup=bs(page_source, "html.parser")
        section=soup.find("section", {"class":"newsIndex newsListContainer"})
        links = section.find_all("figure", {"class" : "articleThumbLarge"})


        for link in links:
            url = link.a["href"]
            if re.match("/{1,2}www\.",url) :
                url = re.sub("/{1,2}www\.","https://www.",url)
            else:
                url = "https://www.world.rugby"+url
            urls.append(url)
            div_name = link.find("h3",{"class" : "title"})
            if div_name:
                name= div_name.text
                name = re.sub("\s {,2}" ," ",name)
                name = re.sub(" ","-",name)
                name = re.sub("\n", "", name)
                name = re.sub("[“”\-|?]+", "", name)
                names.append(name)
    return urls, names

def get_page_source (url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(5)
        buttonCookies = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[5]/button[1]")
        driver.execute_script("arguments[0].click();", buttonCookies)
        sleep(10)
        return driver.page_source
    finally:
        driver.quit()

