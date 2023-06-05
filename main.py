import especialesmarca
import english.gymnastique
import english.fencing
import english.athletics
import english.basket
import english.badminton
import english.boxe
import english.canoe
import english.escalade
import english.football
import english.golf
import english.gymnastique
import english.gymnastique_rythmique
import english.cyclismepiste
import english.halterophilie
import english.handball
import english.hockey
import english.judo
import english.lutte
import english.natation
import english.natation_artistique
import english.plongeon
import english.skateboard
import english.surf
import english.taekwondo
import english.table_tennis
import english.tir
import english.tiralarc
import english.trampoline
import english.triathlon
import english.voile
import english.volleyball
import english.vtt
import english.waterpolo
import usual_function

LISTE_URLS_ARTICLES_GENERALS_OLYMPICSDOTCOM= ["https://olympics.com/en/sports/athletics",
                                            "https://olympics.com/en/sports/rowing/",
                                            "https://olympics.com/en/sports/badminton/",
                                            "https://olympics.com/en/sports/basketball/",
                                            "https://olympics.com/en/sports/cycling-bmx-freestyle/",
                                            "https://olympics.com/en/sports/cycling-bmx-racing/",
                                            "https://olympics.com/en/sports/boxing/",
                                            "https://olympics.com/en/sports/breaking/",
                                            "https://olympics.com/en/sports/canoe-kayak-flatwater/",
                                            "https://olympics.com/en/sports/cycling-road/",
                                            "https://olympics.com/en/sports/cycling-track/",
                                             "https://olympics.com/en/sports/sport-climbing/",
                                            "https://olympics.com/en/sports/fencing/",
                                            "https://olympics.com/en/sports/football/",
                                            "https://olympics.com/en/sports/golf/",
                                            "https://olympics.com/en/sports/artistic-gymnastics/",
                                            "https://olympics.com/en/sports/rhythmic-gymnastics/",
                                            "https://olympics.com/en/sports/weightlifting/",
                                            "https://olympics.com/en/sports/handball/",
                                            "https://olympics.com/en/sports/hockey/",
                                            "https://olympics.com/en/sports/judo/",
                                            "https://olympics.com/en/sports/wrestling/",
                                            "https://olympics.com/en/sports/swimming/",
                                            "https://olympics.com/en/sports/artistic-swimming/",
                                            "https://olympics.com/en/sports/marathon-swimming/",
                                            "https://olympics.com/en/sports/modern-pentathlon/",
                                            "https://olympics.com/en/sports/diving/",
                                            "https://olympics.com/en/sports/rugby-sevens/",
                                            "https://olympics.com/en/sports/skateboarding/",
                                            "https://olympics.com/en/sports/equestrian/",
                                            "https://olympics.com/en/sports/surfing/",
                                            "https://olympics.com/en/sports/taekwondo/",
                                            "https://olympics.com/en/sports/tennis/",
                                            "https://olympics.com/en/sports/table-tennis/",
                                            "https://olympics.com/en/sports/shooting/",
                                            "https://olympics.com/en/sports/archery/",
                                            "https://olympics.com/en/sports/trampoline-gymnastics/",
                                            "https://olympics.com/en/sports/triathlon/",
                                            "https://olympics.com/en/sports/sailing/",
                                            "https://olympics.com/en/sports/beach-volleyball/",
                                            "https://olympics.com/en/sports/volleyball/",
                                            "https://olympics.com/en/sports/water-polo/",
                                            "https://olympics.com/en/sports/cycling-mountain-bike/"]

PATH_FILE_ENGLISH= "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                   "Jeux Olympiques/decembre/anglais"
PATH_FILE_SPANISH= "C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/Jeux Olympiques/decembre/espagnol/"

OTHERS_URLS=["https://olympics.com/en/sports/canoe-kayak-slalom/","https://olympics.com/en/sports/futsal/" ]

NAME_SPORT_TO_OTHER=["canoe","football"]

