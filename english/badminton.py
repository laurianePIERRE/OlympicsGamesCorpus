from bs4 import BeautifulSoup as bs
import requests
import re

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    reponse = requests.get("https://bwfbadminton.com/news/")
    html=reponse.content
    soup=bs(html, "lxml")
    section = soup.find("section", {"class" : "home-news container-sitewidth"})
    items=section.find_all("div", {"class":"feature-image"})
    urls=[]
    names=[]
    for item in items:
        name= item.a["title"]
        names.append(name)
        url= item.a["href"]
        urls.append(url)
    # pick other articles
    new_section = soup.find("div",{"id":"newsfeed"})
    news= new_section.find_all("div", {"class":"news-individual"})
    for new in news:
        name= new.a["title"]
        names.append(name)
        url=new.a["href"]
        urls.append(url)

    return urls, names

def content_article(url, file_output):
    """scrapp content  web page in a file and the plain code

       url : adress web page of federation internationnale of badminton
       file_output : file name created + file name plain

       return two files : file with htlm code and file with only text informations
       """
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    plain_soup = soup.encode("UTF-8")
    section = soup.find_all("p")
    print(section)
    result=""
    for paragraphe in section:
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

