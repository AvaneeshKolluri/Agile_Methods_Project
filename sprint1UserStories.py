from project2 import processGedFile
from dateutil.relativedelta import relativedelta
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
Author: Avaneesh
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
Authors: Pair Programmed: Srikanth & Avaneesh
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
        if wifeID != "NA":
            wifeBirthDate = indiDict[wifeID].Get_birthday()
        else: wifeBirthDate = "NA"
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
User Story 03:
Requirement: Birth date should be before death date for all people.
Author: Erick
'''
def userStory03(file):
    indiDict,famDict = processGedFile(file);
    resultList = list();

    for index in indiDict:
        individual = indiDict[index]
        if (individual.Get_death() == "NA"):
            continue;
        deathDate = str(individual.Get_death());
        birthDate = str(individual.Get_birthday());

        countDeath = int(deathDate[:deathDate.find("-")])
        countBirth = int(birthDate[:birthDate.find("-")])

        if (countDeath < countBirth):
            error = f"ERROR: INDIVIDUAL: US03: {individual.Get_ID()} Death date occurs before birth date - Birth {individual.Get_birthday()}: Death {individual.Get_death()}"
            print(error);
            resultList.append(error)
            continue;
        if (countDeath > countBirth):
            continue;

        deathDate = deathDate[deathDate.find("-") + 1:]
        birthDate = birthDate[birthDate.find("-") + 1:]

        countDeath = int(deathDate[:deathDate.find("-")])
        countBirth = int(birthDate[:birthDate.find("-")])
        if (countDeath < countBirth):
            error = f"ERROR: INDIVIDUAL: US03: {individual.Get_ID()} Death date occurs before birth date - Birth {individual.Get_birthday()}: Death {individual.Get_death()}"
            print(error);
            resultList.append(error)
            continue;
        if (countDeath > countBirth):
            continue;

        deathDate = deathDate[deathDate.find("-") + 1:]
        birthDate = birthDate[birthDate.find("-") + 1:]
        countDeath = int(deathDate);
        countBirth = int(birthDate);
        if (countDeath < countBirth):
            error = f"ERROR: INDIVIDUAL: US03: {individual.Get_ID()} Death date occurs before birth date - Birth {individual.Get_birthday()}: Death {individual.Get_death()}"
            print(error);
            resultList.append(error)
            continue;


    # Print the information of validated data
    for output in resultList:
        print(output)

    resultList.sort()
    # return the list of validated data
    return resultList


'''
User Story 04:
Requirement: Marriage date should be before divorce date for all marriages.
Author: Erick
'''
def userStory04(file):
    indiDict,famDict = processGedFile(file);
    resultList = list();

    for index in famDict:
        family = famDict[index]
        if (family.Get_divorced() == "NA"):
            continue;
        divDate = str(family.Get_divorced());
        marrDate = str(family.Get_married());

        countDiv = int(divDate[:divDate.find("-")])
        countMarr = int(marrDate[:marrDate .find("-")])
        if (countDiv < countMarr):
            error = f"ERROR: FAMILY: US04: {family.Get_ID()} Divorce date occurs before marriage date - Marriage {family.Get_married()}: Divorce {family.Get_divorced()}"
            resultList.append(error)
            continue;
        if (countDiv > countMarr):
            continue;

        divDate = divDate[divDate.find("-") + 1:]
        marrDate = marrDate[marrDate.find("-") + 1:]

        countDiv = int(divDate[:divDate.find("-")])
        countMarr = int(marrDate[:marrDate.find("-")])
        if (countDiv < countMarr):
            error = f"ERROR: FAMILY: US04: {family.Get_ID()} Divorce date occurs before marriage date - Marriage {family.Get_married()}: Divorce {family.Get_divorced()}"
            resultList.append(error)
            continue;
        if (countDiv > countMarr):
            continue;

        divDate = divDate[divDate.find("-") + 1:]
        marrDate = marrDate[marrDate.find("-") + 1:]

        countDiv = int(divDate);
        countMarr = int(marrDate);
        print(countDiv);
        print(countMarr);
        if (countDiv < countMarr):
            error = f"ERROR: FAMILY: US04: {family.Get_ID()} Divorce date occurs before marriage date - Marriage {family.Get_married()}: Divorce {family.Get_divorced()}"
            resultList.append(error)
            continue;


    # Print the information of validated data
    for output in resultList:
        print(output)

    resultList.sort()
    # return the list of validated data
    return resultList


'''
User story 07:
Requirement: Death should be less than 150 years after birth for dead people,
             and current date should be less than 150 years after birth for all living people
Author: Srikanth
'''
# Method: userStory07
def userStory07(file):

    # Fetch the parsed object's from input ged file
    indiDict = processGedFile(file)
    # Create a list of
    resultList = list()

    # Process through all individual's details
    for index in indiDict:

        # Fetch individual details like age, deceased, ID, birthdDate and deathDate.
        individualAge= indiDict[index].Get_age()
        isIndiAlive = indiDict[index].Get_alive()
        individualID = indiDict[index].Get_ID()
        birthDate = indiDict[index].Get_birthday()
        deathDate = indiDict[index].Get_death()

        # If Age is greater than or equal to 150 prompt Invalid data
        if (individualAge >= 150):
            # Check if an individual is alive or not
            if (isIndiAlive == False):
                #error 1
                result_1_str = f"ERROR: INDIVIDUAL: US07: {individualID} More than 150 years old at death - Birth {birthDate}: Death {deathDate}"
                resultList.append(result_1_str)
            else:
                # error 2
                result_2_str = f"ERROR: INDIVIDUAL: US07: {individualID} More than 150 years old - Birth date {birthDate}"
                resultList.append(result_2_str)

    # Print the information of validated data
    for output in resultList:
        print(output)

    # return the list of validated data
    return resultList

###################End of userStory07 ##################

'''
User story 08:
Requirement: Children should be born after marriage of parents (and not more than 9 months after their divorce)
Authors: Pair Programmed: Avaneesh & Srikanth
'''
# Method: userStory08
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

    resultList.sort()
    # return the list of validated data
    return resultList

###################End of userStory08 ##################

'''
User story 09:
Requirement: Birth date should not be after death of parents
Author: Zach and Pratim
'''

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

'''
User story 10:
Requirement: Marriage should not occur prior to the age of 14
Author: Zach
'''

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
   userStory01("FamilyTree.ged")
   userStory02("FamilyTree.ged")
   userStory07("FamilyTree.ged")
   userStory08("FamilyTree.ged")
   userStory09("FamilyTree.ged")
   userStory10("FamilyTree.ged")
