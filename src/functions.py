import re

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
def removefinalcharacters(text):
    if text[-1] == " ":
        return text[0:(len(text)-1)]
    elif text[-1] == "?":
         return text[0:(len(text)-1)]
    else:
        return text
def ChangeType(text):
    dic = {
        'Invalid':'other',
        'Sea Disaster':'other',
        'Boat':'other',
        'Boating':'other' 
    } 
    return dic.get(text,text)

