import unittest
from userStories import userStory13
import HtmlTestRunner

class TestUserStory13Class(unittest.TestCase):

    def test_UserStory13_1(self):
        resultsList = userStory13("InputGedFiles/UserStory13_GED/testUserStory13-1.ged")
        self.assertEqual(resultsList, [])

    def test_UserStory13_2(self):
        resultsList = userStory13("InputGedFiles/UserStory13_GED/testUserStory13-2.ged")
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US13: Family F1 has two children (I3, I5) with implausible birth dates (1000-01-01, 1000-05-01)',
                                       'ERROR: INDIVIDUAL: US13: Family F1 has two children (I3, I7) with implausible birth dates (1000-01-01, 0999-10-01)',
                                       'ERROR: INDIVIDUAL: US13: Family F1 has two children (I4, I5) with implausible birth dates (1000-01-02, 1000-05-01)',
                                       'ERROR: INDIVIDUAL: US13: Family F1 has two children (I4, I7) with implausible birth dates (1000-01-02, 0999-10-01)',
                                       'ERROR: INDIVIDUAL: US13: Family F1 has two children (I5, I7) with implausible birth dates (1000-05-01, 0999-10-01)',
                                       'ERROR: INDIVIDUAL: US13: Family F2 has two children (I10, I12) with implausible birth dates (1000-01-01, 0999-11-01)',
                                       'ERROR: INDIVIDUAL: US13: Family F2 has two children (I12, I9) with implausible birth dates (0999-11-01, 1000-01-01)'])

if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
