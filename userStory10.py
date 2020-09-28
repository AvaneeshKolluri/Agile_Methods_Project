#check for age after 14 for a marriage
def marriage_after_14(individuals, families):
    for family in families.keys():
        if families[family].Get_married() != "NA":
            husband = families[family].Get_husbandID()
            husband_birth_date = individuals[husband].Get_birthday()
            wife = families[family].Get_wifeID()
            wife_birth_date = individuals[wife].Get_birthday()
            family_marriage_date = families[family].Get_married()
            if float(relativedelta(family_marriage_date, husband_birth_date).years) < float(14):
                raise ValueError(f"{family_marriage_date} is not at least 14 years after {husband_birth_date}")
            elif float(relativedelta(family_marriage_date, wife_birth_date).years) < float(14):
                raise ValueError(f"{family_marriage_date} is not at least 14 years after {wife_birth_date}") 
        else:
            return True