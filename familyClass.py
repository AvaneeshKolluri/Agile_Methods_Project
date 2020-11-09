
class familyClass(object):
    def __init__(self, ID = 'NA', Married= 'NA', Divorced = 'NA', HusbandID = 'NA', HusbandName = '0', WifeID = 'NA', WifeName = 'NA', Children = [], DupliID_fam = []):
        self.ID =  ID
        self.Married = Married
        self.Divorced = Divorced
        self.HusbandID = HusbandID
        self.HusbandName = HusbandName
        self.WifeID = WifeID
        self.WifeName = WifeName
        self.Children = []
        self.DupliID_fam = []

    def Set_ID(self, ID):
        self.ID = ID

    def Set_married(self, Married):
        self.Married = Married 

    def Set_divorced(self, Divorced):
        self.Divorced = Divorced

    def Set_husbandID(self, HusbandID):
        self.HusbandID = HusbandID

    def Set_husbandName(self, HusbandName): 
        self.HusbandName = HusbandName

    def Set_wifeID(self, WifeID):
        self.WifeID = WifeID

    def Set_wifeName(self, WifeName):
        self.WifeName = WifeName

    def Set_children(self, Children):
        self.Children.append(Children)
        
    def Set_DupliID_fam(self, dupli_arg):
        self.DupliID_fam.append(dupli_arg)
        
    def Get_ID(self):
        return self.ID

    def Get_married(self):
        return self.Married

    def Get_divorced(self):
        return self.Divorced

    def Get_husbandID(self):
        return self.HusbandID

    def Get_husbandName(self):
        return self.HusbandName

    def Get_wifeID(self):
        return self.WifeID

    def Get_wifeName(self):
        return self.WifeName

    def Get_children(self):
        if(self.Children == []):
            return 'NA'
        return self.Children
        
    def Get_DupliID_fam(self):
        if(self.DupliID_fam == []):
            return 'NA'
        return self.DupliID_fam

    def Get_details(self):
        return [self.ID, self.Married, self.Divorced, self.HusbandID, self.HusbandName, self.WifeID, self.WifeName, self.Children]

