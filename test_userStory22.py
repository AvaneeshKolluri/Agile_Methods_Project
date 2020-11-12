from userStories import userStory22
import unittest
import HtmlTestRunner


class UserStory22Test(unittest.TestCase):


    """ Test the User Story 22 function """


    def test_userStory22_1(self):
        resultsList = userStory22("InputGedFiles/UserStory22_GED/testUserStory22-1.ged")
        self.assertEqual([], resultsList)
    
    def test_userStor22_2(self):
    
        resultsList = userStory22("InputGedFiles/UserStory22_GED/testUserStory22-2.ged")
        self.assertEqual([], resultsList)
    
    def test_userStory22_3(self):
    
        resultsList = userStory22("InputGedFiles/UserStory22_GED/testUserStory22-3.ged")
        self.assertEqual([], resultsList)
        
    def test_userStory22_4(self):
    
        resultsList = userStory22("InputGedFiles/UserStory22_GED/testUserStory22-4.ged")
        self.maxDiff = None
        self.assertEqual(["ERROR: INDIVIDUAL: US22: [211, 211]: The following are duplicate individual ID's ['I1', 'I1'].",
                        "ERROR: FAMILY: US22: [454, 543]: The following are duplicate individual ID's ['F3', 'F12']."], resultsList)



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
