import unittest 
from sprint1UserStories import userStory09
import HtmlTestRunner


class BirthBeforeDeathTest(unittest.TestCase):


    """ Test the US09 function """

    def test_userStory09_1(self):
        resultsList = userStory09('InputGedFiles/UserStory09_GED/FamilyTree.ged')
        self.assertEqual(resultsList, [])
    
    def test_userStory09_2(self):
        resultsList = userStory09('InputGedFiles/UserStory09_GED/FamilyTree_Test_BirthDateisDeathDate.ged')
        self.assertEqual(resultsList, [])
"""
    def test_userStory09_3(self):
    
    def test_userStory09_4(self):
"""

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))