FRENCH_NAME_SPORT= [ "Athletisme", "aviron", "badminton", "basketball", "BMX-freestyle",
                     "BMX-racing", "boxe", "Breaking", "canoe", "cyclisme-sur-route", "cyclisme-sur-piste",
                     "escalade-sportive",
                     "escrime", "football", "golf", "gymnastique-artistique", "gymnastique-rythmique",
                     "halterophilie", "handball", "hockey", "judo", "lutte", "natation",
                     "natation-artistique", "natation-marathon", "pentathlon-moderne",
                     "plongeon", "rugby", "skateboard", "sports-equestres", "surf", "taekwondo",
                     "tennis", "tennis-de-table", "tir", "tir-a-l-arc", "trampoline", "triathlon",
                     "voile", "volleyball-de-plage", "volleyball", "waterpolo", "VTT"]



"""
for url,sport_name in zip(LISTE_URLS_ARTICLES_GENERALS_OLYMPICSDOTCOM,FRENCH_NAME_SPORT):
   scrapp_article_content_OlympicDotCom(url,PATH_FILE_ENGLISH+sport_name+"/generalite_olympicsdotcom")

for url,sport_name in zip(OTHERS_URLS,NAME_SPORT_TO_OTHER) :
    scrapp_article_content_OlympicDotCom(url,
                                         PATH_FILE_ENGLISH + sport_name + "/generalite_olympicsdotcom")
"""

"""
# Scrapp documents from the site Olympics.com ( doc in English) 
for sport, name_sport in zip(LISTE_URLS_ARTICLES_GENERALS_OLYMPICSDOTCOM, FRENCH_NAME_SPORT) :
    urls,names_articles=scrapp_url_articles(sport)
    for url, name in zip(urls,names_articles):
        print (url)
        try :
            content_article(url, PATH_FILE_ENGLISH+name_sport+"/"+name)
        # if no paragrafe in the web page
        except UnboundLocalError:
            continue
        except FileNotFoundError:
            continue
        # if the section doesn't exists
        except AttributeError :
            continue
        except OSError:
            name_modify=re.sub( "[\?\|]+", "_", name)
            print(name_modify)
            try :
                content_article(url, PATH_FILE_ENGLISH + name_sport + "/" + name_modify)
            except UnboundLocalError:
                continue

"""
"""
urls_athletics, names_athletics = english.athletics.pick_adress_sport_pages()

usual_function.print_var(urls_athletics)
usual_function.print_var(names_athletics)


#english.athletics.content_article("https://worldathletics.org/competitions/"
 #                                 "world-athletics-indoor-tour/news/karlsruhe-kambundji-60m"
  #                                "-bekh-romanchuk-mamona-triple-jump", PATH_FILE_ENGLISH+"/Athletisme/karl")
"""


"""
english.gymnastique.content_article(
    "https://www.gymnastics.sport/site/news/displaynews.php?urlNews=3731481",
    PATH_FILE_ENGLISH+"Gymnastique-artistique/new_order_aerobic")
"""
# BATMINTON OK
"""

usual_function.scrapper_english("badminton",english.badminton.pick_adress_sport_pages,
                                english.badminton.content_article)
"""
# BASKET

##usual_function.scrapper_english("basketball",english.basket.pick_adress_sport_pages,
    #                            english.basket.content_article)

## Boxe

#usual_function.scrapper_english("boxe",english.boxe.pick_adress_sport_pages,english.boxe.content_article)

# Canoe

# ESCALADE

#usual_function.scrapper_english("escalade-sportive",english.escalade.pick_adress_sport_pages)

# CYCLISME

# SUR ROUTE
#usual_function.scrapper_english("cyclisme-sur-route",english.cyclisme.pick_adress_road_cycling)

# Sur piste

#usual_function.scrapper_english("cyclisme-sur-piste",english.cyclisme.pick_adress_track_cycling)

# Golf

usual_function.scrapper_english("golf",english.golf.pick_adress_sport_pages)


# Gynm_artistique

#usual_function.scrapper_english("gymnastique-artistique",english.gymnastique.pick_adress_sport_pages)

#Gymnastique rytfhmique

#usual_function.scrapper_english("gymnastique-rythmique", english.gymnastique_rythmique.
 #                               pick_adress_sport_pages)

# Football

#usual_function.scrapper_english("football", english.football.pick_adress_sport_pages,
#                                usual_function.scrap_paragraphs)

# Haterophilie

#usual_function.scrapper_english_with_specific_function("halterophilie",
  #                                                     english.halterophilie.pick_adress_sport_pages,
   #                                                    english.halterophilie.pick_paragraph)

# Handball

#usual_function.scrapper_english("handball",english.handball.pick_adress_article)

