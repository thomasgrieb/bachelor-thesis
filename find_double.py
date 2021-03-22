import Constants as const

'''
Kleines Hilfsprogramm für Lexikonerstellung
Findet doppelte Einträge und gibt sie auf der Konsole aus
'''

double=[]

file_input = input("File angeben: ")
file = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+file_input+const.ENDING_DIC,"r",encoding=const.ENCODING)
for elem in file:
    elem_l=elem.split("\t")
    if elem_l[0] not in double:
        double.append(elem_l[0])
    else:
        print(elem_l[0]+" ist doppelt")

file.close()