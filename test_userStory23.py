import unittest
from userStories import userStory23
import HtmlTestRunner

class TestUserStory23Class(unittest.TestCase):

    def test_UserStory23(self):
        resultsList = userStory23("InputGedFiles/UserStory23_GED/testUserStory23.ged")
        self.assertEqual(resultsList, ["ERROR: INDIVIDUAL: US23: Two individuals [I1, I5] have duplicate names and birthdays [Geeorge Boots, 1000-01-01]."])


if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
