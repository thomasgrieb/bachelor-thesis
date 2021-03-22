import subprocess
import Constants as const
import json
from datetime import datetime

'''
Takes inputtext and grammar\n
Returns output of called transducer
'''

def process_entry(input, grammar):
    return subprocess.check_output(const.EXECUTE_OPERATOR + grammar + " " + input, shell=True,
                                     encoding=const.ENCODING)


'''
Main
Short code that applies the title_grammar Transducer in order to eliminate Tagging of Years or Filmtypes inside of \n
Titles and after that the genre_grammar, in order so separate Genre and Filmtype\n
Does so separately for each article as to not get enormous runtime \n
Also replaces the key with an ID-Number and prints runtime
'''

an_file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_ANN_FILE+const.ENDING_JSON,"r",
                  encoding=const.ENCODING)
intro_dict = json.load(an_file)
an_file.close()

title_clean_grammar = const.TOOL_FOLDER+const.FILE_OPERATOR+"title_grammar"
genre_sep_grammar = const.TOOL_FOLDER+const.FILE_OPERATOR+"genre_grammar"

len_intro = len(intro_dict)
intro_clean_dict = {}

c=0
movie_id=0
start = datetime.now()

for key, value in intro_dict.items():
    if c%100 == 0:
        print("Runtime for "+str(c)+" files: "+str(datetime.now() - start)+"\n")
    value=value.replace("\"","**")
    input = "\""+value+"\""
    output = process_entry(input,title_clean_grammar)
    output = "\""+output+"\""
    output2 = process_entry(output,genre_sep_grammar)
    value_n = output2 if len (output2) > 1 else " "
    intro_clean_dict[str(movie_id)]=value_n.strip()
    movie_id+=1
    c+=1

an_file_clean = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+const.JSON_CLEAN_ANN_FILE+const.ENDING_JSON,"w",
                  encoding=const.ENCODING)
json.dump(intro_clean_dict, an_file_clean, indent=4, ensure_ascii=False)
an_file_clean.close()

print("Total runtime for "+str(c)+" files: "+str(datetime.now()-start))

