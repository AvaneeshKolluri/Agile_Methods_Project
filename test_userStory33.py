import unittest
from userStories import userStory33
import HtmlTestRunner

class TestUserStory33Class(unittest.TestCase):

    def test_UserStory33(self):
        resultsList = userStory33("InputGedFiles/UserStory33_GED/testUserStory33.ged")
        self.assertEqual(resultsList, ['FAMILY: US33: Child [I1] is an orphan in family [F1].',
                                       'FAMILY: US33: Child [I9] is an orphan in family [F1].' ])


if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
