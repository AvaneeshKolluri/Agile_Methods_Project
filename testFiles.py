import unittest
from individualClass import individualClass as indiClass
from collections import OrderedDict
from userStory01 import story1
import warnings
import HtmlTestRunner

class test1(unittest.TestCase):
    
    def test_UserStory01(self):
        resultsList = story1("FamilyTree.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])
        
    def test_UserStory02(self):
        resultsList = story1("FalseMarriage.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: I1: Marriage 3000-05-24 occurs in the future',
                                       'ERROR: INDIVIDUAL: US01: I2: Marriage 3000-05-24 occurs in the future'])
        
    def test_UserStory03(self):
        resultsList = story1("FalseDivorce.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: I3: Divorce 2050-02-04 occurs in the future',
                                       'ERROR: INDIVIDUAL: US01: I4: Divorce 2050-02-04 occurs in the future'])
        
    def test_UserStory04(self):
        resultsList = story1("FalseBday.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: I1: Birthday 2050-10-13 occurs in the future'])
        
    def test_UserStory05(self):
        resultsList = story1("FalseDeath.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: I2: Death 2022-02-09 occurs in the future'])
        
if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
