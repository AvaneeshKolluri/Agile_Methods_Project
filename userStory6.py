from project2 import processGedFile



#death before divorce
def Story6(file):
    indiDict,famDict = processGedFile(file)
    WisDead = False
    HisDead = False
    resultList = list()
    

    for key in famDict:
        family = famDict[key]
        familyID = family.Get_ID()
        
        if(famDict[key] != 'NA'):
            husbandID = str(famDict[familyID].Get_husbandID())
            wifeID = str(famDict[familyID].Get_wifeID())

            if(indiDict[husbandID].Get_death() != 'NA'):
                husbandDeath = indiDict[husbandID].Get_death()
                HisDead = True
                #print(type(husbandDeath))
            if(indiDict[wifeID].Get_death() != 'NA'):
                wifeDeath = indiDict[wifeID].Get_death()
                WisDead = True
                #print(type(wifeDeath))
            if(famDict[familyID].Get_divorced() != "NA"):
                divorcedDate = famDict[familyID].Get_divorced()

            if(WisDead and divorcedDate>wifeDeath):
                #print("the wife is dead and the divorce date is after death")
                result_1_str = "Error: divorce occurs after wife death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Wife Death: " + str(wifeDeath)
                resultList.append(result_1_str)

            if(HisDead and divorcedDate>husbandDeath):
               # print("the husband is dead and the divorce date is after death")
                result_1_str = "Error: divorce occurs after husband death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Husband Death: " + str(husbandDeath)
                resultList.append(result_1_str)
            
    return resultList
          

result = Story6("husband.ged")
print(result)
