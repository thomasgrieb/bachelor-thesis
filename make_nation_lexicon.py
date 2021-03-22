import Constants as const

flexionen_nation = ["","e", "er", "es", "en", "em"]
nationen = ["deutsch"]


'''
Generates possible flexions of given nation-adjective \n
Takes String, returns list of Strings
'''

def flex_nation(wurzel_nation):
    flexionen = []
    for flex in flexionen_nation:
        flexionen.append((wurzel_nation.strip()+flex))
    return flexionen

'''Main - Quick Programm for generating basis for Rewrite-Dictionary'''

nat = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"nations_raw.dic","r",encoding=const.ENCODING)
nat2 = open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"nations.dic","w",encoding=const.ENCODING)

for elem in nat:
    elem_s = elem.strip().split("$")
    flex = flex_nation(elem_s[1])
    for adj in flex:
        nat2.write(adj+"\t"+elem_s[0]+"\n")

nat.close()
nat2.close()
