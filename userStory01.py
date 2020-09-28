from project2 import main
import datetime
from individualClass import individualClass as indiClass
from familyClass import familyClass
import warnings

def story1(file): #info, famtbl
    info, famtbl = main(file)
    resultList = list()
    
    dt = datetime.datetime.now()
    current = datetime.date(dt.year, dt.month, dt.day)
    resultList = list()
    good = True
    for key in info:
        user = info[key]
        fam = user.Get_spouse()
        individualID = user.Get_ID()
        for i in range(len(fam)):
            marr = famtbl[fam[i]].Get_married()
            if(marr != 'NA'):
                marriage = current > marr
                #Do something
                if(marriage == False):
                    result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Marriage {marr} occurs in the future"
                    resultList.append(result_1_str)
                #mlst += [marriage]
        for i in range(len(fam)):
            div = famtbl[fam[i]].Get_divorced()
            if(div != 'NA'):
                divorced = current > div
                #Do something
                if(divorced == False):
                    result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Divorce {div} occurs in the future"
                    resultList.append(result_1_str)
        bday = current > user.Get_birthday()
        if(bday == False):
            result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Birthday {user.Get_birthday()} occurs in the future"
            resultList.append(result_1_str)
        #Do something
        if(user.Get_death() != 'NA'):
            death = current > user.Get_death()
            #Do something
            if(death == False):
                result_1_str = f"ERROR: INDIVIDUAL: US01: {individualID}: Death {user.Get_death()} occurs in the future"
                resultList.append(result_1_str)
    for output in resultList:
        print(output)
    #warnings.filterwarnings("ignore")
    return resultList
