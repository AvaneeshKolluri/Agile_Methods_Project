import unittest
from userStories import userStory31
import HtmlTestRunner

class TestUserStory31Class(unittest.TestCase):

    def test_UserStory31_1(self):
        resultsList = userStory31("InputGedFiles/UserStory31_GED/testUserStory31-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['INDIVIDUAL: US31: Jaden Christopher Syre Smith with id I5 is living, over 30, and never has been married.'])

    def test_UserStory31_2(self):
        resultsList = userStory31("InputGedFiles/UserStory31_GED/testUserStory31-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['INDIVIDUAL: US31: Jaden Christopher Syre Smith with id I5 is living, over 30, and never has been married.'])

    def test_UserStory31_3(self):
        resultsList = userStory31("InputGedFiles/UserStory31_GED/testUserStory31-3.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['INDIVIDUAL: US31: June Doe with id I3 is living, over 30, and never has been married.'])

    def test_UserStory31_4(self):
        resultsList = userStory31("InputGedFiles/UserStory31_GED/testUserStory31-4.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test_UserStory31_5(self):
        resultsList = userStory31("InputGedFiles/UserStory31_GED/testUserStory31-5.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
