import os
import json
import Constants as const
import nltk
import re

'''
Diverse Hilfsfunktionen
'''

genre = re.compile(const.REGEX_GENRE_FILM_HYPH)

'''Helper function, return total amounts of tokens of all sentences in line'''
'''Source: https://stackoverflow.com/questions/27761463/how-can-i-get-the-total-number-of-elements-in-my-arbitrarily-nested-list-of-list/27761524'''

def rec_len_list(tok_list):
    if type(tok_list) == list:
        return sum(rec_len_list(sent) for sent in tok_list)
    else:
        return 1


'''Collects all filenames from target-folder'''

def get_files(folder):
    files = []
    directory = os.fsencode(folder)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        files.append(filename)
    return sorted(files)


'''Prints Dict into json-file in pretty-print'''

def dict_to_json_file(dict_to_print, org_filename, outfolder, filetag, filetyp_input):
    if filetyp_input == "txt":
        filename_new = org_filename[0:-4]
    elif filetyp_input == "json":
        filename_new = org_filename[0:-5]
    else:
        raise Exception("Filetype not supported.")
    outfile_name = outfolder + const.FILE_OPERATOR + filetag + filename_new + const.ENDING_JSON
    outfile = open(outfile_name, "w", encoding=const.ENCODING)
    json.dump(dict_to_print, outfile, indent=4, ensure_ascii=False)
    outfile.close()


'''Takes String, normalizes Text by tokenizing, removing punctuation and setting lowercase'''

def normalize_text(text):
    text = text[0:min(const.MAX_CHARS_FOR_INTRO,len(text))]
    text = re.sub(genre," film", text)
    token_list = nltk.word_tokenize(text, language=const.LANGUAGE)
    lower_no_punct = [elem.lower() for elem in token_list]
    return lower_no_punct


'''Takes list of strings, joins entries into one long String'''
def join_string_list(string_list):
    full_text=""
    for elem in string_list:
        full_text=full_text+" "+elem
    return full_text


''' 
Formula for is_movie-score calculations \
Takes in_title (int) as first argument, genre_count (int) as second, buzzword_score (float) as third \n
Returns True if high enough (=is a movie article)
 '''

def calculate_movie_liklihood(in_title, genre_count, buzzword_score, actor):
    return in_title+genre_count+buzzword_score+(actor*2)