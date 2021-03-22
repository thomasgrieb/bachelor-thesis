import Constants as const
import re

'''
Programm zur Erstellung des Titellexikons aus der bereinigten Titelliste \n
Liest Liste ein, bereinigt Wikipedias Titelmarkierungen (Film, Jahreszahl, Anime), speichert Einträge in neuer Liste \n
Iteriert über neue Liste und checkt, ob der Titel einem Filmtyp entspricht oder schon in die Liste eingetragen wurde.
 Wenn nicht wird der Eintrag mit Markup ins Lexikon geschrieben
'''
movies_file=open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"movielist_cut"+const.ENDING_TXT,"r",encoding=const.ENCODING)
type_file=open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"movietype"+const.ENDING_DIC,"r",encoding=const.ENCODING)

types = [line.split("\t")[0] for line in type_file]
type_file.close()

movies =[]
double = []

film_markup = "\(.*[fF]ilm\)"
film_re = re.compile(film_markup)
year_markup ="\((18|19|20)\d{2}\)"
year_re = re.compile(year_markup)
anime_markup = "\(Anime\)"
anime_re = re.compile(anime_markup)
for title in movies_file:
    title = title.strip()
    title_n=title.strip()
    if len(title) > 1 and title[0] != "#":
        if "(" in title:
            title = re.sub(film_re,"", title)
            title = re.sub(year_re,"", title)
            title = re.sub(anime_re,"", title)
            title = title.strip()
            if len(title) > 1:
                movies.append(title)
        else:
            movies.append(title_n)

movies_out=open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"movies"+const.ENDING_DIC,"w",encoding=const.ENCODING)
for key in movies:
    if key in types or key in double:
        continue
    else:
        movies_out.write(key+"\t"+const.TITLE_MARKUP_L+key+const.TITLE_MARKUP_R+"\n")
        double.append(key)
movies_file.close()
movies_out.close()