import unittest
import HtmlTestRunner
from userStories import userStory37

'''
Author: Srikanth Uppada
User story 37:
Requirement: List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days
'''

# Test Class for User Story 37
class TestUserStory37Class(unittest.TestCase):

    def test_UserStory37_1(self):
        resultsList = userStory37("InputGedFiles/UserStory37_GED/testUserStory37-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "LIST: US37: Survivors of Individual ID:I2 in the last 30 days, Spouse ID:I1, and Children ['I5', 'I6']",
                                        "LIST: US37: Survivors of Individual ID:I3 in the last 30 days, Spouse ID:I1, and Children ['I4']"])

    def test_UserStory37_2(self):
        resultsList = userStory37("InputGedFiles/UserStory37_GED/testUserStory37-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "LIST: US37: Survivors of Individual ID:I1 in the last 30 days, Spouse ID:I2, and Children ['I3', 'I4']",
                                        "LIST: US37: Survivors of Individual ID:I7 in the last 30 days, Spouse ID:I8 with no children"])
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
