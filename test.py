import usual_function
import os
import re
import french.skateboard
import french.scrapp_generalites
import french.boxe
import french.football

FRENCH_FILE_PATH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                      "Jeux Olympiques/decembre/français/"

PATH_FILE_ENGLISH= "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                   "Jeux Olympiques/decembre/anglais/"

SPANISH_FILE_PATH = "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                  "Jeux Olympiques/decembre/espagnol"


url = "https://www.ffboxe.com/kevin-lele-sadjo-toujours-mieux/"

#french.skateboard.scrapp_paragraph(url, FRENCH_FILE_PATH+"/skateboard/test.txt",
                         #      FRENCH_FILE_PATH+"/skateboard/test_plain.txt")

#usual_function.scrap_paragraphs(url,FRENCH_FILE_PATH+"boxe/test3.txt",
 #     FRENCH_FILE_PATH+"boxe/test_plain3.txt")

#french.badminton.scrapp_paragraph(url,FRENCH_FILE_PATH+"/ba/test.txt",
 #                                FRENCH_FILE_PATH+"/badminton/test_plain.txt")
#

urls, names = french.football.pick_adress_sport_pages()
usual_function.print_var(urls)
usual_function.print_var(names)
#for url in urls :
 #   print ("url :",url)
