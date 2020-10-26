from userStories import userStory20 
import unittest
import HtmlTestRunner


class UserStory20Test(unittest.TestCase):


    """ Test the User Story 20 function """


    def test_userStory20_1(self):

        resultsList = userStory20('InputGedFiles/UserStory20_GED/FamilyTree.ged')
        self.assertEqual([], resultsList)

    def test_userStor20_2(self):

        resultsList = userStory20('InputGedFiles/UserStory20_GED/FamilyTree_MarriedNephew.ged')
        self.assertEqual(['ERROR: FAMILY: US20: F2: Wife (I3) married nephew (I6)'], resultsList)

    def test_userStory20_3(self):

        resultsList = userStory20('InputGedFiles/UserStory20_GED/FamilyTree_MarriedNiece.ged')
        self.assertEqual(['ERROR: FAMILY: US20: F3: Husband (I6) married niece (I9)'], resultsList)

    def test_userStory20_4(self):

        resultsList = userStory20('InputGedFiles/UserStory20_GED/FamilyTree_MultipleNephewAndNieceMarriages.ged')
        self.assertEqual(['ERROR: FAMILY: US20: F3: Husband (I6) married niece (I9)', 'ERROR: FAMILY: US20: F6: Wife (I12) married nephew (I14)'], resultsList)

    def test_userStory20_5(self):

        resultsList = userStory20('InputGedFiles/UserStory20_GED/FamilyTree_Normal.ged')
        self.assertEqual([], resultsList)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
