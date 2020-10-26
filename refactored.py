from userStories import processGedFile
from dateutil.relativedelta import relativedelta
from datetime import datetime
import datetime

def portion(file):
    indiDict,famDict = processGedFile(file)
    WisDead = False
    HisDead = False
    resultList = list()

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
        portion(file)
        if(WisDead and marriedDate>wifeDeath):
            result_1_str = "Error: wedding occurs after wife death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Wife Death: " + str(wifeDeath)
            resultList.append(result_1_str)

        if(HisDead and marriedDate>husbandDeath):
            result_1_str = "Error: wedding occurs after husband death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Husband Death: " + str(husbandDeath)
            resultList.append(result_1_str)

    return resultList


def userStory06(file):
    portion(file)
    if(WisDead and divorcedDate>wifeDeath):
        result_1_str = "Error: divorce occurs after wife death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Wife Death: " + str(wifeDeath)
        resultList.append(result_1_str)

    if(HisDead and divorcedDate>husbandDeath):
        result_1_str = "Error: divorce occurs after husband death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Husband Death: " + str(husbandDeath)
        resultList.append(result_1_str)

    return resultList
