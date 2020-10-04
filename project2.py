#Team 2
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
import datetime
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable
from collections import OrderedDict
from individualClass import individualClass as indiClass
from familyClass import familyClass
import sys
import warnings

def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def from_dob_to_death(born,death):
    today = death
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def printTablesData(indiDict_obj, famDict_obj):
    indiTable = PrettyTable()
    familyTable = PrettyTable()

    indiTable.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    familyTable.field_names = ['ID','Married','Divorced','Husband ID', 'Husband Name', 'Wife ID','Wife Name', 'Children']

    for id in indiDict_obj:
        individualData = indiDict_obj[id]
        indiTable.add_row(individualData.Get_details())
        print(individualData.Get_details())
    for id in famDict_obj:
        famData = famDict_obj[id]
        familyTable.add_row(famData.Get_details())
    
    print("Individuals")
    print (indiTable)
    print("Families")
    print (familyTable)


def processGedFile(file_path):
    # Path to your `.ged` file
    #file_path ='FamilyTree.ged'

    #file_path ='gedcom'

    # Initialize the parser
    gedcom_parser = Parser()

    # Parse your file
    gedcom_parser.parse_file(file_path)

    root_elements = gedcom_parser.get_element_list()

    info = {"INDI": [], "FAM":[]}

    for element in root_elements:
       if str(element.get_tag()) == "INDI" or str(element.get_tag()) =="FAM":
           if element.get_tag() == "INDI" and len(info[element.get_tag()]) > 5000:
               raise ValueError("Too many individuals in file")
           if element.get_tag() == "FAM" and len(info[element.get_tag()]) >1000:
               raise ValueError("Too many families in file")

    months = {"JAN" : 1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9,"OCT":10,"NOV":11, "DEC":12}

    # Individual dictionary
    indiDict = OrderedDict()
    myTag = ""

    famDict = OrderedDict()
    famTag = ""
    isMarried = False
    isDivorced = False
    for element in root_elements:
        age = 0


        # Fetch Individual ID details
        if(element.get_level() == 0 and element.get_tag() == "INDI"):
            individualString = element.to_gedcom_string()
            individualString = individualString.replace('@','').strip().split(" ")

            #Fetch Individual ID tag
            myTag = individualString[1]

            indiDict[myTag] = indiClass(myTag)
            indiDict[myTag].Set_ID(myTag)

        # Fetch ans set Child ID details for individual
        if (element.get_level() == 1) and element.get_tag() == "FAMC" :
            childString = element.to_gedcom_string()
            childString = childString.replace('@','').strip().split(" ")
            indiDict[myTag].Set_child(childString[2])

        # Fetch ans set Spouse ID details for individual
        if (element.get_level() == 1) and element.get_tag() == "FAMS" :
            spouseString = element.to_gedcom_string()
            spouseString = spouseString.replace('@','').strip().split(" ")
            indiDict[myTag].Set_spouse(spouseString[2])

        if isinstance(element, IndividualElement):

            # Fetch and set the name
            (first, last) = element.get_name()
            indiDict[myTag].Set_name(str(first+ " " +last))

            # Fetch the Gender and set the gender
            indiDict[myTag].Set_gender(element.get_gender())

            # Check if individual is alive
            if(element.is_deceased() == True):

                # Set Alive status to false
                indiDict[myTag].Set_alive(False)

                # Fetch Birth and death dates
                bday = element.get_birth_data()[0]
                death = element.get_death_data()[0]

                # Format Dates in Day Month and Year
                bday = bday.split(" ")
                bday = datetime.date(int(bday[2]),int(months[bday[1]]), int(bday[0]))
                death = death.split(" ")
                death = datetime.date(int(death[2]),int(months[death[1]]), int(death[0]))

                # Set Birthday
                indiDict[myTag].Set_birthday(bday)
                # Set Death day
                indiDict[myTag].Set_death(death)
                # Calculate the age
                age = from_dob_to_death(bday, death)
                # Set Age
                indiDict[myTag].Set_age(age)

            else:
                # Set Alive status to true
                indiDict[myTag].Set_alive(True)
                # Fetch Birth dates
                bday = element.get_birth_data()[0].split(" ")
                bday = datetime.date(int(bday[2]),int(months[bday[1]]), int(bday[0]))
                # Set Birthday
                indiDict[myTag].Set_birthday(bday)
                # Calculate the age
                age = from_dob_to_age(bday)
                # Set Age
                indiDict[myTag].Set_age(age)

        if(element.get_level() == 0 and element.get_tag() == "FAM"):
            children = set()
            familyString = element.to_gedcom_string()
            familyString = familyString.replace('@','').strip().split(" ")
            famTag = familyString[1]
            famDict[famTag] = familyClass(famTag)
            famDict[famTag].Set_ID(famTag)
        if(element.get_level() == 1 and element.get_tag() == "MARR"):
            isMarried = True
        if(isMarried and element.get_tag()=="DATE" and element.get_level()==2):
            marriedDay = element.get_value()
            marriedDay = marriedDay.split(" ")
            marriedDay = datetime.date(int(marriedDay[2]),int(months[marriedDay[1]]), int(marriedDay[0]))
            famDict[famTag].Set_married(marriedDay)
            isMarried = False
        if(element.get_tag()=="DIV" and element.get_level()==1):
            isDivorced = True
        if(isDivorced and element.get_tag()=="DATE" and element.get_level()==2):
            divorcedDay = element.get_value()
            divorcedDay = divorcedDay.split(" ")
            divorcedDay = datetime.date(int(divorcedDay[2]),int(months[divorcedDay[1]]), int(divorcedDay[0]))
            famDict[famTag].Set_divorced(divorcedDay)
            isDivorced = False
        if(element.get_level()==1 and element.get_tag()=="HUSB"):
            husbStr = element.to_gedcom_string()
            husbStr = husbStr.replace('@','').strip().split(" ")[2]
            famDict[famTag].Set_husbandID(husbStr)
            famDict[famTag].Set_husbandName(indiDict[husbStr].Get_name())
        if(element.get_level()==1 and element.get_tag()=="WIFE"):
            wifeStr = element.to_gedcom_string()
            wifeStr = wifeStr.replace('@','').strip().split(" ")[2]
            famDict[famTag].Set_wifeID(wifeStr)
            famDict[famTag].Set_wifeName(indiDict[wifeStr].Get_name())
        if(element.get_level()==1 and element.get_tag()=="CHIL"):
            child = element.to_gedcom_string()
            child = child.replace('@','').strip().split(" ")[2]
            children.add(child)
            famDict[famTag].Set_children(set(children))

    return indiDict, famDict

# main
if __name__ == "__main__":
    # Process ged file
    indiDetails, familyDetails = processGedFile("FamilyTree.ged")
    # Output the results
    sys.stdout = open("Output_FamilyTree.txt", "w")
    # Print indiDetails and Family details from processed ged file
    printTablesData(indiDetails, familyDetails)
    sys.stdout.close()

