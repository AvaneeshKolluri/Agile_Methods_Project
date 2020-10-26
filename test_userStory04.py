import unittest
from userStories import userStory04
import HtmlTestRunner

class TestUserStory04Class(unittest.TestCase):

    def test_UserStory04_1(self):
        resultsList = userStory04("InputGedFiles/UserStory04_GED/testUserStory04-1.ged")
        self.assertEqual(resultsList, [])

    def test_UserStory04_2(self):
        resultsList = userStory04("InputGedFiles/UserStory04_GED/testUserStory04-2.ged")
        self.assertEqual(resultsList, ['ERROR: FAMILY: US04: F1 Divorce date occurs before marriage date - Marriage 1000-01-03: Divorce 1000-01-01'])

    def test_UserStory04_3(self):
        resultsList = userStory04("InputGedFiles/UserStory04_GED/testUserStory04-3.ged")
        self.assertEqual(resultsList, ['ERROR: FAMILY: US04: F1 Divorce date occurs before marriage date - Marriage 1000-02-01: Divorce 1000-01-01',
                                       'ERROR: FAMILY: US04: F2 Divorce date occurs before marriage date - Marriage 1100-01-01: Divorce 1000-01-01'])

if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
