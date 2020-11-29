from gedReader import processGedFile
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from datetime import timedelta
import datetime
from dateutil import relativedelta as rdelta
import collections
import operator

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

def exactDateDifference(newer, older):  # newer - older
    return rdelta.relativedelta(newer,older)

def yearDifference(newer,older):
    yearDifference = newer.year - older.year
    if newer.month < older.month:
        yearDifference = yearDifference - 1;
    if newer.month == older.month:
        if newer.day < older.day:
            yearDifference = yearDifference - 1;
    return yearDifference;

# Function to calculate a given birthday date is within next 30days from current date.
# Expected input date object in format YYYY-MM-DD
def isBdayWithinNext30days(inputDate):
    retVar = False
    if inputDate != 'NA':
        today = date.today()
        currDayOfYear = today.timetuple().tm_yday
        inputDayOfYear = inputDate.timetuple().tm_yday
        currYear = today.timetuple().tm_year
        inputYear = inputDate.timetuple().tm_year

        if (inputDayOfYear >= currDayOfYear) and (inputDayOfYear <= (currDayOfYear + 30)):
            retVar = True
        elif currDayOfYear >= 335:
            yearEndDays = (365 - currDayOfYear) + inputDayOfYear
            if yearEndDays <= 30:
                retVar = True
    return retVar

# Function to calculate a given date is within last 30days from current date.
# Expected input date object in format YYYY-MM-DD
def isWithinLast30days(inputDate):
    retVar = False
    if inputDate != 'NA':
        today = date.today()
        currDayOfYear = today.timetuple().tm_yday
        inputDayOfYear = inputDate.timetuple().tm_yday
        currYear = today.timetuple().tm_year
        inputYear = inputDate.timetuple().tm_year

        if currDayOfYear >= 31 and currYear == inputYear:
            if (inputDayOfYear <= currDayOfYear) and (inputDayOfYear >= (currDayOfYear - 30)):
                retVar = True
        elif currDayOfYear < 31:
            yearEndDays = (365 - inputDayOfYear) + currDayOfYear
            if inputDayOfYear < currDayOfYear and currYear == inputYear:
                retVar = True
            elif inputDayOfYear >= 335 and currYear == (inputYear +1) and yearEndDays <= 30:
                retVar = True

    return retVar

'''
Bad Smell #1:
Repetitive getting of date of death/birth of husband and wife from a family
Author: Zach George
'''
# Get husband and wife and relevant husband and wife date from a marriage in a family
def get_husband_and_wife_dates(family, individuals, date_type):

    husband = family.Get_husbandID()
    wife = family.Get_wifeID()

    if date_type == "birth":
        husband_date = individuals[husband].Get_birthday()
        wife_date = individuals[wife].Get_birthday()

    if date_type == "death":
        husband_date = individuals[husband].Get_death()
        wife_date = individuals[wife].Get_death()

    return husband, husband_date, wife, wife_date

'''
Bad Smell #2:
Repetitive of printing output of list and returning list
Author: Zach George
'''
# Print list
def print_list(results):
    for item in results:
        print(item)

'''
Following are the definitions of Sprint1 User stories:
'''

'''
User story 01:
Requirement: Dates (birth, marriage, divorce, death) should not be after the current date
Author: Avaneesh
'''
def userStory01(file): #info, famtbl
    info, famtbl, lines = processGedFile(file)
    resultList = list()

    dt = datetime.datetime.now()
    current = datetime.date(dt.year, dt.month, dt.day)
    resultList = list()
    good = True
    for key in info:
        user = info[key]
        fam = user.Get_spouse()
        individualID = user.Get_ID()
        if fam != 'NA':
            for i in range(len(fam)):
                marr = famtbl[fam[i]].Get_married()
                if(marr != 'NA'):
                    marriage = current > marr
                    #Do something
                    if(marriage == False):
                        line = lines[f"{famtbl[fam[i]].Get_ID()}: Married date set"]
                        result_1_str = f"ERROR: INDIVIDUAL: US01: {line}: {individualID}: Marriage {marr} occurs in the future"
                        resultList.append(result_1_str)
                    #mlst += [marriage]
            for i in range(len(fam)):
                div = famtbl[fam[i]].Get_divorced()
                if(div != 'NA'):
                    divorced = current > div
                    #Do something
                    if(divorced == False):
                        line = lines[f"{famtbl[fam[i]].Get_ID()}: Divorced date set"]
                        result_1_str = f"ERROR: INDIVIDUAL: US01: {line}: {individualID}: Divorce {div} occurs in the future"
                        resultList.append(result_1_str)
            bday = current > user.Get_birthday()
            if(bday == False):
                line = lines[f"{individualID}: Birthday set"]
                result_1_str = f"ERROR: INDIVIDUAL: US01: {line}: {individualID}: Birthday {user.Get_birthday()} occurs in the future"
                resultList.append(result_1_str)
            #Do something
            if(user.Get_death() != 'NA'):
                death = current > user.Get_death()
                #Do something
                if(death == False):
                    line = lines[f"{individualID}: Death date set"]
                    result_1_str = f"ERROR: INDIVIDUAL: US01: {line}: {individualID}: Death {user.Get_death()} occurs in the future"
                    resultList.append(result_1_str)
    # for output in resultList:
    #     print(output)
    return resultList

###################End of userStory01 ##################


'''
User story 02:
Requirement: Birth should occur before marriage of an individual
Authors: Pair Programmed: Srikanth & Avaneesh
'''

def userStory02(file):

    # Fetch the parsed object's from input ged file
    indiDict, famDict, lines = processGedFile(file)

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
        if wifeID != "NA":
            husBirthDate = indiDict[husbandID].Get_birthday()
        else: husBirthDate = "NA"
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
            if husBirthDate != 'NA':
                if husBirthDate > marriageDate:
                    line = lines[f"{index}: Married date set"]
                    result_1_str = f"ERROR: FAMILY: US02: {line}: {husbandID}: Husband's birth date {husBirthDate} is after marriage date {marriageDate}"
                    resultList.append(result_1_str)

            # Print error if wife's birth date is greater than marriage date
            if wifeBirthDate != 'NA':
                if wifeBirthDate > marriageDate:
                    line = lines[f"{index}: Married date set"]
                    result_2_str = f"ERROR: FAMILY: US02: {line}: {wifeID}: Wife's birth date {wifeBirthDate} is after marriage date {marriageDate}"
                    resultList.append(result_2_str)

    # Print the information of validated data
    # for output in resultList:
    #     print(output)

    # return the list of validated data
    return resultList
###################End of userStory02 ##################

'''
User Story 03:
Requirement: Birth date should be before death date for all people.
Author: Erick
'''
def userStory03(file):
    indiDict, famDict, lines = processGedFile(file)
    resultList = list()

    for index in indiDict:

        individual = indiDict[index]

        if (individual.Get_death() == "NA"):
            continue
        deathDate = individual.Get_death()
        birthDate = individual.Get_birthday()

        if (deathDate< birthDate):
            line = lines[f"{index}: Death date set"]
            error = f"ERROR: INDIVIDUAL: US03: {line}: {individual.Get_ID()} Death date occurs before birth date - Birth {individual.Get_birthday()}: Death {individual.Get_death()}"
            # print(error)
            resultList.append(error)
            continue

    # Print the information of validated data
    # for output in resultList:
    #     print(output)

    resultList.sort()
    # return the list of validated data
    return resultList


