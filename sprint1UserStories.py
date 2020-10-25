from project2 import processGedFile
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
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

def days_between(start_date, end_date):
    num_days
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
        if fam != 'NA':
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
        deathDate = individual.Get_death();
        birthDate = individual.Get_birthday();

        if (deathDate< birthDate):
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
        divDate = family.Get_divorced();
        marrDate = family.Get_married();

        if (divDate < marrDate):
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
User Story 05:
Requirement: Marriage date should be before death date for people in marriages.
Author: Pratim Patel
'''
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
                    result_1_str = "ERROR: FAMILY: US05: wedding occurs after wife death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Wife Death: " + str(wifeDeath)
                    resultList.append(result_1_str)

                if(HisDead and marriedDate>husbandDeath):
                   # print("the husband is dead and the wedding date is after death")
                    result_1_str = "ERROR: FAMILY: US05: wedding occurs after husband death. Wedding Date: " + str(famDict[familyID].Get_married()) + " Husband Death: " + str(husbandDeath)
                    resultList.append(result_1_str)

    return resultList

'''
User Story 06:
Requirement: Divorce date should be before death date for people in marriages.
Author: Pratim Patel
'''
def userStory06(file):
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
                        result_1_str = "ERROR: FAMILY: US06: divorce occurs after wife death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Wife Death: " + str(wifeDeath)
                        resultList.append(result_1_str)

                    if(HisDead and divorcedDate>husbandDeath):
                       # print("the husband is dead and the divorce date is after death")
                        result_1_str = "ERROR: FAMILY: US06: divorce occurs after husband death. Divorce Date: " + str(famDict[familyID].Get_divorced()) + " Husband Death: " + str(husbandDeath)
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
    indiDict,famDict = processGedFile(file)
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
    print_list(resultList)

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
                    result_1_str = f"ANOMALY: FAMILY: US08: {famid}: Child {i} born {childBday} before marriage on {marriage}"
                    resultList.append(result_1_str)

            # check if they were divorced
            if divorce != 'NA':
                # check to see if the child's bday was not more than 9 months after their divorce
                if months_between(divorce, childBday) > 9:
                    result_2_str = f"ANOMALY: FAMILY: US08: {famid}: Child {i} born {childBday} after divorce on {divorce}"
                    resultList.append(result_2_str)

    # Print the information of validated data
    print_list(resultList)

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
    individuals, families = processGedFile(file)
    resultsList = list()

    #iterate through families
    for family_id, family in families.items():

        #iterate through families that are married
        if family.Get_married() != "NA":

            #get husband and wife and their deaths
            husband, husband_death_date, wife, wife_death_date = get_husband_and_wife_dates(family, individuals, "death")

            #get children of family
            children = family.Get_children()

            #iterate through each child
            if len(children) > 0 and (wife_death_date != "NA" and husband_death_date != "NA"):

                #iterate through children
                for child in children:

                #get each child birthdate
                    child_birthdate = individuals[child].Get_birthday()

                    #check if death date is before child birthdate
                    if husband_death_date < child_birthdate:
                        resultsList.append(f"ERROR: FAMILY: US09: {family_id}: Husband ({husband}) died {husband_death_date} before child's ({child}) birth {child_birthdate}")
                    if wife_death_date < child_birthdate:
                        resultsList.append(f"ERROR: FAMILY: US09: {family_id}: Wife ({wife}) died {wife_death_date} before child's ({child}) birth {child_birthdate}")

    #print each output in the list and return list
    print_list(resultsList)
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
    for family_id, family in families.items():

        #iterate through families that are married
        if family.Get_married() != "NA":

            #get husband and wife and birth dates
            husband, husband_birth_date, wife, wife_birth_date = get_husband_and_wife_dates(family, individuals, "birth")

            #get married date
            family_marriage_date = family.Get_married()

            #determine if husband or wife was married after 14 and output a message if not
            if float(relativedelta(family_marriage_date, husband_birth_date).years) < float(14):
                resultsList.append(f"ERROR: FAMILY: US10: {family_id}: Husband ({husband}) birth date {husband_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")
            if float(relativedelta(family_marriage_date, wife_birth_date).years) < float(14):
                resultsList.append(f"ERROR: FAMILY: US10: {family_id}: Wife ({wife}) birth date {wife_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")

    #print each output in the list and return list
    print_list(resultsList)
    return resultsList

###################End of userStory10 ##################

'''
User story 13:
Requirements: Siblings should be either on (nearly) the same day or more than 8 months apart.
Author: Erick
'''

def userStory13(file):

    indiDict,famDict = processGedFile(file);
    resultList = list();

    for index in famDict:
        family = famDict[index]
        famID = family.Get_ID();

        children = family.Get_children();

        if children == "NA":
            continue

        if (len(children) < 2):
            continue;
        children = list(children);
        children.sort();

        x = 0;
        while (x < len(children)-1):
            child1 = indiDict[children[x]];

            y = x + 1;
            while (y < len(children)):
                child2 = indiDict[children[y]];
                birth1 = child1.Get_birthday();
                birth2 = child2.Get_birthday();

                diffMonths = abs(months_between(birth1,birth2));
                diffDays = (birth1 - birth2).days;
                invDiffDays = (birth2 - birth1).days
                if (diffMonths < 8):
                    if (diffDays > 1 or invDiffDays > 1):
                        child1_ID = child1.Get_ID();
                        child2_ID = child2.Get_ID();
                        resultList.append(f"ERROR: INDIVIDUAL: US13: Family {famID} has two children ({child1_ID}, {child2_ID}) with implausible birth dates ({birth1}, {birth2})")
                y += 1;
            x += 1;

    resultList.sort()
    print_list(resultList);
    return resultList
###################End of userStory13 ##################

'''
User story 14:
Requirements: Family cannot birth more than 5 people in one day.
Author: Erick
'''

def userStory14(file):

    indiDict,famDict = processGedFile(file);
    resultList = list();

    for index in famDict:
        family = famDict[index]
        famID = family.Get_ID();

        children = family.Get_children();
        if (len(children) < 5):
            continue;
        children = list(children);
        children.sort();
        errorChildren = [];
        while len(children)>=5:
            initialAge = indiDict[children[0]].Get_age();
            currentErrorChildren = [];
            count = 0;
            for ID in children:
                if ID in errorChildren:
                    continue;
                child = indiDict[ID];
                if child.Get_age() == initialAge:
                    currentErrorChildren.append(ID);
                    count+= 1;
            if count >= 5:
                for entry in currentErrorChildren:
                    if not entry in errorChildren:
                        errorChildren.append(entry);
                resultList.append(f"ERROR: FAMILY: US14: Family {famID} has {str(count)} children {errorChildren} born at the same time with age {str(initialAge)}.")
                break;
            children = children[1:];


    resultList.sort()
    print_list(resultList);
    return resultList
###################End of userStory14 ##################

'''
User story 17:
Requirement: Parents should not marry any of their descendants
Note: Parents shouldn't marry their children
Author: Srikanth
'''
def userStory17(file):
    # Fetch the parsed object's from input ged file
    indiDict, famDict = processGedFile(file)

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
                                result_1_str = f"ERROR: FAMILY: US17: {famDict[familyID].Get_ID()} Parents should not marry their descendants"
                                resultsList.append(result_1_str)

                        else:
                            # Check if the child's spouse is her father, if so capture the error
                            if famDict[spouseFamily].Get_husbandID() != 'NA':
                                spouseID = famDict[spouseFamily].Get_husbandID()
                            if famDict[familyID].Get_husbandID() != 'NA':
                                childFather = famDict[familyID].Get_husbandID()
                            if spouseID == childFather:
                                result_1_str = f"ERROR: FAMILY: US17: {famDict[familyID].Get_ID()} Parents should not marry their descendants"
                                resultsList.append(result_1_str)

    # Print the information of validated data
    print_list(resultsList)

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
    indiDict, famDict = processGedFile(file)

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
                    result_1_str = f"ERROR: FAMILY: US18 : Sibling Id:{wifeID},name:{indiDict[wifeID].Get_name()} and Individual Id:{husbandID},name:{indiDict[husbandID].Get_name()} are married"
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
                                    result_1_str = f"ERROR: FAMILY: US18 : Sibling Id:{wifeID},name:{indiDict[wifeID].Get_name()} and Individual Id:{husbandID},name:{indiDict[husbandID].Get_name()} are married"
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
                                    result_1_str = f"ERROR: FAMILY: US18 : Sibling Id:{wifeID},name:{indiDict[wifeID].Get_name()} and Individual Id:{husbandID},name:{indiDict[husbandID].Get_name()} are married"
                                    resultsList.append(result_1_str)
                                    duplicateslist.append(wifeID)

    # Print the information of validated data
    print_list(resultsList)

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
    individuals, families = processGedFile(file)
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
                        resultsList.append(f"ERROR: FAMILY: US19: {family_id}: First cousins {husband} and {wife} married. Children of siblings {husband_father} and {wife_father}.")
                elif husband_father_family == wife_mother_family:
                    if husband_father_family != "NA":
                        resultsList.append(f"ERROR: FAMILY: US19: {family_id}: First cousins {husband} and {wife} married. Children of siblings {husband_father} and {wife_mother}.")
                elif husband_mother_family == wife_father_family:
                    if husband_mother_family != "NA":
                        resultsList.append(f"ERROR: FAMILY: US19: {family_id}: First cousins ({husband}) and {wife} married. Children of siblings {husband_mother} and {wife_father}.")
                elif husband_mother_family == wife_mother_family:
                    if husband_mother_family != "NA":
                        resultsList.append(f"ERROR: FAMILY: US19: {family_id}: First cousins {husband} and {wife} married. Children of siblings {husband_mother} and {wife_mother}.")

    #print each output in the list and return list
    print_list(resultsList)
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
    individuals, families = processGedFile(file)
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
                                    resultsList.append(f"ERROR: FAMILY: US20: {family_id}: Husband ({husband}) married niece ({wife})")

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
                                    resultsList.append(f"ERROR: FAMILY: US20: {family_id}: Wife ({wife}) married nephew ({husband})")

    #print each output in the list and return list
    print_list(resultsList)
    return resultsList

###################End of userStory20 ##################

# Sprint1 Main function
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
   userStory13("InputGedFiles/FamilyTree.ged")
   userStory14("InputGedFiles/FamilyTree.ged")
   userStory17("InputGedFiles/FamilyTree.ged")
   userStory18("InputGedFiles/FamilyTree.ged")
   userStory19("InputGedFiles/FamilyTree.ged")
   userStory20("InputGedFiles/FamilyTree.ged")
