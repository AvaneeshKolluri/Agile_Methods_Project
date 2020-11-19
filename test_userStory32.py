import unittest
from userStories import userStory32
import HtmlTestRunner

class TestUserStory32Class(unittest.TestCase):

    def test_UserStory32_1(self):
        resultsList = userStory32("InputGedFiles/UserStory32_GED/testUserStory32-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["FAMILY: US32: Individuals with IDs ['I5', 'I6'] are multiple births."])

    def test_UserStory32_2(self):
        resultsList = userStory32("InputGedFiles/UserStory32_GED/testUserStory32-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test_UserStory32_3(self):
        resultsList = userStory32("InputGedFiles/UserStory32_GED/testUserStory32-3.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["FAMILY: US32: Individuals with IDs ['I10', 'I11', 'I12'] are multiple births."])

if __name__ == '__main__':
    #warnings.filterwarnings("ignore")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
