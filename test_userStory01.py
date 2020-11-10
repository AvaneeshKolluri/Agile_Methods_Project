import unittest
from userStories import userStory01
import HtmlTestRunner

class TestUserStory01Class(unittest.TestCase):

    def test_UserStory01_1(self):
        resultsList = userStory01("InputGedFiles/UserStory01_GED/testUserStory01-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test_UserStory01_2(self):
        resultsList = userStory01("InputGedFiles/UserStory01_GED/testUserStory01-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: 142: I1: Marriage 3000-05-24 occurs in the future',
                                       'ERROR: INDIVIDUAL: US01: 142: I2: Marriage 3000-05-24 occurs in the future'])

    def test_UserStory01_3(self):
        resultsList = userStory01("InputGedFiles/UserStory01_GED/testUserStory01-3.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: 152: I3: Divorce 2050-02-04 occurs in the future',
                                       'ERROR: INDIVIDUAL: US01: 152: I4: Divorce 2050-02-04 occurs in the future'])

    def test_UserStory01_4(self):
        resultsList = userStory01("InputGedFiles/UserStory01_GED/testUserStory01-4.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: 22: I1: Birthday 2050-10-13 occurs in the future'])

    def test_UserStory01_5(self):
        resultsList = userStory01("InputGedFiles/UserStory01_GED/testUserStory01-5.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US01: 39: I2: Death 2022-02-09 occurs in the future'])

if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
