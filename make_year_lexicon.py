import Constants as const

'''
Erstelllt Jahreszahlen-Lexikon
'''

years=open(const.RESOURCE_FOLDER+const.FILE_OPERATOR+"years.dic","w",encoding=const.ENCODING)


for num in range(1888,2030):
    years.write(str(num)+"\t"+const.YEAR_MARKUP_L+str(num)+const.YEAR_MARKUP_R+"\n")
    if num%10 == 0:
        years.write(str(num) + "er\t" + const.YEAR_MARKUP_L + str(num) + "er" + const.YEAR_MARKUP_R + "\n")

years.close()