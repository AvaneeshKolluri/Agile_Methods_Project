import unittest
import HtmlTestRunner
from userStories import userStory27

'''
Author: Srikanth Uppada
User story 27:
Requirement: Include person's current age when listing individuals
'''

# Test Class for User Story 27
class TestUserStory27Class(unittest.TestCase):

    def test_UserStory27_1(self):
        resultsList = userStory27("InputGedFiles/UserStory27_GED/testUserStory27-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "LIST: US27 : List of individuals with their name and age are:{'Willard Carroll Smith': 52, 'Jada Koren Pinkett': 49, 'Caroline Bright': 155, 'Willard Sr Smith': 84}"])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
