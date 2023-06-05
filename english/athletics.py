from bs4 import BeautifulSoup as bs
import usual_function
import requests
import re

def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source(
        "https://worldathletics.org/news/press-releases")
    soup = bs(page_source, 'html.parser')
    section = soup.find("section", {"class" : "PageContent_pageContent__pFSwB"})
    links=section.find_all("div",{"class":"NewsItem_content__1G-Ov"})

    urls=[]
    names=[]
    for link in links :
        name= link.a.h3.text
        name = re.sub(" ", "-", name)
        name = re.sub(":", "", name)
        name = re.sub("[\'\"?]","",name)
        names.append(name)
        url_plain = link.a['href']
        url = "https://worldathletics.org"+ url_plain
        urls.append(url)
    return urls, names

def content_article(url, file_output):
    """scrapp content  web page in a file and the plain code

       url : adress web page of federation internationnale of athletics
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

