from project2 import processGedFile



def Story4(file):
    individuals,famDict = processGedFile(file)
    resultList = list()
    for key in famDict:
        family = famDict[key]
        familyID = family.Get_ID()
        if(famDict[familyID] != 'NA'):
            if(famDict[familyID].Get_married() != 'NA'):
               marriedDate = famDict[familyID].Get_married()
               print("Married Date: " + str(marriedDate))
           
            if(famDict[familyID].Get_divorced() != 'NA'):
                divorcedDate = famDict[familyID].Get_divorced()
                print("Divorced Date: " + str(divorcedDate))
                if(marriedDate>divorcedDate):
                    str1 = 'Error: the date of marriage is greater than the date of divorce for family ID: ' + str(familyID)
                    resultList.append(str1)
        return resultList

result = Story4("divorcebeforewedding.ged")
print(result)
