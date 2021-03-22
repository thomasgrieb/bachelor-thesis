'''
Konstanten
Hier sind alle Konstanten gespeichert. Die meisten Dateipfade sind hier festgelegt. Wenn Dateien oder Ordner verschoben
werden, ist die Anpassung der entsprechenden Konstanten hier wichtig, damit die Programme weiterhin laufen.
'''

''' File constants '''

SOURCE_FOLDER = "WikiFiles"
INTRO_FOLDER = "wiki_intros"
INTRO_FOLDER_CHEAP = "wiki_intros_cheap"
INTRO_FOLDER_MOVIES = "wiki_movie_intros"
RESOURCE_FOLDER = "Ressourcen"
TOOL_FOLDER = "Tools"
TRANSDUCER_FOLDER = "Transducer"
JSON_MOVIEGENRE_FILE = "movieGenre"
JSON_BUZZWORD_FILE = "movieVocab"
INPUT = "999_1200"
JSON_RAW_FILE = "movie_"+INPUT
JSON_ANN_FILE = "movie_"+INPUT+"_pre"
JSON_CLEAN_ANN_FILE = "movie_"+INPUT+"_clean"
RELATIONS_FILE = "movie_relations_"+INPUT
RELATIONS_EMPTY = "N/A"
ENDING_TXT = ".txt"
ENDING_JSON = ".json"
ENDING_DIC = ".dic"
ENDING_TR = ".tr"
FILETAG_INTRO = "intro_"
FILETAG_MOVIE = "mov_"
STAT_FILE = "stats.json"
FILE_OPERATOR = "/"
DOC_START_OPERATOR = "<doc"
DOC_END_OPERATOR = "</doc>"
ENCODING = 'utf-8'
NO_ARTICLE_OPERATOR = "__NOTOC__"
YEAR_MARKUP_L = "<YEAR>"
YEAR_MARKUP_R = "</YEAR>"
GENRE_MARKUP_L = "<GENRE>"
GENRE_MARKUP_R = "</GENRE>"
TITLE_MARKUP_L = "<TITLE>"
TITLE_MARKUP_R = "</TITLE>"
TYPE_MARKUP_L = "<FILMTYPE>"
TYPE_MARKUP_R = "</FILMTYPE>"
NATION_MARKUP_L = "<NAT>"
NATION_MARKUP_R = "</NAT>"
RELATION_SEPERATOR = "|"
LANGUAGE = 'german'
TREE_LANGUAGE= 'de'
MAX_TOKENS_FOR_HEADER = 12
MAX_TOKENS_FOR_DATE = 50
MAX_CHARS_FOR_INTRO = 300
CHARS_FROM_ARTICLE = 400
ACC_FP = "fp"
ACC_TP = "tp"
ACC_FN = "fn"
ACC_FE = "fe"
ACC_TN = "tn"

'''Regex'''

REGEX_POS_VERB_TAG = "^V"
REGEX_FILM_MARKUP_TITLE = ".+\(Film\)$"
NUMBER_REGEX = "^\d+"
YEAR_REGEX = "^(18|19|20)\d{2}$"
REGEX_GENRE_FILM_HYPH = "-[Ff]ilm"
REGEX_GENRE_FILM = "\S+film$"

''' Math constants '''

MIN_MOVIE_SCORE = 2.1

'''OS Constants'''
EXECUTE_OPERATOR = "./"
