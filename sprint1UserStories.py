from project2 import processGedFile

'''
Following are the definitions of Sprint1 User stories:
'''

'''
User story 02:
Requirement: Birth should occur before marriage of an individual
'''
def userStory02(file):

    # Fetch the parsed object's from input ged file
    indiDict, famDict = processGedFile(file)

    # Create a list of
    resultList = list()

    # Process through all individual's details
    for index in famDict:
        # Get husband ID
        husbandID = famDict[index].Get_husbandID()
        #print(f"husbandID: {husbandID}")
        # Get Wife ID
        wifeID = famDict[index].Get_wifeID()
        #print(f"wifeID: {wifeID}")
        # Get husband birth date
        husBirthDate = indiDict[husbandID].Get_birthday()
        #print(f"husBirthDate: {husBirthDate}")
        # Get wife birth date
        wifeBirthDate = indiDict[wifeID].Get_birthday()
        #print(f"wifeBirthDate: {wifeBirthDate}")
        # Get marriage date
        marriageDate = famDict[index].Get_married()
        #print(f"marriageDate: {marriageDate}")

        # Print error if husband's birth date is greater than marriage date
        if husBirthDate > marriageDate:
            result_1_str = f"ERROR: FAMILY: US02: {husbandID}: Husband's birth date {husBirthDate} is after marriage date {marriageDate}"
            resultList.append(result_1_str)

        # Print error if wife's birth date is greater than marriage date
        if wifeBirthDate > marriageDate:
            result_2_str = f"ERROR: FAMILY: US02: {wifeID}: Wife's birth date {wifeBirthDate} is after marriage date {marriageDate}"
            resultList.append(result_2_str)

    # Print the information of validated data
    for output in resultList:
        print(output)

    # return the list of validated data
    return resultList
###################End of userStory02 ##################



# Sprint1 Main function
if __name__ == "__main__":
   #userStory02("FamilyTree.ged")
   userStory02("InputGedFiles/UserStory02_GED/testUserStory02-1.ged")

