import re
import time
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
def print_var(var):
    name= str(var)
    print(name, " :", var, "\n len : ", len(var), ', type : ', type(var), '\n')

def scrapper_english_with_specific_function(sport,function_url_article,scrapper_function):
   """

   :param sport: sport
   :param function_url_article: fiontion scrapp list of url's article
   :param scrapper_function: specific function when the paragraphs aren't tags with <p> only
   :return:files
   """
   PATH_FILE_ENGLISH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                       "Jeux Olympiques/decembre/anglais/"
   urls, names= function_url_article()
   articles_numbers = len(urls)
   for url,name in zip(urls,names):
       print ("ok")
       print (url)
       try:
           print(" Scrap is in progress ... ")
           scrapper_function(url,PATH_FILE_ENGLISH+sport+"/"+name+".txt")
           print(" scrap finish")
       except FileNotFoundError:
           new_name= "news_other"
           scrapper_function(url,PATH_FILE_ENGLISH+sport+"/"+new_name+".txt")
       except OSError:
           new_name=re.sub("[/ /\n]+","-",name)
           scrapper_function(url,PATH_FILE_ENGLISH+sport+"/"+new_name+".txt")
   #   except AttributeError:
      #     print (" attributeError")
       #    articles_numbers = articles_numbers - 1
        #   continue


def scrapper_french_with_specific_function(sport,function_url_article,scrapper_function):
   """

   :param sport: sport
   :param function_url_article: fiontion scrapp list of url's article
   :param scrapper_function: specific function when the paragraphs aren't tags with <p> only
   :return:files
   """
   FRENCH_FILE_PATH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                      "Jeux Olympiques/decembre/français/"
   urls, names= function_url_article()
   print(urls)

   articles_numbers = len(urls)
   for url,name in zip(urls,names):
       print ("ok")
       print (url)
       print ("name :",name)
       try:
           print(" Scrap is in progress ... ")
           scrapper_function(url,FRENCH_FILE_PATH+sport+"/"+name+".txt",
                             FRENCH_FILE_PATH+sport+"/"+name+"_plain.txt")
           print(" scrap finish")
       except FileNotFoundError:
           new_name= "news_other"
           scrapper_function(url,FRENCH_FILE_PATH+sport+"/"+new_name+".txt",
                             FRENCH_FILE_PATH+sport+"/"+new_name+"_plain.txt")
       except OSError:
           new_name=re.sub("[/ /\n]+","-",name)
           scrapper_function(url,FRENCH_FILE_PATH+sport+"/"+new_name+".txt",
                             FRENCH_FILE_PATH + sport + "/" + new_name + "_plain.txt")
   #   except AttributeError:
      #     print (" attributeError")
       #    articles_numbers = articles_numbers - 1
        #   continue


def scrapper_spanish_with_specific_function(sport,function_url_article,scrapper_function):
   """

   :param sport: sport
   :param function_url_article: fiontion scrapp list of url's article
   :param scrapper_function: specific function when the paragraphs aren't tags with <p> only
   :return:files
   """
   SPANISH_FILE_PATH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                       "Jeux Olympiques/decembre/espagnol/"

   urls, names= function_url_article()
   articles_numbers = len(urls)
   for url,name in zip(urls,names):
       print ("ok")
       print (url)
       try:
           print(" Scrap is in progress ... ")
           scrapper_function(url,SPANISH_FILE_PATH+sport+"/"+name+".txt")
           print(" scrap finish")
       except FileNotFoundError:
           new_name= "news_other"
           scrapper_function(url,SPANISH_FILE_PATH+sport+"/"+new_name+".txt")
       except OSError:
           new_name=re.sub("[/ /\n]+","-",name)
           scrapper_function(url,SPANISH_FILE_PATH+sport+"/"+new_name+".txt")
   #   except AttributeError:
      #     print (" attributeError")
       #    articles_numbers = articles_numbers - 1
        #   continue


def scrapper_spanish(sport,function_url_article):
   """

   :param sport: sport
   :param function_url_article: fiontion scrapp list of url's article
   :param function_scrapp: scrap article's containe
   :return:files
   """
   SPANISH_FILE_PATH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                       "Jeux Olympiques/decembre/espagnol/"

   urls, names= function_url_article()
   articles_numbers = len(urls)
   for url,name in zip(urls,names):
       our_path = SPANISH_FILE_PATH + sport + "/" + name + ".txt"
       print("path ", our_path)
       print("---------------------------------------------------------------------------------")
       print ("ok")
       print (url)
       print(name)
       try:
           print(" Scrap is in progress ... ")
           scrap_paragraphs(url,our_path,
                            SPANISH_FILE_PATH+sport+"/"+name+"_plain.txt")
           print(" scrap finish")
       except FileNotFoundError:
           new_name= "news_other"
           scrap_paragraphs(url, SPANISH_FILE_PATH + sport + "/" + new_name + ".txt",
                            SPANISH_FILE_PATH + sport + "/"  + new_name + "_plain.txt")
       except OSError:
           new_name=re.sub("[/]+","-",name)
           new_name = re.sub("\\'s","s",new_name)
           #new_name = re.sub("\"","",new_name)
           scrap_paragraphs(url, SPANISH_FILE_PATH + sport +"/" + new_name + ".txt",
                            SPANISH_FILE_PATH + "/"+ sport + new_name + "_plain.txt")
   #   except AttributeError:
      #     print (" attributeError")
       #    articles_numbers = articles_numbers - 1
        #   continue


