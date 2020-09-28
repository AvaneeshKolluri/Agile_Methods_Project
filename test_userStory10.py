import unittest 
from project2 import processGedFile
from userStory10 import userStory10_marriage_after_14
import datetime

class MarriageAfter14Test(unittest.TestCase):

    
    """ Test the marriage_after_14 function from US10 """


    def test_user_story_10_1(self):

        resultsList = userStory10_marriage_after_14("InputGedFiles/UserStory10_GED/FamilyTree.ged")
        self.assertEqual(resultsList, [])

    def test_user_story_10_2(self):

        resultsList = userStory10_marriage_after_14("InputGedFiles/UserStory10_GED/FamilyTree_Test_Equals14.ged")
        self.assertEqual(resultsList, [])

    def test_user_story_10_3(self):

        resultsList = userStory10_marriage_after_14("InputGedFiles/UserStory10_GED/FamilyTree_Test_JustOver14.ged")
        self.assertEqual(resultsList, [])

    def test_user_story_10_4(self):

        resultsList = userStory10_marriage_after_14("InputGedFiles/UserStory10_GED/FamilyTree_Test_Under14.ged")
        self.assertEqual(resultsList, ["ERROR: Wife's birth date 1946-09-22 not at least 14 years prior to marriage date 1958-04-12"])

    def test_user_story_10_5(self):

        resultsList = userStory10_marriage_after_14("InputGedFiles/UserStory10_GED/FamilyTree_Test_ThreeUnder14.ged")
        self.assertEqual(resultsList, ["ERROR: Wife's birth date 1946-09-22 not at least 14 years prior to marriage date 1958-04-12",
                                        "ERROR: Wife's birth date 1977-05-09 not at least 14 years prior to marriage date 1987-05-09",
                                        "ERROR: Wife's birth date 1976-12-26 not at least 14 years prior to marriage date 1990-12-24"])


if __name__ == "__main__":
    unittest.main()