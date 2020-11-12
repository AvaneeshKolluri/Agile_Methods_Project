import unittest
import HtmlTestRunner
from userStories import userStory18

'''
User story 18:
Requirement: Siblings should not marry one another
'''
# Test Class for User Story 18
class TestUserStory18Class(unittest.TestCase):

    def test_UserStory18_1(self):
        resultsList = userStory18("InputGedFiles/UserStory18_GED/testUserStory18-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US18 : 78: Sibling Id:I4,name:Julia Anniston and Individual Id:I3,name:Michael Anniston are married"])

    def test_UserStory18_2(self):
        resultsList = userStory18("InputGedFiles/UserStory18_GED/testUserStory18-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US18 : 123: Sibling Id:I4,name:Julia Anniston and Individual Id:I3,name:Michael Anniston are married",
                                       "ERROR: FAMILY: US18 : 131: Sibling Id:I5,name:Rose Anniston and Individual Id:I8,name:Romeo Bell are married",
                                       "ERROR: FAMILY: US18 : 136: Sibling Id:I6,name:Lilly Anniston and Individual Id:I10,name:Robin Bell are married"])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