def scrapper_french(sport,function_url_article):
   """

   :param sport: sport
   :param function_url_article: fiontion scrapp list of url's article
   :param function_scrapp: scrap article's containe
   :return:files
   """
   FRENCH_FILE_PATH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                      "Jeux Olympiques/decembre/français/"
   urls, names= function_url_article()
   articles_numbers = len(urls)
   for url,name in zip(urls,names):
       our_path = FRENCH_FILE_PATH + sport + "/" + name + ".txt"
       print("path ", our_path)
       print("---------------------------------------------------------------------------------")
       print ("ok")
       print (url)
       print(name)
       try:
           print(" Scrap is in progress ... ")
           scrap_paragraphs(url,our_path,
                            FRENCH_FILE_PATH+sport+"/"+name+"_plain.txt")
           print(" scrap finish")
       except FileNotFoundError:
           new_name= "news_other"
           scrap_paragraphs(url, FRENCH_FILE_PATH + sport + "/" + new_name + ".txt",
                            FRENCH_FILE_PATH + sport + "/"  + new_name + "_plain.txt")
       except OSError:
           new_name=re.sub("[/]+","-",name)
           new_name = re.sub("\\'s","s",new_name)
           #new_name = re.sub("\"","",new_name)
           scrap_paragraphs(url, FRENCH_FILE_PATH + sport +"/" + new_name + ".txt",
                            FRENCH_FILE_PATH + "/"+ sport + new_name + "_plain.txt")
   #   except AttributeError:
      #     print (" attributeError")
       #    articles_numbers = articles_numbers - 1
        #   continue


def scrapper_english(sport,function_url_article):
   """

   :param sport: sport
   :param function_url_article: fiontion scrapp list of url's article
   :param function_scrapp: scrap article's containe
   :return:files
   """
   PATH_FILE_ENGLISH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                       "Jeux Olympiques/decembre/anglais/"

   urls, names= function_url_article()
   articles_numbers = len(urls)

   for url,name in zip(urls,names):
       our_path=PATH_FILE_ENGLISH+sport+"/"+name+".txt"
       try:
           print(" Scrap is in progress ... ")
           print(url)
           scrap_paragraphs(url,our_path,
                            PATH_FILE_ENGLISH+sport+"/"+name+"_plain.txt")
           print(" scrap finish")
       except FileNotFoundError:
           new_name= "news_other"
           scrap_paragraphs(url, PATH_FILE_ENGLISH + sport + "/" + new_name + ".txt",
                            PATH_FILE_ENGLISH + sport + "/"  + new_name + "_plain.txt")
       except OSError:
           new_name=re.sub("[/]+","-",name)
           new_name = re.sub("\\'s","s",new_name)
           new_name = re.sub("\"","",new_name)
           scrap_paragraphs(url, PATH_FILE_ENGLISH + sport +"/" + new_name + ".txt",
                            PATH_FILE_ENGLISH + "/"+ sport + new_name + "_plain.txt")
   #   except AttributeError:
      #     print (" attributeError")
       #    articles_numbers = articles_numbers - 1
        #   continue

def clear_flex_tag(url) :
    """ Cleaning html page
    return html page without flex tag
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("--hearless")
    driver = webdriver.Chrome("/user/lib/chromium-brower/chromedriver", chrome_options=options)
    driver.get(url)
    time.sleep((3))
    page_source = driver.page_source
    return page_source

def get_text_from_elements(elements):
    return [element.text for element in elements]

def get_page_source(url):
    """
    Take an URL, return the page source completed

    """
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        sleep(3)
        return driver.page_source
    finally:
        driver.quit()

def get_page_source_natation_spe(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element(By.CLASS_NAME,"button load-more-button js-show-more-button").click()
        sleep(5)
        return driver.page_source
    finally:
        driver.quit()


def store_texts(outpath, texts):
    with open(outpath, mode='w',encoding="utf-8") as file:
        file.writelines(str(texts)+"\n")

def store_paragraphs (ourpath, texts, divs) :
    with open(ourpath, mode="w", encoding="utf-8") as file :
        for paragraph in texts :
            file.writelines(str(paragraph)+"\n")

def get_paragraph_specific_div(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    return soup.find_all("div",{"class":"main-content"})

def get_paragraph(page_source) :
     soup = BeautifulSoup(page_source,"html.parser")
     return soup.find_all('p')


def get_div(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    return soup.find_all('div')


def get_element(page_source) :
     return BeautifulSoup(page_source,"html.parser").encode("UTF-8")

def scrap_paragraphs(url,path,plain_path) :
    path = re.sub("\n\t",'',path)
    plain_path = re.sub('\n','',plain_path)
    page_source = get_page_source(url)
    paragraphs=get_paragraph(page_source)
    paragraphs_text=get_text_from_elements(paragraphs)
    divs=get_div(page_source)
    divs_text = get_text_from_elements(divs)
    print ("Path is scrap_paragraph : ",path)
    store_paragraphs(path,paragraphs_text,divs)
    store_element = get_element(page_source)
    html_page= store_texts(plain_path,store_element)
    print("the file ",path," has been created")

def scrap_paragraphs_specific_div(url,path,plain_path) :
    path = re.sub("\n\t",'',path)
    plain_path = re.sub('\n','',plain_path)
    page_source = get_page_source(url)
    paragraphs=get_paragraph_specific_div(page_source)
    print (paragraphs)
    paragraphs_text=get_text_from_elements(paragraphs)
    divs=get_div(page_source)
    divs_text = get_text_from_elements(divs)
    print ("Path is scrap_paragraph : ",path)
    store_paragraphs(path,paragraphs_text,divs)
    store_element = get_element(page_source)
    html_page= store_texts(plain_path,store_element)
    print("the file ",path," has been created")
