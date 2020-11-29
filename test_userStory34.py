import unittest
from userStories import userStory34
import HtmlTestRunner

class TestUserStory34Class(unittest.TestCase):

    def test_UserStory33(self):
        resultsList = userStory34("InputGedFiles/UserStory34_GED/testUserStory34.ged")
        self.assertEqual(resultsList, ['FAMILY: US34: Spouses in family [F1] have large age gap at marriage [I1, 100], [I3, 200].' ,
                                       'FAMILY: US34: Spouses in family [F2] have large age gap at marriage [I1, 100], [I2, 50].' ])


if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
