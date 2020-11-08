import unittest
import HtmlTestRunner
from userStories import userStory28

'''
Author: Srikanth Uppada
User story 28:
Requirement: List siblings in families by decreasing age, i.e. oldest siblings first
'''
# Test Class for User Story 28
class TestUserStory28Class(unittest.TestCase):

    def test_UserStory28_1(self):
        resultsList = userStory28("InputGedFiles/UserStory28_GED/testUserStory28-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["LIST: US28: Family ID: F1 Siblings list in descending order of their age ['I5', 'I6']",
                                       "LIST: US28: Family ID: F2 Siblings list in descending order of their age ['I4']",
                                       "LIST: US28: Family ID: F3 Siblings list in descending order of their age ['I1']"])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
