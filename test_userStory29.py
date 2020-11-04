from userStories import userStory29
import unittest
import HtmlTestRunner


class UserStory29Test(unittest.TestCase):


    """ Test the User Story 29 function """


    def test_userStory29_1(self):

        resultsList = userStory29('InputGedFiles/UserStory29_GED/FamilyTree_Normal.ged')
        self.assertEqual([], resultsList)

    def test_userStor29_2(self):

        resultsList = userStory29('InputGedFiles/UserStory29_GED/FamilyTree_SomeDeaths.ged')
        self.assertEqual(["INDIVIDUAL: US29: John Doe with id I1 is deceased.", 
                        "INDIVIDUAL: US29: Joan Deer with id I2 is deceased.",
                        "INDIVIDUAL: US29: June Doe with id I3 is deceased.",
                        "INDIVIDUAL: US29: Judy Bear with id I5 is deceased."], resultsList)

    def test_userStor29_3(self):

        resultsList = userStory29('InputGedFiles/UserStory29_GED/FamilyTree_AllDeaths.ged')
        self.assertEqual(["INDIVIDUAL: US29: John Doe with id I1 is deceased.", 
                        "INDIVIDUAL: US29: Joan Deer with id I2 is deceased.",
                        "INDIVIDUAL: US29: June Doe with id I3 is deceased.",
                        "INDIVIDUAL: US29: Jason Doe with id I4 is deceased.",
                        "INDIVIDUAL: US29: Judy Bear with id I5 is deceased.",
                        "INDIVIDUAL: US29: Jasper Doe with id I6 is deceased.",
                        "INDIVIDUAL: US29: Jessica Doe with id I7 is deceased.",
                        "INDIVIDUAL: US29: Justin Elk with id I8 is deceased.",
                        "INDIVIDUAL: US29: Julia Elk with id I9 is deceased.",
                        "INDIVIDUAL: US29: Jules Doe with id I10 is deceased.",
                        "INDIVIDUAL: US29: Jared Squirrel with id I11 is deceased.",
                        "INDIVIDUAL: US29: Judith Doe with id I12 is deceased.",
                        "INDIVIDUAL: US29: Janet Doe with id I13 is deceased.",
                        "INDIVIDUAL: US29: Jud Squirrel with id I14 is deceased."], resultsList)
                        

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))