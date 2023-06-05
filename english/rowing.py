from bs4 import BeautifulSoup as bs
import usual_function
import requests
import re



def pick_adress_sport_pages() :
    """ pick the adress of the web pages of sports
    :return: a list with the url's page
    """
    page_source = usual_function.get_page_source("https://worldrowing.com/news")
    soup = bs(page_source, 'html.parser')
    section = soup.find("div", {"id" : "aggregator"})
    items=section.find_all("article", {"class":"news-card mx-1 mb-2"})
    urls=[]
    names=[]
    for item in items:
        name= item.h2.text
        name = re.sub("\s{2,} ", " ", name)
        name = re.sub(":", "", name)
        name = re.sub("[/]",'-',name)
        names.append(name)
        url_plain= item.a["href"]
        url = "https://worldrowing.com"+url_plain
        urls.append(url)

    return urls, names

def content_article(url, file_output):
    """scrapp content  web page in a file and the plain code

       url : adress web page of federation internationnale of rowing
       file_output : file name created + file name plain

       return two files : file with htlm code and file with only text informations
       """
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    plain_soup = soup.encode("UTF-8")
    section = soup.find("section", {"class":"content my-0"})
    paragraphes = section.find_all("p")
    result=""
    for paragraphe in paragraphes:
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

