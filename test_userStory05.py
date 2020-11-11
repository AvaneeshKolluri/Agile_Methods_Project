import unittest
from userStories import userStory05

class TestUserStory05Class(unittest.TestCase):

    def test1_UserStory05(self):
        resultsList = userStory05("InputGedFiles/UserStory05_GED/deathWifeafter.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US05: 38: wedding occurs after wife death. Wedding Date: 2080-02-02 Wife Death: 2040-02-01'])

    def test2_UserStory05(self):
        resultsList = userStory05("InputGedFiles/UserStory05_GED/deathHusbandafter.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US05: 38: wedding occurs after husband death. Wedding Date: 2080-02-02 Husband Death: 2050-01-05'])

    def test3_UserStory05(self):
        resultsList = userStory05("InputGedFiles/UserStory05_GED/normaltree.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test4_UserStory05(self):
        resultsList = userStory05("InputGedFiles/UserStory05_GED/normal.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test5_UserStory05(self):
        resultsList = userStory05("InputGedFiles/UserStory05_GED/test5.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['ERROR: FAMILY: US05: 38: wedding occurs after husband death. Wedding Date: 2090-02-02 Husband Death: 2050-01-05'])


if __name__ == "__main__":
    unittest.main()
