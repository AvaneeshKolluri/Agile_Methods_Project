import unittest 
from sprint1UserStories import userStory11
import HtmlTestRunner

class TestUserStory11Class(unittest.TestCase):

    
    """ Test the marriage_after_14 function from US10 """


    def test_user_story_11_1(self):

        resultsList = userStory11("InputGedFiles/UserStory11_GED/testUserStory11-1.ged")
        self.assertEqual(resultsList, [])

    def test_user_story_11_2(self):

        resultsList = userStory11("InputGedFiles/UserStory11_GED/testUserStory11-2.ged")
        self.assertEqual(resultsList,['ERROR: FAMILY: US11: F2: Marriage 1993-12-31 should not be happening during another marriage 1992-05-09.'])

    def test_user_story_11_3(self):

        resultsList = userStory11("InputGedFiles/UserStory11_GED/testUserStory11-3.ged")
        self.assertEqual(resultsList, [])

    def test_user_story_11_4(self):

        resultsList = userStory11("InputGedFiles/UserStory11_GED/testUserStory11-4.ged")
        self.assertEqual(resultsList, ["ERROR: FAMILY: US11: F6: Marriage 1990-12-24 should not be happening during another marriage 1987-05-09.",
                                       "ERROR: FAMILY: US11: F6: Marriage 2006-11-18 should not be happening during another marriage 1990-12-24."])

    def test_user_story_11_5(self):

        resultsList = userStory11("InputGedFiles/UserStory11_GED/testUserStory11-5.ged")
        self.assertEqual(resultsList, [])

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
