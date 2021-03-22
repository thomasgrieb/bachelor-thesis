import Constants as const
import json


'''
Main - Nutzt die bestehenden Genre-Daten aus  movieGenre.json zur Erstellung eines Genre-Lexikons \n
Entfernt alle Filmtypen per Abgleich mit der entsprechenden Datei

'''
genre_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_MOVIEGENRE_FILE+const.ENDING_JSON,"r",encoding=const.ENCODING)
genre_out = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"genre"+const.ENDING_DIC,"w",encoding=const.ENCODING)

type_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"movietype"+const.ENDING_DIC,"r",encoding=const.ENCODING)
types =[ftype.split("\t")[0].strip("\n") for ftype in type_file]
type_file.close()

genre_dict = json.load(genre_file)
genre_list = []

for genre, obj  in genre_dict.items():
    genre_list.append(genre)
    for key, value in obj.items():
        for elem in value:
            genre_list.append(elem)

genre_out = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"genre.dic","w",encoding=const.ENCODING)
genre = []
for entry in genre_list:
    if entry in types:
        continue
    genre_out.write(entry+"\t"+const.GENRE_MARKUP_L+entry+const.GENRE_MARKUP_R+"\n")

genre_file.close()
genre_out.close()
