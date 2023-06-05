import usual_function
import re
import os
import french.athletisme
import french.aviron
import french.basket
import french.bmxFreestyle
import french.breaking
import french.canoe
import french.cyclismepiste
import french.cyclismeroute
import french.escalade
import french.escrime
import french.football
import french.golf
import french.gymnastiqueartistique
import french.gymnatisquerythmique
import french.halterophilie
import french.handball
import french.hockey
import french.judo
import french.lutte
import french.natation
import french.natation_artistique
import french.marathon_natation
import french.pentathlon
import french.plongeons
import french.rugby
import french.sportsequestres
import french.surf
import french.tennis
import french.tennistable
import french.tir
import french.tiralarc
import french.trampoline
import french.triathlon
import french.voile
import french.volleyball
import french.vtt
import french.waterpolo
import french.scrapp_generalites
import french.boxe


FRENCH_FILE_PATH="C:/Users/la5794ma/OneDrive - Université de Bourgogne/Documents/PNR/" \
                   "Jeux Olympiques/decembre/français"
LIST_OLYMPICS_GAMES= ['Athletisme', 'aviron', 'badminton', 'basketball', 'basketball3×3',
                      'boxe', 'canoe', 'canoe' , 'canoe','cyclisme-sur-piste', 'cyclisme-sur-route',
                      'BMX-freestyle', 'BMX-racing', 'vtt',  'escrime', 'football', 'golf',
                      'gymnastique-artistique', 'gymnastique-rythmique', 'trampoline',
                      'halterophilie', 'handball', 'hockey', 'judo', 'lutte',
                      'pentathlon-moderne', 'rugby', 'natation', 'natation-artistique',
                      'natation-marathon', 'plongeon', 'waterpolo', 'sports-equestres',
                      'taekwondo',  'tennis', 'tennis-de-table', 'tir', 'tir-a-l-arc',
                      'triathlon', 'voile', 'volleyball', 'volleyball-de-plage', 'Breaking',
                      'escalade-sportive', "skateboard"]

# For generalites


#for url, name in zip(urls,LIST_OLYMPICS_GAMES):
 #   usual_function.scrap_paragraphs(url, FRENCH_FILE_PATH +"/"+name+"/generalities.txt",
  #                                  FRENCH_FILE_PATH+"/"+name+"/generalities_plain.txt")

# Athletisme

#usual_function.scrapper_french("Athletisme",french.athletisme.pick_adress_sport_pages)

# Aviron

#print(" Pour aviron")

#usual_function.scrapper_french("aviron",french.aviron.pick_adress_sport_pages)

# Basket 16 links

#usual_function.scrapper_french_with_specific_function("basketball",
 #                                                     french.basket.pick_adress_sport_pages,
  #                                                    french.basket.scrapp_paragraph)

# Bmx_freestyle 16 links

#usual_function.scrapper_french("BMX-freestyle",french.bmxFreestyle.pick_adress_sport_pages)


# Boxe 18 links

usual_function.scrapper_french("boxe",french.boxe.pick_adress_sport_pages)

# breaking 12 links

#usual_function.scrapper_french("breaking",french.breaking.pick_adress_sport_pages)



# Canoe

#usual_function.scrapper_french("canoe",french.canoe.pick_adress_sport_pages)

# Cyclisme sur Piste 24 links

#usual_function.scrapper_french("cyclisme-sur-piste",french.cyclismepiste.pick_adress_sport_pages)


# Cyclisme sur Route 24 links

#usual_function.scrapper_french("cyclisme-sur-route",french.cyclismeroute.pick_adress_sport_pages)


# Escalade

#usual_function.scrapper_french("escalade-sportive",french.escalade.pick_adress_sport_pages)

# Escrime

#usual_function.scrapper_french("escrime",french.escrime.pick_adress_sport_pages)

# Football 20 links

usual_function.scrapper_french("football",french.football.pick_adress_sport_pages)


# Golf

#usual_function.scrapper_french("golf", french.golf.pick_adress_sport_pages)

# Gynm artistique

#usual_function.scrapper_french("gymnastique-artistique",french.gymnastiqueartistique.pick_adress_sport_pages)

# Gymn rythmique

#usual_function.scrapper_french("gymnastique-rythmique",french.gymnatisquerythmique.pick_adress_sport_pages)

# halterophilie

#usual_function.scrapper_french(("halterophilie"),french.halterophilie.pick_adress_sport_pages)

# handball 6 links ( necessary selenium)

#usual_function.scrapper_french("handball",french.handball.pick_adress_sport_pages)

# Hockey 18 links

#usual_function.scrapper_french("hockey",french.hockey.pick_adress_sport_pages)


# Judo 18 links

#usual_function.scrapper_french("judo",french.judo.pick_adress_sport_pages)

# Lutte 20 links

#usual_function.scrapper_french("lutte",french.lutte.pick_adress_sport_pages)

# Natation 6 links

#usual_function.scrapper_french("natation",french.natation.pick_adress_sport_pages)

# Natation artistique 6 links

#usual_function.scrapper_french("natation-artistique",french.natation_artistique.pick_adress_sport_pages)

# Natation Marathon 6 links

#usual_function.scrapper_french("natation-marathon", french.marathon_natation.pick_adress_sport_pages)

# Pentathlon moderne 14 Links

#usual_function.scrapper_french("pentathlon-moderne", french.pentathlon.pick_adress_sport_pages)

# Plongeons 6 links

#usual_function.scrapper_french("plongeon", french.plongeons.pick_adress_sport_pages)

# Rugby

#usual_function.scrapper_french("rugby",french.rugby.pick_adress_sport_pages)

# Sports equestres

#usual_function.scrapper_french("sports-equestres",french.sportsequestres.pick_adress_sport_pages)

# Surf

#usual_function.scrapper_french("surf",french.surf.pick_adress_sport_pages)

# Tennis ( 2 pages changer l'url dans fonction )

#usual_function.scrapper_french("tennis",french.tennis.pick_adress_sport_pages)

# Tennis de table

#usual_function.scrapper_french("tennis-de-table",french.tennistable.pick_adress_sport_pages)

# tir

#usual_function.scrapper_french("tir",french.tir.pick_adress_sport_pages)

# tir à l arc 24 links

#usual_function.scrapper_french("tir-a-l-arc",french.tiralarc.pick_adress_sport_pages)

# Trampoline

#usual_function.scrapper_french("trampoline",french.trampoline.pick_adress_sport_pages)

# Triathlon

#usual_function.scrapper_french("triathlon",french.triathlon.pick_adress_sport_pages)

# Voile 10 Links

#usual_function.scrapper_french("voile",french.voile.pick_adress_sport_pages)

# Volleyball 20 links

#usual_function.scrapper_french_with_specific_function("volleyball",
#                                                     french.volleyball.pick_adress_sport_pages,
 #                                                     french.volleyball.scrapp_paragraph)

# VTT 24 links

#usual_function.scrapper_french("VTT",french.vtt.pick_adress_sport_pages)

# Waterpolo 6 links

#usual_function.scrapper_french("waterpolo",french.waterpolo.pick_adress_sport_pages)