'''
User Story 04:
Requirement: Marriage date should be before divorce date for all marriages.
Author: Erick
'''
def userStory04(file):
    indiDict,famDict, lines = processGedFile(file)
    resultList = list()

    for index in famDict:
        family = famDict[index]
        if (family.Get_divorced() == "NA"):
            continue
        divDate = family.Get_divorced()
        marrDate = family.Get_married()

        if (divDate < marrDate):
            line = lines[f"{index}: Divorced date set"]
            error = f"ERROR: FAMILY: US04: {line}: {family.Get_ID()} Divorce date occurs before marriage date - Marriage {family.Get_married()}: Divorce {family.Get_divorced()}"
            resultList.append(error)
            continue

    # Print the information of validated data
    # for output in resultList:
    #     print(output)

    resultList.sort()
    # return the list of validated data
    return resultList

'''
User Story 05:
Requirement: Marriage date should be before death date for people in marriages.
Author: Pratim Patel
'''
def userStory05(file):
    indiDict,famDict, lines = processGedFile(file)
    WisDead = False
    HisDead = False
    resultList = list()


    for key in famDict:
        family = famDict[key]
        familyID = family.Get_ID()

        if(famDict[key] != 'NA'):
            husbandID = str(famDict[familyID].Get_husbandID())
            wifeID = str(famDict[familyID].Get_wifeID())
            if(husbandID != 'NA' and wifeID != 'NA'):
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
                    line = lines[f"{key}: Married date set"]
                    result_1_str = f"ERROR: FAMILY: US05: {line}: wedding occurs after wife death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Wife Death: " + str(wifeDeath)
                    resultList.append(result_1_str)

                if(HisDead and marriedDate>husbandDeath):
                   # print("the husband is dead and the wedding date is after death")
                    line = lines[f"{key}: Married date set"]
                    result_1_str = f"ERROR: FAMILY: US05: {line}: wedding occurs after husband death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Husband Death: " + str(husbandDeath)
                    resultList.append(result_1_str)

    return resultList

'''
User Story 06:
Requirement: Divorce date should be before death date for people in marriages.
Author: Pratim Patel
'''
def userStory06(file):
    indiDict,famDict, lines = processGedFile(file)
    WisDead = False
    HisDead = False
    resultList = list()


    for key in famDict:
        family = famDict[key]
        familyID = family.Get_ID()

        if(famDict[key] != 'NA'):
            husbandID = str(famDict[familyID].Get_husbandID())
            wifeID = str(famDict[familyID].Get_wifeID())

            if(husbandID != 'NA' and wifeID != 'NA'):
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

                    if(WisDead and divorcedDate > wifeDeath):
                        #print("the wife is dead and the divorce date is after death")
                        line = lines[f"{familyID}: Divorced date set"]
                        result_1_str = f"ERROR: FAMILY: US06: {line}: divorce occurs after wife death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Wife Death: " + str(wifeDeath)
                        resultList.append(result_1_str)

                    if(HisDead and divorcedDate>husbandDeath):
                       # print("the husband is dead and the divorce date is after death")
                        line = lines[f"{familyID}: Divorced date set"]
                        result_1_str = f"ERROR: FAMILY: US06: {line}: divorce occurs after husband death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Husband Death: " + str(husbandDeath)
                        resultList.append(result_1_str)

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
    indiDict,famDict,lines = processGedFile(file)
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
        if individualAge != "NA":
            if(individualAge >= 150):
                # Check if an individual is alive or not
                if (isIndiAlive == False):
                    #error 1
                    line = lines[f"{individualID}: Birthday set"]
                    result_1_str = f"ERROR: INDIVIDUAL: US07: {line}: {individualID} More than 150 years old at death - Birth {birthDate}: Death {deathDate}"
                    resultList.append(result_1_str)
                else:
                    # error 2
                    line = lines[f"{individualID}: Birthday set"]
                    result_2_str = f"ERROR: INDIVIDUAL: US07: {line}: {individualID} More than 150 years old - Birth date {birthDate}"
                    resultList.append(result_2_str)

    # Print the information of validated data
    # print_list(resultList)

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
    indiDict, famDict, lines = processGedFile(file)

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

        if children == "NA":
            continue

        # iterate through children
        for i in children:
            # get each child's bday
            childBday = indiDict[i].Get_birthday()

            # check if they were married
            if marriage != 'NA':
                # check if marriage was after the childs bday
                if marriage > childBday:
                    line = lines[f"{index}: Married date set"]
                    result_1_str = f"ANOMALY: FAMILY: US08: {line}: {famid}: Child {i} born {childBday} before marriage on {marriage}"
                    resultList.append(result_1_str)

            # check if they were divorced
            if divorce != 'NA':
                # check to see if the child's bday was not more than 9 months after their divorce
                if months_between(divorce, childBday) > 9:
                    line = lines[f"{index}: Married date set"]
                    result_2_str = f"ANOMALY: FAMILY: US08: {line}: {famid}: Child {i} born {childBday} after divorce on {divorce}"
                    resultList.append(result_2_str)

    # Print the information of validated data
    # print_list(resultList)

    resultList.sort()
    # return the list of validated data
    return resultList

###################End of userStory08 ##################

'''
User story 09:
Requirement: Birth date should not be after death of parents
Author: Pair Programmed: Zach and Pratim
'''

def userStory09(file):

    # get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    #iterate through families
    for family_id, family in families.items():

        #iterate through families that are married
        if family.Get_married() != "NA":

            #get husband and wife and their deaths
            husband, husband_death_date, wife, wife_death_date = get_husband_and_wife_dates(family, individuals, "death")

            #get children of family
            children = family.Get_children()

            if children == 'NA':
                continue

            #iterate through each child
            if len(children) > 0 and (wife_death_date != "NA" and husband_death_date != "NA"):

                #iterate through children
                for child in children:

                    # get each child birthdate
                    child_birthdate = individuals[child].Get_birthday()

                    #check if death date is before child birthdate
                    if husband_death_date < child_birthdate:
                        line = lines[f"{husband}: Death date set"]
                        resultsList.append(f"ERROR: FAMILY: US09: {line}: {family_id}: Husband ({husband}) died {husband_death_date} before child's ({child}) birth {child_birthdate}")
                    if wife_death_date < child_birthdate:
                        line = lines[f"{wife}: Death date set"]
                        resultsList.append(f"ERROR: FAMILY: US09: {line}: {family_id}: Wife ({wife}) died {wife_death_date} before child's ({child}) birth {child_birthdate}")

    #print each output in the list and return list
    # print_list(resultsList)
    return resultsList

###################End of userStory09 ##################

'''
User story 10:
Requirement: Marriage should not occur prior to the age of 14
Author: Zach
'''

