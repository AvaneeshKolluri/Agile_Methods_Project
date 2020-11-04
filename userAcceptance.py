from gedReader import printTablesData
from gedReader import processGedFile
from userStories import userStory01
from userStories import userStory02
from userStories import userStory03
from userStories import userStory04
from userStories import userStory05
from userStories import userStory06
from userStories import userStory07
from userStories import userStory08
from userStories import userStory09
from userStories import userStory10
from userStories import userStory11
from userStories import userStory12
from userStories import userStory13
from userStories import userStory14
from userStories import userStory15
from userStories import userStory16
from userStories import userStory17
from userStories import userStory18
from userStories import userStory19
from userStories import userStory20

def sprint1n2UserStories():
    fileName="InputGedFiles/SprintAcceptance/testSprint1_2_Acceptance.ged"
    indiObj,familyObj = processGedFile(fileName)
    indiTable,familyTable= printTablesData(indiObj, familyObj)
    errorList = []
    errorList.extend(userStory01(fileName))
    errorList.extend(userStory02(fileName))
    errorList.extend(userStory03(fileName))
    errorList.extend(userStory04(fileName))
    errorList.extend(userStory05(fileName))
    errorList.extend(userStory06(fileName))
    errorList.extend(userStory07(fileName))
    errorList.extend(userStory08(fileName))
    errorList.extend(userStory09(fileName))
    errorList.extend(userStory10(fileName))
    errorList.extend(userStory11(fileName))
    errorList.extend(userStory12(fileName))
    errorList.extend(userStory13(fileName))
    errorList.extend(userStory14(fileName))
    errorList.extend(userStory15(fileName))
    errorList.extend(userStory16(fileName))
    errorList.extend(userStory17(fileName))
    errorList.extend(userStory18(fileName))
    errorList.extend(userStory19(fileName))
    errorList.extend(userStory20(fileName))


    for eachError in errorList:
       print(eachError)

    with open('sprint1n2Output.txt','w') as file:
        file.write('\n\nIndividuals Information----------------------->\n')
        file.write(indiTable.get_string())
        file.write("\n")
        file.write('\n\nFamily Information----------------------->\n')
        file.write(familyTable.get_string())
        file.write("\n")
        for eachError in errorList:
            file.write(eachError+"\n")


if __name__ == "__main__":
    sprint1n2UserStories()