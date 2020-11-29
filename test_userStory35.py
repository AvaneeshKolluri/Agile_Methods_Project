import unittest
from userStories import userStory35

class TestUserStory35Class(unittest.TestCase):

    def test1_UserStory25(self):
        resultsList = userStory35("InputGedFiles/UserStory35_GED/one.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Tom Johnson'])

    def test2_UserStory35(self):
        resultsList = userStory35("InputGedFiles/UserStory35_GED/two.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Tom Johnson', 'Max Johnson'])
        
    def test3_UserStory35(self):
        resultsList = userStory35("InputGedFiles/UserStory35_GED/three.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Tom Johnson', 'Max Johnson', 'Jennifer Johnson'])

    def test4_UserStory35(self):
        resultsList = userStory35("InputGedFiles/UserStory35_GED/four.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])


if __name__ == "__main__":
    unittest.main()
        
