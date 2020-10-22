from sprint1UserStories import userStory19
import unittest
import HtmlTestRunner

class UserStory19Test(unittest.TestCase):


    """ Test the User Story 19 function """


    def test_userStory19_1(self):

        resultsList = userStory19('InputGedFiles/UserStory19_GED/FamilyTree.ged')
        self.assertEqual([], resultsList)

    def test_userStory19_2(self):

        resultsList = userStory19('InputGedFiles/UserStory19_GED/FamilyTree_Normal.ged')
        self.assertEqual([], resultsList)

    def test_userStory19_3(self):

        resultsList = userStory19('InputGedFiles/UserStory19_GED/FamilyTree_OneFirstCousinMarriage_1.ged')
        self.assertEqual(['ERROR: FAMILY: US19: F4: First cousins I9 and I8 married. Children of siblings I7 and I6.'], resultsList)

    def test_userStory19_4(self):

        resultsList = userStory19('InputGedFiles/UserStory19_GED/FamilyTree_TwoFirstCousinMarriage.ged')
        self.assertEqual(['ERROR: FAMILY: US19: F5: First cousins I9 and I8 married. Children of siblings I7 and I6.', 
                            'ERROR: FAMILY: US19: F8: First cousins I17 and I14 married. Children of siblings I12 and I11.'], resultsList)

    def test_userStory19_5(self):

        resultsList = userStory19('InputGedFiles/UserStory19_GED/FamilyTree_OneFirstCousinMarriage_2.ged')
        self.assertEqual(['ERROR: FAMILY: US19: F7: First cousins I16 and I13 married. Children of siblings I11 and I10.'], resultsList)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
