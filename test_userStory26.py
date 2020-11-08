import unittest
from userStories import userStory26

class TestUserStory26Class(unittest.TestCase):

    def test1_UserStory26(self):
        resultsList = userStory26("InputGedFiles/UserStory26_GED/smalltest.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,['ERROR: INDIVIDUAL: US26: Individual  I7 does not correspond to any individual in a family'])


    def test2_UserStory26(self):
        resultsList = userStory26("InputGedFiles/UserStory25_GED/smalltest2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,[])
    def test3_UserStory26(self):
        resultsList = userStory26("InputGedFiles/UserStory26_GED/test.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,[])





if __name__ == "__main__":
    unittest.main()
