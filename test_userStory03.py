import unittest
from userStories import userStory03
import HtmlTestRunner

class TestUserStory03Class(unittest.TestCase):

    def test_UserStory03_1(self):
        resultsList = userStory03("InputGedFiles/UserStory03_GED/testUserStory03-1.ged")
        self.assertEqual(resultsList, [])

    def test_UserStory03_2(self):
        resultsList = userStory03("InputGedFiles/UserStory03_GED/testUserStory03-2.ged")
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US03: 23: I1 Death date occurs before birth date - Birth 2000-04-03: Death 2000-04-01'])

    def test_UserStory03_3(self):
        resultsList = userStory03("InputGedFiles/UserStory03_GED/testUserStory03-3.ged")
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US03: 23: I1 Death date occurs before birth date - Birth 2000-04-01: Death 1900-04-01',
                                       'ERROR: INDIVIDUAL: US03: 34: I2 Death date occurs before birth date - Birth 1200-06-05: Death 1200-01-01'])

    def test_UserStory03_4(self):
        resultsList = userStory03("InputGedFiles/UserStory03_GED/testUserStory03-4.ged")
        self.assertEqual(resultsList, [])

    def test_UserStory03_5(self):
        resultsList = userStory03("InputGedFiles/UserStory03_GED/testUserStory03-5.ged")
        self.assertEqual(resultsList, [])

if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
