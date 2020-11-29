import unittest
from userStories import userStory36

class TestUserStory36Class(unittest.TestCase):

    def test1_UserStory36(self):
        resultsList = userStory36("InputGedFiles/UserStory36_GED/death.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,['Tommy Johnson'])

    def test2_UserStory36(self):
        resultsList = userStory36("InputGedFiles/UserStory36_GED/death2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,['Tommy Johnson', 'Suzanne Johnson'])

    def test3_UserStory36(self):
        resultsList = userStory36("InputGedFiles/UserStory36_GED/death3.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,['Tommy Johnson', 'Suzanne Johnson', 'Max Johnson'])

    def test4_UserStory36(self):
        resultsList = userStory36("InputGedFiles/UserStory36_GED/death4.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,[])





if __name__ == "__main__":
    unittest.main()
