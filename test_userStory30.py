from userStories import userStory30
import unittest
import HtmlTestRunner


class UserStory30Test(unittest.TestCase):


    """ Test the User Story 30 function """


    def test_userStory30_1(self):

        resultsList = userStory30('InputGedFiles/UserStory30_GED/FamilyTree_NoneAliveAndMarried.ged')
        self.assertEqual([], resultsList)


    def test_userStor30_2(self):

        resultsList = userStory30('InputGedFiles/UserStory30_GED/FamilyTree_SomeAliveAndMarried.ged')
        self.assertEqual(["INDIVIDUAL: US30: Justin Elk, with id I8, and Jessica Doe, with id I7, are married and both alive.",
                        "INDIVIDUAL: US30: Jared Squirrel, with id I11, and Jules Doe, with id I10, are married and both alive."], resultsList)

    def test_userStor30_3(self):

        resultsList = userStory30('InputGedFiles/UserStory30_GED/FamilyTree_MostAliveAndMarried.ged')
        self.assertEqual(["INDIVIDUAL: US30: John Doe, with id I1, and Joan Deer, with id I2, are married and both alive.",
                        "INDIVIDUAL: US30: Jason Doe, with id I4, and Judy Bear, with id I5, are married and both alive.",
                        "INDIVIDUAL: US30: Justin Elk, with id I8, and Jessica Doe, with id I7, are married and both alive.",
                        "INDIVIDUAL: US30: Jared Squirrel, with id I13, and Jules Doe, with id I10, are married and both alive."], resultsList)

                        

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))