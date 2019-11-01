def changeCharacterSex(text):
    if text == "M ":
        return "M"
    elif text in [".","lli","N"]:
        return "UNKNOWN"
    else:
        return text
        
def changeFatalValue(text):
    dic = {
        '#VALUE!':'UNKNOWN',
        'F':'UNKNOWN',
        'n':'N',
        ' N':'N',
        'N ':'N'
        }
    return dic.get(text,text)