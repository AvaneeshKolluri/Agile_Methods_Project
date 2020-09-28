from project2 import processGedFile 
from dateutil.relativedelta import relativedelta
"""
Author: Zach George
User Story 10:
Age after 14 for a marriage
"""

def userStory10_marriage_after_14(file):
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
                resultsList.append(f"ERROR: Husband's birth date {husband_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")
            elif float(relativedelta(family_marriage_date, wife_birth_date).years) < float(14):
                resultsList.append(f"ERROR: Wife's birth date {wife_birth_date} not at least 14 years prior to marriage date {family_marriage_date}")
                
    return resultsList