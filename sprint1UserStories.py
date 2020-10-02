from project2 import processGedFile
from datetime import datetime
import datetime


'''
All Utility Functions are Below:
'''
# Expected parameters are 2 datetime objects of this format: YYYY-MM-DD
def months_between(start_date, end_date):
    num_months = (end_date. year - start_date. year) * 12 + (end_date. month - start_date. month)
    if num_months == 9:
        if ((end_date.day - start_date.day) > 0):
            num_months += 1
    return num_months


'''
Following are the definitions of Sprint1 User stories:
'''

'''
User story 01:
Requirement: Dates (birth, marriage, divorce, death) should not be after the current date
'''
def userStory01(file): #info, famtbl
    info, famtbl = processGedFile(file)
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
    return resultList

###################End of userStory01 ##################


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

        # check if they were married
        if marriageDate != 'NA':
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

'''
User story 08:
Requirement: Children should be born after marriage of parents (and not more than 9 months after their divorce)
'''
def userStory08(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict = processGedFile(file)

    # Create a list of
    resultList = list()

    
    # iterate through families
    for index in famDict:
        # get list of children
        children = famDict[index].Get_children()
        # get family id
        famid = famDict[index].Get_ID()
        # get family marriage
        marriage = famDict[index].Get_married()
        # get family divorce
        divorce = famDict[index].Get_divorced()

        # iterate through children
        for i in children:
            # get each child's bday
            childBday = indiDict[i].Get_birthday()

            # check if they were married
            if marriage != 'NA':
                # check if marriage was after the childs bday
                if marriage > childBday:
                    result_1_str = f"ANOMALY: FAMILY: US08: {famid}: Child {i} born {childBday} before marriage on {marriage}"
                    resultList.append(result_1_str)

            # check if they were divorced
            if divorce != 'NA':
                # check to see if the child's bday was not more than 9 months after their divorce
                if months_between(divorce, childBday) > 9: 
                    result_2_str = f"ANOMALY: FAMILY: US08: {famid}: Child {i} born {childBday} after divorce on {divorce}"
                    resultList.append(result_2_str)
            
    
    # Print the information of validated data
    for output in resultList:
        print(output)

    # return the list of validated data
    return resultList
    

###################End of userStory08 ##################

# Sprint1 Main function
if __name__ == "__main__":
   #userStory02("FamilyTree.ged")
   #userStory02("InputGedFiles/UserStory02_GED/testUserStory02-1.ged")
    userStory01("InputGedFiles/UserStory01_GED/testUserStory01-1.ged")
    #userStory08("InputGedFiles/UserStory08_GED/testUserStory08-5.ged")
    # ANOMALY: FAMILY: US08: F1: Child I5 born 1988-07-08 before marriage on 1997-12-31
    # []
    # ANOMALY: FAMILY: US08: F3: Child I1 born 1869-09-25 before marriage on 1962-08-24
    # ANOMALY: FAMILY: US08: F1: Child I6 born 1870-10-31 before marriage on 1997-12-31, ANOMALY: FAMILY: US08: F1: Child I5 born 1853-07-08 before marriage on 1997-12-31, ANOMALY: FAMILY: US08: F2: Child I3 born 1866-11-11 before marriage on 1967-05-09, ANOMALY: FAMILY: US08: F3: Child I1 born 1868-09-25 before marriage on 1962-08-24
    # ANOMALY: FAMILY: US08: F2: Child I3 born 1996-09-11 after divorce on 1995-12-10



    