def userStory10(file):

    # get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    #iterate through families
    for family_id, family in families.items():

        #iterate through families that are married
        if family.Get_married() != "NA":

            #get husband and wife and birth dates
            husband, husband_birth_date, wife, wife_birth_date = get_husband_and_wife_dates(family, individuals, "birth")

            #get married date
            family_marriage_date = family.Get_married()

            #determine if husband or wife was married after 14 and output a message if not
            if float(relativedelta(family_marriage_date, husband_birth_date).years) < float(14):
                line = lines[f"{family_id}: Married date set"]
                resultsList.append(f"ERROR: FAMILY: US10: {line}: {family_id}: Husband ({husband}) birth date {husband_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")
            if float(relativedelta(family_marriage_date, wife_birth_date).years) < float(14):
                line = lines[f"{family_id}: Married date set"]
                resultsList.append(f"ERROR: FAMILY: US10: {line}: {family_id}: Wife ({wife}) birth date {wife_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")

    #print each output in the list and return list
    # print_list(resultsList)
    return resultsList

###################End of userStory10 ##################

'''
User story 11:
Requirements: Marriage should not occur during marriage to another spouse
Author: Avaneesh Kolluri
'''

def userStory11(file):
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    for user_id in individuals.items():
        user_id = user_id[0]
        relative_families = individuals[user_id].Get_spouse()
        marriages = []
        if relative_families == 'NA':
            continue
        for fam in relative_families:
            family = families[fam]
            marriages.append((family.Get_married(), family.Get_divorced()))
        while ('NA', 'NA') in marriages:
            marriages.remove(('NA', 'NA'))
        for i in range(len(marriages)-1):
            if len(marriages) == 1:
                break
            for index, date in zip(range(len(marriages)), marriages):
                for s_index, s_date in zip(range(len(marriages)), marriages):
                    if index != s_index:
                        m1,d1 = date
                        m2, d2 = s_date
                        #print(m1,m2,d1)
                        if d2 == d1:
                            line = lines[f"{fam}: Married date set"]
                            string = f"ERROR: FAMILY: US11: {line}: {fam}: Marriage {m1} should not be happening during another marriage {m2}."
                            if string not in resultsList:
                                resultsList.append(string)
                        elif (d1 != "NA"):
                            if(m1 < m2 < d1):
                                line = lines[f"{fam}: Married date set"]
                                string = f"ERROR: FAMILY: US11: {line}: {fam}: Marriage {m2} should not be happening during another marriage {m1}."
                                if string not in resultsList:
                                    resultsList.append(string)
    # print_list(resultsList)
    return resultsList

###################End of userStory11 ##################

'''
User story 12:
Requirements: Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
Author: Avaneesh Kolluri
'''

def userStory12(file):

    individuals, families, lines = processGedFile(file)
    resultsList = list()


    for user_id in individuals.items():

        user_id = user_id[0]
        children_fam = individuals[user_id].Get_spouse()
        if children_fam == "NA":
            continue
        gender = individuals[user_id].Get_gender()
        parent_bday = individuals[user_id].Get_birthday()
        for each in children_fam:
            if families[each].Get_children() == 'NA':
                continue
            for child in families[each].Get_children():
                child_bday = individuals[child].Get_birthday()
                if gender == 'M':
                    if exactDateDifference(child_bday, parent_bday).years >=80:
                        line = lines[f"{user_id}: Birthday set"]
                        resultsList.append(f"ERROR: INDIVIDUAL: US12: {line}: {user_id}: Father {user_id} is more than 80 years older than his child ({child}): {individuals[child].Get_name()}.")
                else:
                    if exactDateDifference(child_bday, parent_bday).years >=60:
                        line = lines[f"{user_id}: Birthday set"]
                        resultsList.append(f"ERROR: INDIVIDUAL: US12: {line}: {user_id}: Mother {user_id} is more than 60 years older than her child ({child}): {individuals[child].Get_name()}.")
    resultsList.sort()
    # print_list(resultsList)
    return resultsList

###################End of userStory12 ##################

'''
User story 13:
Requirements: Siblings should be either on (nearly) the same day or more than 8 months apart.
Author: Erick
'''

def userStory13(file):

    indiDict,famDict, lines = processGedFile(file)
    resultList = list()

    for index in famDict:
        family = famDict[index]
        famID = family.Get_ID()

        children = family.Get_children()

        if children == "NA":
            continue

        if (len(children) < 2):
            continue
        children = list(children)
        children.sort()

        x = 0
        while (x < len(children)-1):
            child1 = indiDict[children[x]]

            y = x + 1
            while (y < len(children)):
                child2 = indiDict[children[y]]
                birth1 = child1.Get_birthday()
                birth2 = child2.Get_birthday()

                diffMonths = abs(months_between(birth1,birth2))
                diffDays = (birth1 - birth2).days
                invDiffDays = (birth2 - birth1).days
                if (diffMonths < 8):
                    if (diffDays > 1 or invDiffDays > 1):
                        child1_ID = child1.Get_ID()
                        child2_ID = child2.Get_ID()
                        line = lines[f"{child2_ID}: Birthday set"]
                        # print(lines[f"{child2_ID}: ID set"])
                        # print(line)
                        resultList.append(f"ERROR: INDIVIDUAL: US13: {line}: Family {famID} has two children ({child1_ID}, {child2_ID}) with implausible birth dates ({birth1}, {birth2})")
                y += 1
            x += 1

    resultList.sort()
    # print_list(resultList)
    return resultList
###################End of userStory13 ##################

'''
User story 14:
Requirements: Family cannot birth more than 5 people in one day.
Author: Erick
'''

def userStory14(file):

    indiDict,famDict,lines = processGedFile(file)
    resultList = list()

    for index in famDict:
        family = famDict[index]
        famID = family.Get_ID()

        children = family.Get_children()
        if (len(children) < 5):
            continue
        children = list(children)
        children.sort()
        errorChildren = []
        while len(children)>=5:
            initialAge = indiDict[children[0]].Get_age()
            currentErrorChildren = []
            count = 0
            for ID in children:
                if ID in errorChildren:
                    continue
                child = indiDict[ID]
                if child.Get_age() == initialAge:
                    currentErrorChildren.append(ID)
                    count+= 1
            if count >= 5:
                for entry in currentErrorChildren:
                    if not entry in errorChildren:
                        errorChildren.append(entry)
                line = lines[f"{famID}: {errorChildren[len(errorChildren) - 1]} added to children"]
                resultList.append(f"ERROR: FAMILY: US14: {line}: Family {famID} has {str(count)} children {errorChildren} born at the same time with age {str(initialAge)}.")
                break
            children = children[1:]


    resultList.sort()
    # print_list(resultList);
    return resultList
###################End of userStory14 ##################
'''
User story 15:
Requirement: There must be fewer than 15 siblings
Author: Pratim
'''
def userStory15(file):
    indiDict,famDict, lines = processGedFile(file)

    resultsList = list()

    for familyID in famDict:
        children = famDict[familyID].Get_children()
        if(len(children)>=15):
            line = lines[f"{familyID}: {children[len(children)-1]} added to children"]
            resultsList.append(f"ERROR: FAMILY: US15: {line}: There must be fewer than 15 siblings. {familyID} has more than 15 siblings. {len(children)} >= 15.")
    return resultsList
###################End of userStory15 ##################

'''
User story 16:
Requirement: Find male last names
Author: Pratim
'''

