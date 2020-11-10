import unittest
import HtmlTestRunner
from userStories import userStory39


class UserStory39Test(unittest.TestCase):


    """ Test the userStory 39 function """

    def test_userStory39_1(self):

        resultsList = userStory39("InputGedFiles/UserStory39_GED/FamilyTree_None.ged")
        self.assertEqual([], resultsList)
    
    def test_userStory39_2(self):

        resultsList = userStory39("InputGedFiles/UserStory39_GED/FamilyTree_Some.ged")
        self.assertEqual(["FAMILY: US39: F1 has an upcoming anniversary on 11-23.", 
                        "FAMILY: US39: F2 has an upcoming anniversary on 11-23."], resultsList)

    def test_userStory39_3(self):

        resultsList = userStory39("InputGedFiles/UserStory39_GED/FamilyTree_All.ged")
        self.assertEqual(["FAMILY: US39: F1 has an upcoming anniversary on 11-23.", 
                        "FAMILY: US39: F2 has an upcoming anniversary on 11-23.",
                        "FAMILY: US39: F3 has an upcoming anniversary on 11-23.",
                        "FAMILY: US39: F4 has an upcoming anniversary on 11-23."], resultsList)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))