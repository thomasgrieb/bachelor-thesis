
import Constants as const
import Tools

'''
Parser-Programm, das über alle Rohdateien iteriert und den Titel sowie die ersten 400 Zeichen kopiert. \n
Wenn ein Artikel-Beginn-Markup gefunden wird, wird die nächste Zeile als Titel verwendet und die weiteren Zeilen
 gelesen \n
Wenn ein _NOTOC_ Markup gefunden wird, wird der Artikel  \n
&amp wird zu & korrigiert \n
Speichert die gekürzten Artikel am Ende wieder in einen neuen Ordner ab
'''

'''Instanzvariablen'''
title=""

filelist = Tools.get_files(const.SOURCE_FOLDER)  # Alle wikifiles AA bis AZ

'''loops through all files in filelist '''
'''Checks for Markups'''
for filename in filelist:
    file = open(const.SOURCE_FOLDER + const.FILE_OPERATOR + filename, "r", encoding=const.ENCODING)
    ignore_lines=False
    doc_dict = {}
    text=""
    eoa = False

    for line in file:

        if len(line.strip()) < 1:
            continue

        elif line.startswith(const.DOC_START_OPERATOR):
            ignore_lines = False
            nextline = next(file)
            title = nextline.strip("\n")
            title = title.replace("&amp;","&")

            continue

        if line.strip() == const.NO_ARTICLE_OPERATOR:
            ignore_lines = True
            continue

        elif line.startswith(const.DOC_END_OPERATOR):
            if len(text) > 0:
                doc_dict[title] = text
                text = ""
            continue


        if not ignore_lines:
            line = line.replace("\n", " ")
            text_len = len(text)
            if text_len < const.CHARS_FROM_ARTICLE:
                if text_len+len(line) < const.CHARS_FROM_ARTICLE:
                    text += line
                else:
                    text += line[0:const.CHARS_FROM_ARTICLE-text_len]
                text_len = len(text)
            elif text_len == const.CHARS_FROM_ARTICLE or eoa:
                ignore_lines = True

    file.close()
    Tools.dict_to_json_file(doc_dict,filename,const.INTRO_FOLDER_CHEAP, const.FILETAG_INTRO, "txt")
    print(filename+" done")



