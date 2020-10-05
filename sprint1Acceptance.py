from project2 import printTablesData
from project2 import processGedFile
from sprint1UserStories import userStory01
from sprint1UserStories import userStory02
from sprint1UserStories import userStory03
from sprint1UserStories import userStory04
from sprint1UserStories import userStory05
from sprint1UserStories import userStory06
from sprint1UserStories import userStory07
from sprint1UserStories import userStory08
from sprint1UserStories import userStory09
from sprint1UserStories import userStory10

def sprint1UserStories():
    fileName="InputGedFiles/SprintAcceptance/testSprint1Acceptance.ged"
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
    

    for eachError in errorList:
       print(eachError)

    with open('sprint1Output.txt','w') as file:
        file.write('\n\nIndividuals Information----------------------->\n')
        file.write(indiTable.get_string())
        file.write("\n")
        file.write('\n\nFamily Information----------------------->\n')
        file.write(familyTable.get_string())
        file.write("\n")
        for eachError in errorList:
            file.write(eachError+"\n")
        
        
if __name__ == "__main__":
    sprint1UserStories()