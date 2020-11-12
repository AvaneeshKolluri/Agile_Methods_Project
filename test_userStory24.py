import unittest
from userStories import userStory24
import HtmlTestRunner

class TestUserStory24Class(unittest.TestCase):

    def test_UserStory24(self):
        resultsList = userStory24("InputGedFiles/UserStory24_GED/testUserStory24.ged")
        self.assertEqual(resultsList, ["ERROR: FAMILY: US24: (99, 100) and (110, 111): Two families [F1, F2] have duplicate spouses [Geeorge Boots, Dara Boots]."])


if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
