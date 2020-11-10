import unittest
import HtmlTestRunner
from userStories import userStory02

'''
User story 02:
Requirement: Birth should occur before marriage of an individual
'''
# Test Class for User Story 02
class TestUserStory02Class(unittest.TestCase):

    def test_UserStory02_1(self):
        resultsList = userStory02("InputGedFiles/UserStory02_GED/testUserStory02-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test_UserStory02_2(self):
        resultsList = userStory02("InputGedFiles/UserStory02_GED/testUserStory02-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: FAMILY: US02: 117: I1: Husband's birth date 1968-09-25 is after marriage date 1967-12-31",
                                        "ERROR: FAMILY: US02: 117: I4: Wife's birth date 1971-09-18 is after marriage date 1967-12-31"])
    def test_UserStory02_3(self):
        resultsList = userStory02("InputGedFiles/UserStory02_GED/testUserStory02-3.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: FAMILY: US02: 117: I4: Wife's birth date 1971-09-18 is after marriage date 1970-12-31"])

    def test_UserStory02_4(self):
        resultsList = userStory02("InputGedFiles/UserStory02_GED/testUserStory02-4.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: FAMILY: US02: 125: I2: Wife's birth date 1967-11-16 is after marriage date 1967-05-09"])

    def test_UserStory02_5(self):
        resultsList = userStory02("InputGedFiles/UserStory02_GED/testUserStory02-5.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: FAMILY: US02: 135: I7: Wife's birth date 1867-07-13 is after marriage date 1862-08-24"])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
