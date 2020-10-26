import unittest
import HtmlTestRunner
from userStories import userStory17

'''
User story 17:
Requirement: Parents should not marry any of their descendants
'''
# Test Class for User Story 17
class TestUserStory17Class(unittest.TestCase):

    def test_UserStory17_1(self):
        resultsList = userStory17("InputGedFiles/UserStory17_GED/testUserStory17-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US17: F2 Parents should not marry their descendants"])

    def test_UserStory17_2(self):
        resultsList = userStory17("InputGedFiles/UserStory17_GED/testUserStory17-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US17: F1 Parents should not marry their descendants"])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
