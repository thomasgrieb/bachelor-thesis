import Constants as const
import subprocess
import json

'''
Dieses Programm wendet automatisch die mittels plmlm-Technik erstellten Ersetzungstransducer auf die angegeben
 Texte an und bereinigt überflüssige Titel-Markierungen nach dem Titel-Transducer. Außerdem werden zu Beginn noch alle
 Artikel, die nicht in der gesäuberten Filmliste (movielist_cut.txt) stehen aus der Datei geworfen.
'''

title_ann = "title_annotation"
genre_ann = "genre_annotation"
nation_ann = "nation_annotation"
type_ann = "type_annotation"
year_ann = "year_annotation"

plmlm_a = "plmlm apply"


def process_entry(todo,transduc, input, output):
    return subprocess.check_output(const.TOOL_FOLDER + const.FILE_OPERATOR + todo + " " + const.TRANSDUCER_FOLDER +
                                   const.FILE_OPERATOR + transduc + const.ENDING_TR + " " + const.RESOURCE_FOLDER +
                                   const.FILE_OPERATOR + input + const.ENDING_JSON + " " + const.RESOURCE_FOLDER +
                                   const.FILE_OPERATOR + output + const.ENDING_JSON , shell=True,
                                   encoding=const.ENCODING)

raw_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_RAW_FILE+const.ENDING_JSON,"r",
                  encoding=const.ENCODING)
intro_dict = json.load(raw_file)
raw_file.close()

movies_file=open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"movielist_cut"+const.ENDING_TXT,"r",encoding=const.ENCODING)
movies = [movie.strip() for movie in movies_file if movie[0] != "#"]
movies_file.close()

intro_dict_n = {}

for key, value in intro_dict.items():
    if key in movies:
        intro_dict_n[key]=value

ann_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_ANN_FILE+const.ENDING_JSON,"w",
                  encoding=const.ENCODING)
json.dump(intro_dict_n, ann_file, indent=4, ensure_ascii=False)
ann_file.close()


process_entry(plmlm_a, title_ann, const.JSON_ANN_FILE, const.JSON_ANN_FILE)

an_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_ANN_FILE+const.ENDING_JSON,"r",
                  encoding=const.ENCODING)
intro_dict = json.load(an_file)
an_file.close()

for key, value in intro_dict.items():
    if const.TITLE_MARKUP_R not in value:
        continue
    value_left=value[0:value.index(const.TITLE_MARKUP_R)+len(const.TITLE_MARKUP_R)]
    value_right=value.split("</TITLE>",1)[1]
    value_right_new = value_right.replace("<TITLE>","").replace("</TITLE>","")
    new_value = value_left+value_right_new
    intro_dict[key] = new_value


an_file_clean = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_ANN_FILE+const.ENDING_JSON,"w",
                  encoding=const.ENCODING)
json.dump(intro_dict, an_file_clean, indent=4, ensure_ascii=False)
an_file_clean.close()

process_entry(plmlm_a, genre_ann, const.JSON_ANN_FILE, const.JSON_ANN_FILE)
process_entry(plmlm_a, nation_ann, const.JSON_ANN_FILE, const.JSON_ANN_FILE)
process_entry(plmlm_a, year_ann, const.JSON_ANN_FILE, const.JSON_ANN_FILE)
process_entry(plmlm_a, type_ann, const.JSON_ANN_FILE, const.JSON_ANN_FILE)


