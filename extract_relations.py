import re
import Constants as const
import json

'''
Extrahiert die markierten Informationen und wandelt sie in fertige Relationsmengen um, die dann in eine Datei 
geschrieben werden. 
'''

an_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_CLEAN_ANN_FILE+const.ENDING_JSON,"r",
                  encoding=const.ENCODING)
an_dict = json.load(an_file)

out_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.RELATIONS_FILE+const.ENDING_TXT,"w",
                  encoding=const.ENCODING)

rel_list = []

reg_op = "(.+?)"
title_reg=re.compile(const.TITLE_MARKUP_L+reg_op+const.TITLE_MARKUP_R)
type_reg = re.compile(const.TYPE_MARKUP_L+reg_op+const.TYPE_MARKUP_R)
genre_reg = re.compile(const.GENRE_MARKUP_L+reg_op+const.GENRE_MARKUP_R)
nation_reg = re.compile(const.NATION_MARKUP_L+reg_op+const.NATION_MARKUP_R)
year_reg = re.compile(const.YEAR_MARKUP_L+reg_op+const.YEAR_MARKUP_R)
sep="|"


for key, value in an_dict.items():

    text = key+": "+value
    title = re.search(title_reg, text)
    if title:
        title = title.group(1)
    else:
        title = const.RELATIONS_EMPTY
    type = re.search(type_reg, text)
    if type:
        type = type.group(1)
    else:
        type = const.RELATIONS_EMPTY
    genres = re.findall(genre_reg, text)
    genre_l = []
    for elem in genres:
        elem=elem.strip("-")
        if elem[0].islower():
            first=elem[0].upper()
            elem=first+elem[1:]
        if elem not in genre_l:
            genre_l.append(elem)
    nation = re.search(nation_reg, text)
    if nation:
        nation = nation.group(1)
    else:
        nation = const.RELATIONS_EMPTY
    year = re.search(year_reg, text)
    if year:
        year = year.group(1)
    else:
        year = const.RELATIONS_EMPTY

    if len(genre_l)>0:
        genre = "/".join(genre_l[0:3]) #Nur erste 3 Genres
    else:
        genre = const.RELATIONS_EMPTY

    rel_list.append("<"+title+sep+type+sep+genre+sep+nation+sep+year+">")

for entry in rel_list:
    out_file.write(entry+"\n")