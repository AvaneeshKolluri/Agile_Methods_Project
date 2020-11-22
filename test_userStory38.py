import unittest
import HtmlTestRunner
from userStories import userStory38

'''
Author: Srikanth Uppada
User story 38:
Requirement: List all living people in a GEDCOM file whose birthdays occur in the next 30 days
'''

# Test Class for User Story 38
class TestUserStory38Class(unittest.TestCase):

    def test_UserStory38_1(self):
        resultsList = userStory38("InputGedFiles/UserStory38_GED/testUserStory38-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "LIST: US38: No individual's birthday occur in the next 30 days"])

    def test_UserStory38_2(self):
        resultsList = userStory38("InputGedFiles/UserStory38_GED/testUserStory38-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "LIST: US38: Individuals whose birthdays occur in the next 30 days: ['Willow Camille Reign Smith']"])
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
