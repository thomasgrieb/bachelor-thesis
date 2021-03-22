import Constants as const
import scores

'''
Hilfsprogramm \n
Errechnet diverse Statistiken und Scores für den Vergleich von automatisch generierten Relationen zum Goldstandard \n
Gibt die Werte auf die Konsole aus
'''

gold_file = open(const.RESOURCE_FOLDER + const.FILE_OPERATOR + "relations_goldstandard" + const.ENDING_TXT, "r",
                 encoding=const.ENCODING)
gold = [entry.strip() for entry in gold_file]
gold_file.close()
gold_split = [elem.strip("<").strip(">").split("|") for elem in gold]

relation_file = open(const.RESOURCE_FOLDER + const.FILE_OPERATOR + const.RELATIONS_FILE + const.ENDING_TXT, "r",
                     encoding=const.ENCODING)
relations = [entry.strip() for entry in relation_file][0:115]
relation_file.close()

ident = 0
nearly_ident = 0
diff=0
not_movie = 0
line = 0
matrix = []
fe=0
fp=0
fn=0
tp=0
tn=0
gesamt=0

for rel in relations:
    gesamt+=1
    if gold[line][0] == "#":
        not_movie +=1
        line += 1
        continue
    rel_s = rel.strip("<").strip(">").split("|")
    c = 0
    res = []
    for elem in rel_s:
        if elem == gold_split[line][c] and elem != const.RELATIONS_EMPTY:
            res.append(const.ACC_TP)    #true positive = einträge vorhanden und identisch
            tp+=1
        elif elem == gold_split[line][c] and elem == const.RELATIONS_EMPTY:
            res.append(const.ACC_TN)    #true negative = einträge nicht vorhanden und identisch
            tn+=1
        else:
            if elem == const.RELATIONS_EMPTY and gold_split[line][c] != const.RELATIONS_EMPTY:
                res.append(const.ACC_FN)    #false negative = eintrag leer, sollte aber gefunden werden
            elif elem != const.RELATIONS_EMPTY and gold_split[line][c] == const.RELATIONS_EMPTY:
                res.append(const.ACC_FP)    #false positive = eintrag gefunden, sollte aber leer sein
            elif elem != gold_split[line][c]:
                res.append(const.ACC_FE)    #false entry = eintrag gefunden, sollte gefunden werden, ist aber inkorrekt
        c+=1
    matrix.append(res)
    line+=1

for l in matrix:
    i = 0
    for entry in l:
        if entry == const.ACC_TP or entry == const.ACC_TN:
            i+=1
        elif entry == const.ACC_FE:
            fe+=1
        elif entry == const.ACC_FN:
            fn+=1
        elif entry == const.ACC_FP:
            fp+=1
    if i == 5:
        ident+=1
    if i == 4:
        nearly_ident+=1
    if i<=3:
        diff+=1

print("Identisch: "+str(ident)+" , Akzeptabel: "+ str(nearly_ident)+" , Verschieden: "+str(diff)+" , True Positive: "
      +str(tp)+" , False Entry: "+str(fe)+" , False Positive: " +str(fp)+" , False Negative: "+str(fn)+
      " , Kein Film: "+str(not_movie)+ " , True Negative: "+str(tn))

title=[]
filmtype=[]
genre=[]
nat=[]
year=[]

for l in matrix:
    title.append(l[0])
    filmtype.append(l[1])
    genre.append(l[2])
    nat.append(l[3])
    year.append(l[4])

print("Relationen: ", gesamt)
print("\n")

print("title:")
print(title.count(const.ACC_TP),title.count(const.ACC_FP),title.count(const.ACC_FN), title.count(const.ACC_TN),
      title.count(const.ACC_FE))
scores.get_scores(title.count(const.ACC_TP),title.count(const.ACC_FP),title.count(const.ACC_FN))
scores.get_scores_fe(title.count(const.ACC_TP),title.count(const.ACC_FP),title.count(const.ACC_FN),title.count(const.ACC_FE))

print("\nfilmtyp:")
print(filmtype.count(const.ACC_TP),filmtype.count(const.ACC_FP), filmtype.count(const.ACC_FN),
      filmtype.count(const.ACC_TN),filmtype.count(const.ACC_FE))
scores.get_scores(filmtype.count(const.ACC_TP),filmtype.count(const.ACC_FP), filmtype.count(const.ACC_FN))
scores.get_scores_fe(filmtype.count(const.ACC_TP),filmtype.count(const.ACC_FP), filmtype.count(const.ACC_FN),filmtype.count(const.ACC_FE))

print("\ngenre:")
print(genre.count(const.ACC_TP),genre.count(const.ACC_FP), genre.count(const.ACC_FN),genre.count(const.ACC_TN),
      genre.count(const.ACC_FE))
scores.get_scores(genre.count(const.ACC_TP),genre.count(const.ACC_FP), genre.count(const.ACC_FN))
scores.get_scores_fe(genre.count(const.ACC_TP),genre.count(const.ACC_FP), genre.count(const.ACC_FN),genre.count(const.ACC_FE))

print("\nnat:")
print(nat.count(const.ACC_TP),nat.count(const.ACC_FP), nat.count(const.ACC_FN), nat.count(const.ACC_TN),
      nat.count(const.ACC_FE))
scores.get_scores(nat.count(const.ACC_TP),nat.count(const.ACC_FP), nat.count(const.ACC_FN))
scores.get_scores_fe(nat.count(const.ACC_TP),nat.count(const.ACC_FP), nat.count(const.ACC_FN),nat.count(const.ACC_FE))

print("\njahr:")
print(year.count(const.ACC_TP),year.count(const.ACC_FP), year.count(const.ACC_FN), year.count(const.ACC_TN),
      year.count(const.ACC_FE))
scores.get_scores(year.count(const.ACC_TP),year.count(const.ACC_FP), year.count(const.ACC_FN))
scores.get_scores_fe(year.count(const.ACC_TP),year.count(const.ACC_FP), year.count(const.ACC_FN),year.count(const.ACC_FE))

print("\ntotal:")
scores.get_scores(tp,fp, fn)
scores.get_scores_fe(tp,fp, fn,fe)

print("\n")
line_g=0
c=2
matrix_g=[]
for rel in relations:
    rel_s = rel.strip("<").strip(">").split("|")
    if gold_split[line_g][c] != rel_s[c]:
        print("genre\t",rel_s[c],"\t",gold_split[line_g][c])
    line_g+=1