# Hockey

#usual_function.scrapper_english("hockey",english.hockey.pick_adress_article)

# Judo

#usual_function.scrapper_english("judo",english.judo.pick_adress_sport_pages)

# Lutte

#usual_function.scrapper_english("lutte", english.lutte.pick_adress_sport_pages)

# Natation

#usual_function.scrapper_english("natation", english.natation.pick_adress_sport_pages)

# Natation artistique

#usual_function.scrapper_english("natation-artistique", english.natation_artistique.pick_adress_sport_pages)


# Plongeon

#usual_function.scrapper_english("plongeon", english.plongeon.pick_adress_sport_pages)

# Skateboard

#usual_function.scrapper_english("skateboard",english.stakeboard.pick_adress_sport_pages)

# Surf

#usual_function.scrapper_english("surf",english.surf.pick_adress_sport_pages)

# Taekwondo

#usual_function.scrapper_english("taekwondo", english.taekwondo.pick_adress_sport_pages)

# table tennis

#usual_function.scrapper_english("tennis-de-table",english.table_tennis.pick_adress_sport_pages)


# tir

#usual_function.scrapper_english("tir",english.tir.pick_adress_sport_pages)

# tir a larc

#usual_function.scrapper_english("tir-a-l-arc",english.tir_a_l_arc.pick_adress_sport_pages)

# trampoline

#usual_function.scrapper_english("trampoline", english.trampoline.pick_adress_sport_pages)

# Triathlon

#usual_function.scrapper_english("triathlon",english.triathlon.pick_adress_sport_pages)

#  Voile

#usual_function.scrapper_english("voile", english.voile.pick_adress_sport_pages)

# Volleyball and Beach Volley

#usual_function.scrapper_english("volleyball",english.volleyball.pick_adress_sport_pages)

# VTT

#usual_function.scrapper_english("VTT",english.vtt.pick_adress_cycling)


# Waterpolo

#usual_function.scrapper_english("waterpolo",english.waterpolo.pick_adress_sport_pages)
""""
urls_fencing,names_fencing = english.fencing.pick_adress_sport_pages()
print("urls_fencing : ",len(urls_fencing)," ",urls_fencing)
print("names_fencing ", len(names_fencing)," ",names_fencing)

for url,name in zip(urls_fencing,names_fencing):
    english.fencingcontent_article("https://fie.org/articles/1244",PATH_FILE_ENGLISH+
                                   "/escrime/"+name)
"""

######################## For langage spanish

## Scrapp a generality's page for each sport
"""
URLS_SPANISH_GENERALITE_ESPECIALESMARCAS,SPANISH_NAMES=especialesmarca.pick_adress_sport_pages()

print ( "URLS_SPANISH_GENERALITE : ", URLS_SPANISH_GENERALITE_ESPECIALESMARCAS)
"""


"""
# create text file with sports' names in spanish
url="C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/Jeux " \
    "Olympiques/decembre/outils/"
file = open(url, 'w', encoding="utf_8")
for sport in SPANISH_NAMES:
    file.write(sport+"\h")
file.close()
"""

"""
for url, name_sport in zip(URLS_SPANISH_GENERALITE,FRENCH_NAME_SPORT):
    especialesmarca.scrapp_article_content_especialesmarca(url,PATH_FILE_SPANISH+name_sport+"/generalites)")

"""

# Scrap a generality  site protected --> impossible to scrap
"""
URLS_GENERALITE_MIS_JUEGOS = otrossitio.pick_adress_sport_pages()
print(URLS_GENERALITE_MIS_JUEGOS)
print(len(URLS_GENERALITE_MIS_JUEGOS))
"""
"""
otrossitio.scrapp_article_content_concepto("https://concepto.de/atletismo/",PATH_FILE_SPANISH+"athletisme/generalites_concepto")
otrossitio.scrapp_article_content_concepto("https://concepto.de/baloncesto/",PATH_FILE_SPANISH+"basket/generalite_concepto")
otrossitio.scrapp_article_content_concepto("https://concepto.de/gimnasia/",PATH_FILE_SPANISH+"gymnastique-artistique/generalites-concepto")
otrossitio.scrapp_article_content_concepto("https://concepto.de/voleibol/",PATH_FILE_SPANISH+"volley/generalites-concepto")
"""