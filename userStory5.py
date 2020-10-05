from project2 import processGedFile
#User story 5, marriage before death


#death before divorce
def userStory05(file):
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
            if(famDict[familyID].Get_married() != "NA"):
                marriedDate = famDict[familyID].Get_married()

            if(WisDead and marriedDate>wifeDeath):
                #print("the wife is dead and the wedding date is after death")
                result_1_str = "Error: wedding occurs after wife death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Wife Death: " + str(wifeDeath)
                resultList.append(result_1_str)

            if(HisDead and marriedDate>husbandDeath):
               # print("the husband is dead and the wedding date is after death")
                result_1_str = "Error: wedding occurs after husband death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Husband Death: " + str(husbandDeath)
                resultList.append(result_1_str)
            
    return resultList
          

result = userStory05("husband.ged")
print(result)
