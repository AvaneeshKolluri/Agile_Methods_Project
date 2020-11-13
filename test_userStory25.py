import unittest
from userStories import userStory25

class TestUserStory25Class(unittest.TestCase):

    def test1_UserStory25(self):
        resultsList = userStory25("InputGedFiles/UserStory25_GED/smalltest.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,['ERROR: INDIVIDUAL: US25: (42, 48): Individual  Tom Johnson is a duplicate name with duplicate Birthday 1999-04-03.'])


    def test2_UserStory25(self):
        resultsList = userStory25("InputGedFiles/UserStory25_GED/smalltest2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,[])
    def test3_UserStory25(self):
        resultsList = userStory25("InputGedFiles/UserStory25_GED/test.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,[])





if __name__ == "__main__":
    unittest.main()

