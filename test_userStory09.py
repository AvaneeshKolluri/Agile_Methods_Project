import unittest
from userStories import userStory09
import HtmlTestRunner


class TestUserStory09Class(unittest.TestCase):


    """ Test the US09 function """

    def test_userStory09_1(self):
        resultsList = userStory09('InputGedFiles/UserStory09_GED/FamilyTree.ged')
        self.assertEqual(resultsList, [])

    def test_userStory09_2(self):
        resultsList = userStory09('InputGedFiles/UserStory09_GED/FamilyTree_Test_BirthDateisDeathDate.ged')
        self.assertEqual(resultsList, [])

    def test_userStory09_3(self):
        resultsList = userStory09('InputGedFiles/UserStory09_GED/FamilyTree_Test_I9BirthDateChange.ged')
        self.assertEqual(resultsList, [])

    def test_userStory09_4(self):
        resultsList = userStory09('InputGedFiles/UserStory09_GED/FamilyTree_Test_I3BirthDateChange.ged')
        self.assertEqual(resultsList, ["ERROR: FAMILY: US09: 25: F1: Husband (I1) died 1984-01-09 before child's (I3) birth 2062-07-03",
                                        "ERROR: FAMILY: US09: 39: F1: Wife (I2) died 2017-02-09 before child's (I3) birth 2062-07-03"])

    def test_userStory09_5(self):
        resultsList = userStory09('InputGedFiles/UserStory09_GED/FamilyTree_Test_I2DeathDateChange.ged')
        self.assertEqual(resultsList, ["ERROR: FAMILY: US09: 39: F1: Wife (I2) died 1962-07-02 before child's (I3) birth 1962-07-03"])

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