def userStory16(file):
    indiDict, famDict, lines = processGedFile(file)
    resultsList = list()

    for indID in indiDict:
        if(indiDict[indID].Get_gender() == "M"):
           name = indiDict[indID].Get_name()
           x = name.split(" ")
           last_name = x[1]
           resultsList.append(last_name)
    result = all(elem == resultsList[0] for elem in resultsList)
    if(result == True):
        return ['All members have the same last name']
    else:
        last = [elem for elem in resultsList if elem != resultsList[0]]
        individual = [individual.Get_ID() for individual in indiDict.values() if individual.Get_name() != "NA" and individual.Get_name().split(" ")[1] == last[0] and individual.Get_gender() == "M"]
        line = lines[f"{individual[0]}: First and last name set"]
        return [f'ERROR: FAMILY: US16: {line}: All male members should have the same last name']

###################End of userStory16 ##################
'''
User story 17:
Requirement: Parents should not marry any of their descendants
Note: Parents shouldn't marry their children
Author: Srikanth
'''
def userStory17(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict, lines = processGedFile(file)

    # Create a list of
    resultsList = list()

    # Loop through all families
    for familyID in famDict:
        # fetch all the children in a family
        children = famDict[familyID].Get_children()

        # Ignore the below process if the no children in a family
        if children == 'NA':
            continue
        # For each child in a family
        for child in children:
            # Fetch all the families of a child's spouse
            if indiDict[child].Get_spouse():
                if indiDict[child].Get_spouse() != 'NA':
                    spouseFamilies = indiDict[child].Get_spouse()
                else:
                    continue
                # For each family of a child's spouse
                for spouseFamily in spouseFamilies:
                    # Check if the child's spouse is his mother, if so capture the error
                    if indiDict[child].Get_gender() != 'NA':
                        if indiDict[child].Get_gender() == 'M':
                            if famDict[spouseFamily].Get_wifeID() != 'NA':
                                spouseID = famDict[spouseFamily].Get_wifeID()
                            if famDict[familyID].Get_wifeID() != 'NA':
                                childMother = famDict[familyID].Get_wifeID()
                            if spouseID == childMother:
                                line = lines[f"{spouseFamily}: Wife ID set"]
                                result_1_str = f"ERROR: FAMILY: US17: {line}: {famDict[familyID].Get_ID()} Parents should not marry their descendants"
                                resultsList.append(result_1_str)

                        else:
                            # Check if the child's spouse is her father, if so capture the error
                            if famDict[spouseFamily].Get_husbandID() != 'NA':
                                spouseID = famDict[spouseFamily].Get_husbandID()
                            if famDict[familyID].Get_husbandID() != 'NA':
                                childFather = famDict[familyID].Get_husbandID()
                            if spouseID == childFather:
                                line = lines[f"{spouseFamily}: Husband ID set"]
                                result_1_str = f"ERROR: FAMILY: US17: {line}: {famDict[familyID].Get_ID()} Parents should not marry their descendants"
                                resultsList.append(result_1_str)

    # Print the information of validated data
    # print_list(resultsList)

    # Return error List
    return resultsList

###################End of userStory17 ##################
'''
User story 18:
Requirement: Siblings should not marry one another
Author: Srikanth
'''

def userStory18(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict, lines = processGedFile(file)

    # Create a list of
    resultsList = list()

    # Capture lists of siblings marriage to avoid duplicates
    duplicateslist= list()
    # iterate through families
    for key, index in famDict.items():
        # Get Wife Id from family
        wifeID = famDict[key].Get_wifeID()
        # Get Husband Id from family
        husbandID = famDict[key].Get_husbandID()

        if wifeID != "NA" and husbandID != "NA":
            # Get wife's parent's Family ID
            wifeParentFamID = indiDict[wifeID].Get_child()
            # Get husband's parent's Family ID
            HusbandParentFamID = indiDict[husbandID].Get_child()

            # Check If both parent ID 's are matching, if so siblings got married
            if wifeParentFamID == HusbandParentFamID and wifeParentFamID != "NA" and HusbandParentFamID != "NA":
                if wifeID not in duplicateslist:
                    # Record error if a person's Family ID is equal to a sibling's family ID, this means both are married
                    line = lines[f"{key}: ID set"]
                    result_1_str = f"ERROR: FAMILY: US18 : {line}: Sibling Id:{wifeID},name:{indiDict[wifeID].Get_name()} and Individual Id:{husbandID},name:{indiDict[husbandID].Get_name()} are married"
                    resultsList.append(result_1_str)
                    duplicateslist.append(wifeID)
            else:
                # Check if Half siblings got married
                if wifeParentFamID != "NA" and HusbandParentFamID != "NA":
                    # Get Husband's father's spouse ID
                    HusbFatherFamID = famDict[HusbandParentFamID[0]].Get_husbandID()
                    HusbFatherFamilies = indiDict[HusbFatherFamID].Get_spouse()
                    # Get Wifes's Mother's spouse ID
                    wifeMotherFamID = famDict[wifeParentFamID[0]].Get_wifeID()
                    wifeMotherFamilies = indiDict[wifeMotherFamID].Get_spouse()

                    # check if a person's father got married to a person's wife's mother.
                    for hubFatherFamily in HusbFatherFamilies:
                        for wifeMotherfamily in wifeMotherFamilies:
                            if hubFatherFamily == wifeMotherfamily and hubFatherFamily != "NA" and wifeMotherfamily != "NA":
                                if wifeID not in duplicateslist:
                                    line = lines[f"{key}: ID set"]
                                    result_1_str = f"ERROR: FAMILY: US18 : {line}: Sibling Id:{wifeID},name:{indiDict[wifeID].Get_name()} and Individual Id:{husbandID},name:{indiDict[husbandID].Get_name()} are married"
                                    resultsList.append(result_1_str)
                                    duplicateslist.append(wifeID)

                    # Get Husband's Mother's spouse ID
                    HusbMotherFamID = famDict[HusbandParentFamID[0]].Get_wifeID()
                    HusbMotherFamilies = indiDict[HusbMotherFamID].Get_spouse()
                    # Get Wifes's Father's spouse ID
                    wifeFatherFamID = famDict[wifeParentFamID[0]].Get_husbandID()
                    wifeFatherFamilies = indiDict[wifeFatherFamID].Get_spouse()

                    # check if a person's Mother got married to a person's wife's father.
                    for hubMotherfamily in HusbMotherFamilies:
                        for wifeFatherfamily in wifeFatherFamilies:
                            if hubMotherfamily == wifeFatherfamily and wifeFatherfamily != "NA" and hubMotherfamily != "NA":
                                if wifeID not in duplicateslist:
                                    line = lines[f"{key}: ID set"]
                                    result_1_str = f"ERROR: FAMILY: US18 : {line}: Sibling Id:{wifeID},name:{indiDict[wifeID].Get_name()} and Individual Id:{husbandID},name:{indiDict[husbandID].Get_name()} are married"
                                    resultsList.append(result_1_str)
                                    duplicateslist.append(wifeID)

    # Print the information of validated data
    # print_list(resultsList)

    # Return error List
    return resultsList

###################End of userStory18 ##################


'''
User story 19:
Requirements: First cousins cannot marry
Author: Zach
'''

def userStory19(file):

    #get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    #iterate through families
    for family_id, family in families.items():

        #check for marriage
        if family.Get_married() != "NA":

            #store wife and husband id
            husband = family.Get_husbandID()
            wife = family.Get_wifeID()

            #find family ID of husband and wife as child
            husband_family = individuals[husband].Get_child()
            wife_family = individuals[wife].Get_child()

            #find parents husband and wife
            if len(husband_family) != 0 and len(wife_family) != 0 and husband_family !='NA' and wife_family != 'NA':
                husband_father = families[husband_family[0]].Get_husbandID()
                husband_mother = families[husband_family[0]].Get_wifeID()
                wife_father = families[wife_family[0]].Get_husbandID()
                wife_mother = families[wife_family[0]].Get_wifeID()

                #find families as children for each parent
                husband_father_family = individuals[husband_father].Get_child()
                husband_mother_family = individuals[husband_mother].Get_child()
                wife_father_family = individuals[wife_father].Get_child()
                wife_mother_family = individuals[wife_mother].Get_child()

                #check if any of the familes are equal
                if husband_father_family == wife_father_family:
                    if husband_father_family != "NA":
                        line = lines[f"{family_id}: Wife ID set"]
                        resultsList.append(f"ERROR: FAMILY: US19: {line}: {family_id}: First cousins {husband} and {wife} married. Children of siblings {husband_father} and {wife_father}.")
                elif husband_father_family == wife_mother_family:
                    if husband_father_family != "NA":
                        line = lines[f"{family_id}: Wife ID set"]
                        resultsList.append(f"ERROR: FAMILY: US19: {family_id}: First cousins {husband} and {wife} married. Children of siblings {husband_father} and {wife_mother}.")
                elif husband_mother_family == wife_father_family:
                    if husband_mother_family != "NA":
                        line = lines[f"{family_id}: Wife ID set"]
                        resultsList.append(f"ERROR: FAMILY: US19: {family_id}: First cousins ({husband}) and {wife} married. Children of siblings {husband_mother} and {wife_father}.")
                elif husband_mother_family == wife_mother_family:
                    if husband_mother_family != "NA":
                        line = lines[f"{family_id}: Wife ID set"]
                        resultsList.append(f"ERROR: FAMILY: US19: {family_id}: First cousins {husband} and {wife} married. Children of siblings {husband_mother} and {wife_mother}.")

    #print each output in the list and return list
    # print_list(resultsList)
    resultsList.sort()
    return resultsList

###################End of userStory19 ##################

'''
User story 20:
Requirement: Aunts and uncles cannot marry their nephews and nieces
Author: Zach
'''

def userStory20(file):

    # get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    # iterate through families and check for marriage
    for family_id, family in families.items():
        if family.Get_married() != "NA":

            #store husband and wife ID
            husband = family.Get_husbandID()
            wife = family.Get_wifeID()

            #get families of husband and wife as children
            husband_family = individuals[husband].Get_child()
            wife_family = individuals[wife].Get_child()

            #get children (other siblings of each spouse)
            if len(husband_family) != 0 and len(wife_family) != 0 and husband_family !='NA' and wife_family != 'NA':
                husband_family = husband_family[0]
                wife_family = wife_family[0]
                husband_siblings = families[husband_family].Get_children()
                husband_siblings = [child for child in husband_siblings if child != husband]
                wife_siblings = families[wife_family].Get_children()
                wife_siblings = [child for child in wife_siblings if child != wife]

                #iterate through husband_siblings and get each of their children
                if len(husband_siblings) > 0:
                    for sibling in husband_siblings:
                        sibling_spouses = individuals[sibling].Get_spouse()
                        if sibling_spouses != 'NA':
                            #iterate through each family of the siblings and get the children
                            for family in sibling_spouses:
                                sibling_children = families[family].Get_children()

                                #check if wife ID in children
                                if wife in sibling_children:
                                    line = lines[f"{family_id}: Wife ID set"]
                                    resultsList.append(f"ERROR: FAMILY: US20: {line}: {family_id}: Husband ({husband}) married niece ({wife})")

                #iterate through wife_siblings and get each of their children
                if len(wife_siblings) > 0:
                    for sibling in wife_siblings:
                        sibling_spouses = individuals[sibling].Get_spouse()

                        if sibling_spouses != 'NA':
                            #iterate through each family of the siblings and get the children
                            for family in sibling_spouses:
                                sibling_children = families[family].Get_children()

                                #check if wife ID in children
                                if husband in sibling_children:
                                    line = lines[f"{family_id}: Husband ID set"]
                                    resultsList.append(f"ERROR: FAMILY: US20: {line}: {family_id}: Wife ({wife}) married nephew ({husband})")

    #print each output in the list and return list
    # print_list(resultsList)
    return resultsList

###################End of userStory20 ##################

'''
User story 21:
Requirement: Husband in family should be male and wife in family should be female
Author: Avaneesh
'''

def userStory21(file):

    # get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    for fam in families:
        #print(fam)
        #return
        #fam_id = fam[0][0]
        fclass = families[fam]

        husb_id = fclass.Get_husbandID()
        wife_id = fclass.Get_wifeID()
        if husb_id != 'NA':
            male = individuals[husb_id].Get_gender()
            if male != 'M':
                line = lines[f"{husb_id}: Gender set"]
                resultsList.append(f"ERROR: FAMILY: US21: {line}: {fam}: Husband ({husb_id}) is labelled incorrectly as ({male}).")
        if wife_id != 'NA':
            female = individuals[wife_id].Get_gender()
            if female != 'F':
                line = lines[f"{wife_id}: Gender set"]
                resultsList.append(f"ERROR: FAMILY: US21: {line}: {fam}: Wife ({wife_id}) is labelled incorrectly as ({female}).")

    #print each output in the list and return list
    # print_list(resultsList)
    return resultsList

###################End of userStory21 ##################

'''
User story 22:
Requirement: All individual IDs should be unique and all family IDs should be unique
Author: Avaneesh
'''

def userStory22(file):

    # get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()
    ind = individuals["DupI_ID"].Get_DupliID()

    fad = families["DupliID_fam"].Get_DupliID_fam()
    #print each output in the list and return list
    # print_list(resultsList)
    if ind != 'NA':
        line_numbers = lines["Duplicate Ind"]
        resultsList.append(f"ERROR: INDIVIDUAL: US22: {line_numbers}: The following are duplicate individual ID's {ind}.")

    if fad != 'NA':
        line_numbers = lines["Duplicate Fam"]
        resultsList.append(f"ERROR: FAMILY: US22: {line_numbers}: The following are duplicate individual ID's {fad}.")

    # print_list(resultsList)
    return (resultsList)
###################End of userStory22 ##################
'''
User story 23:
Requirement: All individuals must have a unique name and birth date pair.
Author: Erick
'''

def userStory23(file):

    indiDict, famDict, lines = processGedFile(file)
    indiList = []
    resultList = list()

    for index in indiDict:
        indiList += [index]

    count = 0
    while count <= len(indiList)-2:
        tempIndi1 = indiDict[indiList[count]]

        temp = count + 1
        while temp <= len(indiList)-1:
            tempIndi2 = indiDict[indiList[temp]]
            if tempIndi1.Get_name() == tempIndi2.Get_name() and tempIndi1.Get_birthday() == tempIndi2.Get_birthday():
                indi_1 = tempIndi1.Get_ID()
                indi_2 = tempIndi2.Get_ID()
                indiBirth_2 = tempIndi2.Get_birthday()
                indiName_2 = tempIndi1.Get_name()
                line_1 = lines[f"{indi_2}: First and last name set"]
                line_2 = lines[f"{indi_2}: Birthday set"]
                resultList.append(f"ERROR: INDIVIDUAL: US23: {line_1}, {line_2}: Two individuals [{indi_1}, {indi_2}] have duplicate names and birthdays [{tempIndi1.Get_name()}, {tempIndi2.Get_birthday()}].")
            temp += 1
        count += 1

    resultList.sort()
    # print_list(resultList);
    return resultList
###################End of userStory23 ##################

'''
User story 24:
Requirement: All families must have a unique spouse pair.
Author: Erick
'''

def userStory24(file):

    indiDict, famDict, lines = processGedFile(file)
    famList = []
    resultList = list()

    for index in famDict:
        famList += [index]

    count = 0
    while count <= len(famList)-2:
        tempFam1 = famDict[famList[count]]
        tempFam1_Husb = tempFam1.Get_husbandName()
        tempFam1_Wife = tempFam1.Get_wifeName()
        temp = count + 1
        while temp <= len(famList)-1:
            tempFam2 = famDict[famList[temp]]
            tempFam2_Husb = tempFam2.Get_husbandName()
            tempFam2_Wife = tempFam2.Get_wifeName()
            if tempFam1_Husb == tempFam2_Husb and tempFam1_Wife == tempFam2_Wife :
                fam_1 = tempFam1.Get_ID()
                fam_2 = tempFam2.Get_ID()
                line_1 = (lines[f"{fam_1}: Husband ID set"], lines[f"{fam_1}: Wife ID set"])
                line_2 = (lines[f"{fam_2}: Husband ID set"], lines[f"{fam_2}: Wife ID set"])
                resultList.append(f"ERROR: FAMILY: US24: {line_1} and {line_2}: Two families [{fam_1}, {fam_2}] have duplicate spouses [{tempFam1_Husb}, {tempFam2_Wife}].")
            temp += 1
        count += 1

    resultList.sort()
    # print_list(resultList);
    return resultList

###################End of userStory24 ##################

'''
User story 25:
Requirement: No more than one child with the same name and bday should appear in a family
Author: Pratim
'''


def userStory25(file):
    indiDict,famDict, lines = processGedFile(file)
    resultsList = list()

    for familyID in famDict:
        #get list of children
        children = famDict[familyID].Get_children()
        #create a dictionary of child names and bdays
        childList = dict()
        if children != "NA":
            for child in children:
                name = indiDict[child].Get_name()
                #get the birthday of each child
                bday = indiDict[child].Get_birthday()
                x = name.split(" ")
                #get the first name of each child
                first_name = x[0]
                if first_name in childList:
                    if childList[first_name] == bday:
                        line = (lines[f"{child}: First and last name set"], lines[f"{child}: Birthday set"])
                        resultsList.append(f"ERROR: INDIVIDUAL: US25: {line}: Individual  {name} is a duplicate name with duplicate Birthday {bday}.")
                else:
                    childList[first_name] = bday
    return resultsList
###################End of userStory25 ##################

'''
User story 26:
Requirement: All family roles in the individual record should have corresponding records in the corresponding family records
Author: Pratim
'''
#grab each individual

#go through each family to ensure that individual is part of a family

#get child and get spouse refer to the family id of what fam they are a child or spouse of

#do spouses first, then do children in separate lists
def userStory26(file):
    indiDict,famDict, lines = processGedFile(file)
    resultsList = list()
    indSpouses = list() #list of ids of those who are spouses
    indChildren = list()#list of ids of those who are children
    hubVer = False
    wifeVer = False
    isGood = True
    for indID in indiDict:
        if(indiDict[indID].Get_spouse() != 'NA'):
            indSpouses.append(indID)
    for indID in indiDict:
        if(indiDict[indID].Get_child() != 'NA'):
            indChildren.append(indID)

    for ind in indSpouses:
        famID = indiDict[ind].Get_spouse() #id of the family of the spouse
        famIDD = famID[0]
        #checks if they are husband or wife in family
        husID = famDict[famIDD].Get_husbandID()
        wifeID = famDict[famIDD].Get_wifeID()
        if(ind == husID):
            hubVer = True
        if(ind == wifeID):
            wifeVer = True
        if(ind != husID and ind != wifeID):
            line = lines[f"{ind}: {famIDD} spouse set"]
            resultsList.append(f"ERROR: INDIVIDUAL: US26: {line}: Individual  {ind} does not correspond to any spouse in Family")


    for ind in indChildren:
        famID = indiDict[ind].Get_child() #id of the family of the child
        famIDD = famID[0]
        #check if ind exists within the family of the famid
        allChildren = famDict[famIDD].Get_children()
        if(ind not in allChildren):
            line = lines[f"{ind}: {famIDD} child set"]
            resultsList.append(f"ERROR: INDIVIDUAL: US26: {line}: Individual  {ind} does not correspond to any child in Family")



    return resultsList

###################End of userStory26 ##################

'''
User story 27:
Requirement: Include person's current age when listing individuals
Author: Srikanth
'''

def userStory27(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict, lines = processGedFile(file)
    # Create a list of
    resultsList = list()
    # Create a dictionary to accumulate each individual with their age
    indiAgeDict = {}
    # iterate through individual
    for key, index in indiDict.items():
        # Get Individual's name
        indiName = indiDict[key].Get_name()
        # Get Individual's age
        indiAge = indiDict[key].Get_age()
        if indiAge != "NA":
            # Accumulate all individuals with their age
            indiAgeDict[indiName] = indiAge
    # Collect all the list individual with their age
    result_1_str = f"LIST: US27 : List of individuals with their name and age are:{indiAgeDict}"
    resultsList.append(result_1_str)

    # Print the information of gathered data
    #print_list(resultsList)

    # Return error List
    return resultsList

###################End of userStory27 ##################

'''
User story 28:
Requirement: List siblings in families by decreasing age, i.e. oldest siblings first
Author: Srikanth
'''

def userStory28(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict, lines = processGedFile(file)
    # Create a list of
    resultsList = list()
    # array index to process each object
    arrayIndex = 0
    # iterate through families
    for key, index in famDict.items():
        # Get all children in a family
        siblingsList = famDict[key].Get_children()
        # Get Family ID
        familyID = famDict[key].Get_ID()
        # Create a dictionary object to accumulate all children based on ages
        siblingsAgeDict = dict()

        # Process only if a family has children
        if siblingsList != "NA":
            # For every child in siblings list, update the dictionary with age
            for indiPerson in siblingsList:
                siblingAge = indiDict[indiPerson].Get_age()
                siblingsAgeDict[indiPerson] = siblingAge
            # Sort the dictionary based on descending order of age of each sibling.
            sorted_x = sorted(siblingsAgeDict.items(), key=operator.itemgetter(1), reverse=True)
            keys = collections.OrderedDict(sorted_x).keys()
            # Family object to sort the order of siblings
            index.Children = keys
        # Collect the list of siblings from family object
        childrenData = list(famDict.values())[arrayIndex]
        # Increment the array for next iteration
        arrayIndex = arrayIndex+1
        # Fetch the Children data from family, this data is in descending order of age
        famChildrenData = childrenData.Get_children()

        # If a family has children fetch the data in a string to list all the siblings in descending order of their age
        if famChildrenData != "NA":
            # Record all siblings in a list
            result_1_str = f"LIST: US28: Family ID: {familyID} Siblings list in descending order of their age {list(famChildrenData)}"
            resultsList.append(result_1_str)

    # Print the information of gathered data
    #print_list(resultsList)

    # Return error List
    return resultsList

###################End of userStory28 ##################

'''
User story 29:
Requirement: List all deceased individuals in a GEDCOM File
Author: Zach
'''
def userStory29(file):

    # get individuals
    individuals = processGedFile(file)[0]
    resultsList = list()

    #iterate through individuals
    for individual_id, individual in individuals.items():
        if not individual.Get_alive():
            resultsList.append(f"INDIVIDUAL: US29: {individual.Get_name()} with id {individual_id} is deceased.")

    #print each output in the list and return list
    #print_list(resultsList)
    return (resultsList)

###################End of userStory29 ##################

'''
User story 30:
Requirement: List all living married people in a GEDCOM file
Author: Zach
'''

def userStory30(file):

    # get individuals and families in file, create results
    individuals = processGedFile(file)[0]
    families = processGedFile(file)[1]
    resultsList = list()

    #iterate through families and find married couples and spouses
    for family_id, family in families.items():
        if family.Get_married() != "NA" and family.Get_divorced() == "NA":
            husband = families[family_id].Get_husbandID()
            wife = families[family_id].Get_wifeID()

            #get if both spouses are alive to append to the list
            if individuals[husband].Get_alive() and individuals[wife].Get_alive():
                resultsList.append(f"INDIVIDUAL: US30: {individuals[husband].Get_name()}, with id {husband}, and {individuals[wife].Get_name()}, with id {wife}, are married and both alive.")

    #print each output in the list and return list
    #print_list(resultsList)
    return (resultsList)

###################End of userStory30 ##################

'''
User story 31:
Requirement: List all living people over 30 who have never been married in a GEDCOM file
Author: Avaneesh
'''

def userStory31(file):

    # get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    for ind in individuals:
        if individuals[ind].Get_alive():
            if individuals[ind].Get_age() != 'NA':
                if individuals[ind].Get_age() > 30:
                    if individuals[ind].Get_spouse() == 'NA':
                        resultsList.append(f"INDIVIDUAL: US31: {individuals[ind].Get_name()} with id {ind} is living, over 30, and never has been married.")

    #print each output in the list and return list
    #print_list(resultsList)
    #print(resultsList)
    return (resultsList)

###################End of userStory31 ##################

'''
User story 32:
Requirement: List all multiple births in a GEDCOM file
Author: Avaneesh
'''

def userStory32(file):
    # get individuals and families in file, create results
    individuals, families, lines = processGedFile(file)
    resultsList = list()

    for fam in families:
        children = families[fam].Get_children()
        record = {}
        if children == 'NA':
            continue
        for child in children:
            bday = individuals[child].Get_birthday()
            if bday in record:
                record[bday] += [child]
            else:
                record[bday] = [child]
        for i in record:
            if len(record[i]) > 1:
                resultsList.append(f"FAMILY: US32: Individuals with IDs {record[i]} are multiple births.")

    #print each output in the list and return list
    #print_list(resultsList)
    return (resultsList)

###################End of userStory32 ##################

'''
User story 33:
Requirement: List all orphans (Age < 18, Parents dead).
Author: Erick
'''

def userStory33(file):

    indiDict, famDict, lines = processGedFile(file)
    resultList = list()

    for index in famDict:
        if (index == "DupliID_fam"):
            continue;
        fam = famDict[index];
        if not (fam.Get_husbandID() != 'NA' and fam.Get_wifeID() != 'NA'):
            continue;
        husband = indiDict[fam.Get_husbandID()]
        wife = indiDict[fam.Get_wifeID()]

        if not (husband.Get_death() != 'NA' and wife.Get_death() != 'NA'):
            continue;

        if (wife.Get_death() > husband.Get_death()):
            death = wife.Get_death();
        else:
            death = husband.Get_death();

        children = fam.Get_children();
        if (children == 'NA'):
            continue;
        for c_index in children:
            child = indiDict[c_index];

            if (child.Get_death() != 'NA' and child.Get_death() < death):
                continue;
            #Found out the hard way there's no easy way to grab year differences in datetime. Oh well.
            birth = child.Get_birthday()
            b_year = child.Get_birthday().year
            age_years_at_death = death.year- birth.year
            if death.month < birth.month:
                age_years_at_death = age_years_at_death - 1;
            if death.month == death.month:
                if death.day <= birth.day:
                    age_years_at_death = age_years_at_death - 1;
            if (age_years_at_death <= 18):
                child_ID = child.Get_ID();
                fam_ID = fam.Get_ID();
                resultList.append(f"FAMILY: US33: Child [{child_ID}] is an orphan in family [{fam_ID}].");

    resultList.sort()
    # print_list(resultList);
    return resultList

'''
User story 34:
Requirement: List all orphans (Age < 18, Parents dead).
Author: Erick
'''

def userStory34(file):

    indiDict, famDict, lines = processGedFile(file)
    resultList = list()

    for index in famDict:
        if (index == "DupliID_fam"):
            continue;
        fam = famDict[index];
        if not (fam.Get_husbandID() != 'NA' and fam.Get_wifeID() != 'NA'):
            continue;
        husband = indiDict[fam.Get_husbandID()]
        wife = indiDict[fam.Get_wifeID()]
        husAge = yearDifference(fam.Get_married(),husband.Get_birthday());
        wifeAge = yearDifference(fam.Get_married(),wife.Get_birthday());

        if husAge <= wifeAge:
            smallAge = husAge;
            largeAge = wifeAge;
        else:
            smallAge = wifeAge;
            largeAge = husAge;

        doubleAge = smallAge*2;
        if (doubleAge > largeAge):
            continue;

        husID = husband.Get_ID();
        wifeID = wife.Get_ID();
        famID = fam.Get_ID();
        resultList.append(f"FAMILY: US34: Spouses in family [{famID}] have large age gap at marriage [{husID}, {husAge}], [{wifeID}, {wifeAge}].");

    resultList.sort()
    # print_list(resultList);
    return resultList

'''
User story 35:
Requirement: List recent births within 30 days.
Author: Pratim
'''
#go through each individual
# get their birthday
# if their birthday was within 30 days, add to results list

def userStory35(file):
    indiDict, famDict, lines = processGedFile(file)
    resultsList = list()
    today = date.today()
    EndDate = today - timedelta(days=30)
    for index in indiDict:
        individual = indiDict[index]
        bday = individual.Get_birthday()
        if(bday != 'NA' and bday>EndDate):
            resultsList.append(f"LIST: US35: Individuals who were born within 30 days: {individual.Get_name()}")
    return resultsList

###################End of userStory35 ##################
'''
User story 36:
Requirement: List recent deaths within 30 days.
Author: Pratim
'''

def userStory36(file):
    indiDict,famDict,lines = processGedFile(file)
    resultsList = list()
    today = date.today()
    EndDate = today - timedelta(days=30)
    for index in indiDict:
        individual = indiDict[index]
        if(individual.Get_death() != 'NA'):
            deathday = individual.Get_death()
            if(deathday>EndDate):
                resultsList.append(f"LIST: US36: Individuals who have died within 30 days: {individual.Get_name()}")
    return resultsList
'''
User story 37:
Requirement: List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days
Author: Srikanth
'''

def userStory37(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict, lines = processGedFile(file)
    # Create a list of
    resultsList = list()

    # iterate through families
    for key, index in famDict.items():
        # Get Husband and Wife ID
        husID = index.Get_husbandID()
        wifeID = index.Get_wifeID()
        if husID == 'NA' or wifeID == 'NA':
            continue
        # Fetch both husband and wife's death status
        isHubAlive = indiDict[husID].Get_alive()
        isWifeAlive  = indiDict[wifeID].Get_alive()
        # Check if one of the spouse is alive in a family
        if isHubAlive == 'NA' or isWifeAlive == 'NA':
            continue
        # Check if wife a is widow
        if isHubAlive is False and isWifeAlive is True:
            # check if husband dead in last 30 days
            if isWithinLast30days(indiDict[husID].Get_death()):
                # Fetch children id's if any
                childrenID = index.Get_children()
                if childrenID != 'NA':
                    # Construct a string to list all survivors with wife and children
                    result_1_str = f"LIST: US37: Survivors of Individual ID:{husID} in the last 30 days, Spouse ID:{wifeID}, and Children {childrenID}"
                else:
                    # Construct a string to list all survivors with wife and no children
                    result_1_str = f"LIST: US37: Survivors of Individual ID:{husID} in the last 30 days, Spouse ID:{wifeID} with no children"
                resultsList.append(result_1_str)
        # Check if husband a is widower
        if isHubAlive is True and isWifeAlive is False:
            # check if wife dead in last 30 days
            if isWithinLast30days(indiDict[wifeID].Get_death()):
                # Fetch children id's if any
                childrenID = index.Get_children()
                if childrenID != 'NA':
                    # Construct a string to list all survivors with husband and children
                    result_2_str = f"LIST: US37: Survivors of Individual ID:{wifeID} in the last 30 days, Spouse ID:{husID}, and Children {childrenID}"
                else:
                    # Construct a string to list all survivors with husband and no children
                    result_2_str = f"LIST: US37: Survivors of Individual ID:{wifeID} in the last 30 days, Spouse ID:{husID} with no children"
                resultsList.append(result_2_str)

    # Print the information of gathered data
    # print_list(resultsList)

    # Return error List
    return resultsList

###################End of userStory37 ##################

'''
User story 38:
Requirement: List all living people in a GEDCOM file whose birthdays occur in the next 30 days
Author: Srikanth
'''

def userStory38(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict, lines = processGedFile(file)
    # Create a list of
    resultsList = list()

    # List to hold all individual name, if their birthday is within next 30days.
    next30BdayList = []
    # iterate through individuals
    for key, index in indiDict.items():
        # Is an Individual alive
        indiAlive = index.Get_alive()
        # Check if an individual is alive
        if indiAlive is True and indiAlive != 'NA':
            # Get the birthday and check if yes birthday is less than 30 days
            indiBday = index.Get_birthday()
            # Is the birthday date's day is in next 30 days ?
            if isBdayWithinNext30days(indiBday):
                 indiName = index.Get_name()
                 next30BdayList.append(indiName)

    if len(next30BdayList) > 0:
        # Record all siblings in a list
        result_1_str = f"LIST: US38: Individuals whose birthdays occur in the next 30 days: {next30BdayList}"
    else:
        # Output no individual's birthday in next 30 days.
        result_1_str = f"LIST: US38: No individual's birthday occur in the next 30 days"

    resultsList.append(result_1_str)

    # Print the information of gathered data
    # print_list(resultsList)

    # Return error List
    return resultsList

###################End of userStory38 ##################

'''
User story 39:
Requirement: List all upcoming anniversaries in a GEDCOM file
Author: Zach
'''

def userStory39(file):

    #retrieve dictionaries
    individuals, families, lines = processGedFile(file)

    #create empty list of upcoming anniversaries
    upcomingAnnis = list()

    #get today's date in month and day
    today = datetime.datetime.now()
    today = datetime.date(today.year, today.month, today.day)

    #iterate through married couples
    for family_id, family in families.items():
        if family.Get_married() != "NA":
            marriage_date = datetime.date(today.year, family.Get_married().month, family.Get_married().day)

            #check if marriage date is within 30 days of today
            if (marriage_date - today).days <= 30 and (marriage_date - today).days > 0:
                upcomingAnnis.append(f"FAMILY: US39: {family_id} has an upcoming anniversary on {family.Get_married().month}-{family.Get_married().day}.")

    #print each output in the list and return list
    #print_list(resultsList)
    return (upcomingAnnis)



# Sprint1n2n3n4 Main function


if __name__ == "__main__":
   userStory01("InputGedFiles/FamilyTree.ged")
   userStory02("InputGedFiles/FamilyTree.ged")
   userStory03("InputGedFiles/FamilyTree.ged")
   userStory04("InputGedFiles/FamilyTree.ged")
   userStory05("InputGedFiles/FamilyTree.ged")
   userStory06("InputGedFiles/FamilyTree.ged")
   userStory07("InputGedFiles/FamilyTree.ged")
   userStory08("InputGedFiles/FamilyTree.ged")
   userStory09("InputGedFiles/FamilyTree.ged")
   userStory10("InputGedFiles/FamilyTree.ged")
   userStory11("InputGedFiles/FamilyTree.ged")
   userStory12("InputGedFiles/FamilyTree.ged")
   userStory13("InputGedFiles/FamilyTree.ged")
   userStory14("InputGedFiles/FamilyTree.ged")
   userStory15("InputGedFiles/FamilyTree.ged")
   userStory16("InputGedFiles/FamilyTree.ged")
   userStory17("InputGedFiles/FamilyTree.ged")
   userStory18("InputGedFiles/FamilyTree.ged")
   userStory19("InputGedFiles/FamilyTree.ged")
   userStory20("InputGedFiles/FamilyTree.ged")
   userStory21("InputGedFiles/FamilyTree.ged")
   userStory22("InputGedFiles/FamilyTree.ged")
   userStory23("InputGedFiles/FamilyTree.ged")
   userStory24("InputGedFiles/FamilyTree.ged")
   userStory25("InputGedFiles/FamilyTree.ged")
   userStory26("InputGedFiles/FamilyTree.ged")
   userStory27("InputGedFiles/FamilyTree.ged")
   userStory28("InputGedFiles/FamilyTree.ged")
   userStory29("InputGedFiles/FamilyTree.ged")
   userStory30("InputGedFiles/FamilyTree.ged")
   userStory31("InputGedFiles/FamilyTree.ged")
   userStory32("InputGedFiles/FamilyTree.ged")
   userStory33("InputGedFiles/FamilyTree.ged")
   userStory34("InputGedFiles/FamilyTree.ged")
   userStory35("InputGedFiles/FamilyTree.ged")
   userStory36("InputGedFiles/FamilyTree.ged")
   userStory37("InputGedFiles/FamilyTree.ged")
   userStory38("InputGedFiles/FamilyTree.ged")
   userStory39("InputGedFiles/FamilyTree.ged")
