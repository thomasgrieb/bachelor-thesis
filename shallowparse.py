
import nltk
import treetaggerwrapper as tree
from collections import defaultdict
import re
import Constants as const
import Tools

'''Verworfener erster Parser'''

'''Instanzvariablen'''
title=""

'''Checks, if line is likely to be an article-headline.'''
'''Tokenizes the line, if number of tokens excedes specified constant, line is probably not a headline.'''
'''If not more than specified number of tokens, uses POS-Tagging to check for Verbs.
    No Verb means probably no headline.'''
'''Source: http://textmining.wp.hs-hannover.de/Preprocessing.html'''

def is_header(line):
    sentences = nltk.sent_tokenize(line, language=const.LANGUAGE)
    text_tok = [nltk.word_tokenize(sent, language=const.LANGUAGE) for sent in sentences]
    if Tools.rec_len_list(text_tok) > const.MAX_TOKENS_FOR_HEADER:
        return False
    tagger = tree.TreeTagger(TAGLANG=const.TREE_LANGUAGE)
    tag_list = [tagger.tag_text(sent,tagonly=True) for sent in text_tok]
    tags_made_list = [tree.make_tags(tags) for tags in tag_list]
    for sent_tags in tags_made_list:
        for entry in sent_tags:
            if re.search(const.REGEX_POS_VERB_TAG, entry.pos) is not None:
                return False
    return True


filelist = Tools.get_files(const.SOURCE_FOLDER)[16:26]  # Alle wikifiles AA bis AZ

'''loops through all files in filelist '''
'''Checks for Markups'''
for filename in filelist:
    file = open(const.SOURCE_FOLDER + const.FILE_OPERATOR + filename, "r", encoding=const.ENCODING)
    ignore_lines=False
    doc_dict = defaultdict(list)

    for line in file:
        if len(line.strip()) < 1:
            continue
        if line.startswith(const.DOC_START_OPERATOR):
            ignore_lines = False
            nextline = next(file)
            if nextline.strip() == const.NO_ARTICLE_OPERATOR:
                continue
            else:
                title = nextline.strip("\n")
        elif line.startswith(const.DOC_END_OPERATOR):
            continue
        elif not ignore_lines:
            if is_header(line):
                ignore_lines=True
            else:
                doc_dict[title].append(line.strip("\n"))
    file.close()
    Tools.dict_to_json_file(doc_dict,filename,const.INTRO_FOLDER, const.FILETAG_INTRO, "txt")
    print(filename+" done")



