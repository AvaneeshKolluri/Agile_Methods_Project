from userStories import userStory21
import unittest
import HtmlTestRunner


class UserStory21Test(unittest.TestCase):


    """ Test the User Story 21 function """


    def test_userStory21_1(self):

        resultsList = userStory21("InputGedFiles/UserStory21_GED/testUserStory21-1.ged")
        self.assertEqual([], resultsList)

    def test_userStor21_2(self):

        resultsList = userStory21("InputGedFiles/UserStory21_GED/testUserStory21-2.ged")
        self.assertEqual(['ERROR: FAMILY: US21: F2: Husband (I3) is labelled incorrectly as (F).', 'ERROR: FAMILY: US21: F3: Husband (I3) is labelled incorrectly as (F).', 'ERROR: FAMILY: US21: F4: Husband (I3) is labelled incorrectly as (F).', 'ERROR: FAMILY: US21: F5: Husband (I3) is labelled incorrectly as (F).', 'ERROR: FAMILY: US21: F6: Husband (I3) is labelled incorrectly as (F).'], resultsList)

    def test_userStory21_3(self):

        resultsList = userStory21("InputGedFiles/UserStory21_GED/testUserStory21-3.ged")
        self.assertEqual(['ERROR: FAMILY: US21: F3: Wife (I5) is labelled incorrectly as (M).'], resultsList)

    def test_userStory21_4(self):

        resultsList = userStory21("InputGedFiles/UserStory21_GED/testUserStory21-4.ged")
        self.assertEqual(['ERROR: FAMILY: US21: F1: Husband (I1) is labelled incorrectly as (F).'], resultsList)
        
    def test_userStory21_5(self):

        resultsList = userStory21("InputGedFiles/UserStory21_GED/testUserStory21-5.ged")
        self.assertEqual(['ERROR: FAMILY: US21: F1: Wife (I2) is labelled incorrectly as (M).'], resultsList)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
