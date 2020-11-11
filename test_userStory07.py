import unittest
import HtmlTestRunner
from userStories import userStory07

'''
Author: Srikanth Uppada
User story 07:
Requirement: Death should be less than 150 years after birth for dead people,
             and current date should be less than 150 years after birth for all living people
'''

# Test Class for User Story 07
class TestUserStory07Class(unittest.TestCase):

    def test_UserStory07_1(self):
        resultsList = userStory07("InputGedFiles/UserStory07_GED/testUserStory07-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: INDIVIDUAL: US07: 96: I7 More than 150 years old - Birth date 1865-07-13"])

    def test_UserStory07_2(self):
        resultsList = userStory07("InputGedFiles/UserStory07_GED/testUserStory07-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: INDIVIDUAL: US07: 104: I8 More than 150 years old at death - Birth 1865-04-06: Death 2016-11-07"])

    def test_UserStory07_3(self):
        resultsList = userStory07("InputGedFiles/UserStory07_GED/testUserStory07-3.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: INDIVIDUAL: US07: 25: I1 More than 150 years old - Birth date 1869-09-25"])

    def test_UserStory07_4(self):
        resultsList = userStory07("InputGedFiles/UserStory07_GED/testUserStory07-4.ged")
        resultsList.sort()
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: INDIVIDUAL: US07: 25: I1 More than 150 years old - Birth date 1868-09-25",
                                        "ERROR: INDIVIDUAL: US07: 52: I3 More than 150 years old - Birth date 1866-11-11",
                                        "ERROR: INDIVIDUAL: US07: 63: I4 More than 150 years old - Birth date 1843-09-18",
                                        "ERROR: INDIVIDUAL: US07: 74: I5 More than 150 years old - Birth date 1853-07-08",
                                        "ERROR: INDIVIDUAL: US07: 85: I6 More than 150 years old - Birth date 1870-10-31"])

    def test_UserStory07_5(self):
        resultsList = userStory07("InputGedFiles/UserStory07_GED/testUserStory07-5.ged")
        resultsList.sort()
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ERROR: INDIVIDUAL: US07: 104: I8 More than 150 years old at death - Birth 1859-04-06: Death 2016-11-07",
                                        "ERROR: INDIVIDUAL: US07: 25: I1 More than 150 years old - Birth date 1868-09-25",
                                        "ERROR: INDIVIDUAL: US07: 35: I2 More than 150 years old at death - Birth 1867-11-16: Death 2020-03-17",
                                        "ERROR: INDIVIDUAL: US07: 52: I3 More than 150 years old - Birth date 1866-11-11",
                                        "ERROR: INDIVIDUAL: US07: 63: I4 More than 150 years old - Birth date 1843-09-18",
                                        "ERROR: INDIVIDUAL: US07: 74: I5 More than 150 years old - Birth date 1853-07-08",
                                        "ERROR: INDIVIDUAL: US07: 85: I6 More than 150 years old - Birth date 1869-10-31",
                                        "ERROR: INDIVIDUAL: US07: 96: I7 More than 150 years old - Birth date 1867-07-13"])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
