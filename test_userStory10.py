import unittest 
from project2 import marriage_after_14, main
import datetime

class MarriageAfter14Test(unittest.TestCase):

    
    """ Test the marriage_after_14 function from US10 """


    def test_marriage_after_14_errors(self):

        """ Test the error catching of marriage_after_14 """

        #create gedcom files where there are marriages before 14
        individuals_1, families_1 = main('FamilyTree_Test_Under14.ged')
        individuals_2, families_2 = main('FamilyTree_Test_JustUnder14.ged')

        with self.assertRaises(ValueError):
            marriage_after_14(individuals_1, families_1) 
        with self.assertRaises(ValueError):
            marriage_after_14(individuals_2, families_2)
    
    def test_marriage_after_14_no_errors(self):

        """ Test the functionality of marriage_after_14 """

        #create gedcom files where marriages are on or after 14 
        individuals_3, families_3 = main('FamilyTree.ged')
        individuals_4, families_4 = main('FamilyTree_Test_Equals14.ged')
        individuals_5, families_5 = main('FamilyTree_Test_JustOver14.ged')

        self.assertTrue(marriage_after_14(individuals_3, families_3))
        self.assertTrue(marriage_after_14(individuals_4, families_4))
        self.assertTrue(marriage_after_14(individuals_5, families_5))
            
if __name__ == "__main__":
    unittest.main()