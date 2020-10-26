import unittest
from userStories import userStory14
import HtmlTestRunner

class TestUserStory14Class(unittest.TestCase):

    def test_UserStory14_1(self):
        resultsList = userStory14("InputGedFiles/UserStory14_GED/testUserStory14-1.ged")
        self.assertEqual(resultsList, [])

    def test_UserStory14_2(self):
        resultsList = userStory14("InputGedFiles/UserStory14_GED/testUserStory14-2.ged")
        self.assertEqual(resultsList, [ "ERROR: FAMILY: US14: Family F1 has 6 children ['I14', 'I15', 'I4', 'I5', 'I6', 'I7'] born at the same time with age 1020.",
                                        "ERROR: FAMILY: US14: Family F2 has 5 children ['I10', 'I11', 'I12', 'I13', 'I9'] born at the same time with age 1020."])

if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
