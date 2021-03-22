import json
import Constants as const
import re
import Tools

'''
Klassifikator - Entscheidet, ob ein Artikel zu einem Film gehört oder nicht, checkt dafür 4 Komponenten und berechnet 
einen Score. Erstellt dann Datei mit allen Film-Artikeln und extra Liste mit den Titeln.
'''

'''Instanzvariablen'''

filelist = Tools.get_files(const.INTRO_FOLDER_CHEAP)
date_reg = re.compile(const.NUMBER_REGEX)
year_reg = re.compile(const.YEAR_REGEX)
genre_reg = re.compile(const.REGEX_GENRE_FILM)
movie_list = []

#Genre-Dictionary
genre_file = open(const.RESOURCE_FOLDER + const.FILE_OPERATOR + const.JSON_MOVIEGENRE_FILE + const.ENDING_JSON, "r",
                  encoding=const.ENCODING)
genre_dict = json.load(genre_file)
genre_file.close()

#Buzzword-Dictionary
buzz_file = open(const.RESOURCE_FOLDER + const.FILE_OPERATOR + const.JSON_BUZZWORD_FILE + const.ENDING_JSON, "r",
                 encoding=const.ENCODING)
buzz_dict = json.load(buzz_file)
buzz_file.close()


'''
Takes normalized values (list of lowercase tokens) and checks for mentions of Genres from the movieGenre_old.json file \n
Disambiguates whether genre is unambiguous or not (does it include the string "film" or "Film"?)
Each entry in movieGenre_old.json consists of 3 entries itself: \n
Genre: String, the name of the genre \n
Subgenres: List of Strings, a list of possible subgenres \n
Alt: List of Strings, a list of possible alternative names or common abbreviations for the (sub-)genre(s) \n
Returns 1.5 is unambiguous, 1 if not
'''

def check_for_genre(token_list):
    for key, value_dict in genre_dict.items():
        if key.lower() in token_list:
            if re.search(genre_reg, key.lower()) != None:
                return 1.5
            else:
                return 1
        for key_d,value_d in value_dict.items():
            for elem in value_d:
                if elem.lower() in token_list:
                    if re.search(genre_reg, elem.lower()) != None:
                        return 1.5
                    else:
                        return 1
    return 0


'''
Takes json-entry and checks its key (=title) for the Wikipedia Movie-Marker \"(Film)\" \n
Returns 1 if one is found, else 0 \n
Also checks if a genre-title matches the title, indicating an article about the genre \n
Returns -10 if yes
'''

def check_title(entry_key):
    if re.search(const.REGEX_FILM_MARKUP_TITLE, entry_key) != None:
        return 1
    for key, value_dict in genre_dict.items():
        if key.lower() == entry_key.lower():
            return -10
        for key_d, value_d in value_dict.items():
            for elem in value_d:
                if elem.lower() == entry_key.lower():
                    return -10
    else:
        return 0


'''
Takes normalized values (list of lowercase tokens) and checks for mentions of buzzwords from the movieVocab.json
file. \n
Buzzwords are words that appear in many movie-articles. The file consists of several categories of buzzwords,
each of which contain a list of entries, where the key is the word and the value a score which indicates estimated 
importance. \n
Returns sum of scores
'''

def check_for_buzzwords(token_list):
    score = 0
    for key, value_dict in buzz_dict.items():
        for key_d,value_d in value_dict.items():
            occ_count=token_list.count(key_d.lower())
            if occ_count > 0:
                score += (value_d*occ_count)

    return score


'''
Takes normalized values (list of lowercase tokens) \n
Checks, if article is likely to be that of on actor by searching for a birth-marker (*[date]) in the first 20 tokens \n
Token-sequence = ...,[(],[*],[day],[month],[year], ...
Returns -1 if birth-marker is found, 0 if not, 0.25 if just year beginning with 18/19/20 is found (often release year)
'''

def check_if_actor_or_date(token_list):
    bracket = False
    star = False

    for token in token_list:
        if bracket == False and token == '(':
            bracket = True
            continue
        if bracket == True and token == ')':
            bracket = False
            continue
        if bracket == True and token == '*':
            star = True
            continue
        if star == True and date_reg.match(token):
            return -1.0
        else:
            star = False
        if bracket == False and year_reg.match(token):
            return 0.25
    return 0.0





'''main'''

movie_dict = {}

for filename in filelist:
    json_file = open(const.INTRO_FOLDER_CHEAP+const.FILE_OPERATOR+filename, "r", encoding=const.ENCODING)
    json_dict = json.load(json_file)
    json_file.close()

    for key, value in json_dict.items():
        in_title = check_title(key)
        normalized_text = Tools.normalize_text(value)
        genre = check_for_genre(normalized_text)
        buzzwords_score = check_for_buzzwords(normalized_text)
        actor = check_if_actor_or_date(normalized_text)

        score = Tools.calculate_movie_liklihood(in_title, genre, buzzwords_score, actor)
        if score >= const.MIN_MOVIE_SCORE:
            movie_list.append(key)
            movie_dict[key] = value

    print(filename+" done\n")


Tools.dict_to_json_file(movie_dict,"movie_intros.json","Ressourcen","","json")
outfile = open("movielist","w",encoding=const.ENCODING)
for elem in movie_list:
    outfile.write(elem+"\n")
outfile.close()
