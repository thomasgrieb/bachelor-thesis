'''
Hilfsprogramm, stellt Berechnungsformeln für results_calc.py bereit
'''

def get_precision(tp, fp):
    return tp/(tp+fp)

def get_recall(tp, fn):
    return tp/(tp+fn)

def get_f1(p, r):
    return (2*p*r)/(p+r)

def get_scores(tp, fp, fn):
    precision = get_precision(tp, fp)
    recall = get_recall(tp, fn)
    f1 = get_f1(precision, recall)

    print("precision: " + str(precision))
    print("recall: " + str(recall))
    print("f1 score: " + str(f1))

''' Formeln mit FE'''

def get_precision_fe(tp, fp, fe):
    return tp/(tp+fp+fe)

def get_recall_fe(tp, fn, fe):
    return tp/(tp+fn+fe)

def get_scores_fe(tp, fp, fn, fe):
    precision = get_precision_fe(tp, fp,fe)
    recall = get_recall_fe(tp, fn,fe)
    f1 = get_f1(precision, recall)

    print("precision_fe: " + str(precision))
    print("recall_fe: " + str(recall))
    print("f1 score_fe: " + str(f1))