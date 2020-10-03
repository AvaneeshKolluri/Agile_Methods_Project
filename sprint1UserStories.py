from project2 import processGedFile
from dateutil.relativedelta import relativedelta

'''
Following are the definitions of Sprint1 User stories:
'''

'''
User story 02:
Requirement: Birth should occur before marriage of an individual
'''

'''
User story 09:
Requirement: Birth date should not be after death of parents
Author: Zach and Pratim
'''

'''
User story 10:
Requirement: Marriage should not occur prior to the age of 14 
Author: Zach 
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

def userStory09(file):

    # get individuals and families in file, create results
    individuals, families = processGedFile(file)
    resultsList = list()

    #iterate through families
    for family in families.keys():
        
        #find married families
        if families[family].Get_married() != "NA":

            #get husband ID and wife ID as well as death dates 
            husband = families[family].Get_husbandID()
            husband_death_date = individuals[husband].Get_death()
            wife = families[family].Get_wifeID()
            wife_death_date = individuals[wife].Get_death()

            #get children of family
            children = families[family].Get_children()

            #iterate through each child
            if len(children) > 0 and (wife_death_date != "NA" or husband_death_date != "NA"):

                #iterate through children
                for child in children:
                
                #get each child birthdate
                    child_birthdate = individuals[child].Get_birthday()
                    
                    #check if death date is before child birthdate 
                    if husband_death_date < child_birthdate:
                        resultsList.append(f"ERROR: FAMILY: US09: {family}: Husband ({husband}) died {husband_death_date} before child's ({child}) birth {child_birthdate}")
                    if wife_death_date < child_birthdate:
                        resultsList.append(f"ERROR: FAMILY: US09: {family}: Wife ({wife}) died {wife_death_date} before child's ({child}) birth {child_birthdate}")

    #return list
    return resultsList

###################End of userStory09 ##################
    
def userStory10(file):

    # get individuals and families in file, create results
    individuals, families = processGedFile(file)
    resultsList = list()

    #iterate through families
    for family in families.keys():
        
        #find married families
        if families[family].Get_married() != "NA":

            #get husband ID and wife ID as well as birth dates 
            husband = families[family].Get_husbandID()
            husband_birth_date = individuals[husband].Get_birthday()
            wife = families[family].Get_wifeID()
            wife_birth_date = individuals[wife].Get_birthday()
            
            #get married date
            family_marriage_date = families[family].Get_married()

            #determine if husband or wife was married after 14 and output a message if not
            if float(relativedelta(family_marriage_date, husband_birth_date).years) < float(14):
                resultsList.append(f"ERROR: FAMILY: US10: {family}: Husband ({husband}) birth date {husband_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")
            if float(relativedelta(family_marriage_date, wife_birth_date).years) < float(14):
                resultsList.append(f"ERROR: FAMILY: US10: {family}: Wife ({wife}) birth date {wife_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")
                
    return resultsList

###################End of userStory10 ##################


# Sprint1 Main function
if __name__ == "__main__":
   print(userStory09("InputGedFiles/UserStory09_GED/FamilyTree.ged"))