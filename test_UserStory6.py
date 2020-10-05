import unittest
from userStory6 import Story6

class TestUserStory06Class(unittest.TestCase):

    def test1_UserStory6(self):
        resultsList = Story6("InputGedFiles/UserStory06_GED/death_divorcebefore.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test2_UserStory6(self):
        resultsList = Story6("InputGedFiles/UserStory06_GED/deathbeforeDIV.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Error: divorce occurs after husband death. Divorce Date: 2030-02-02 Husband Death: 2020-01-01'])

    def test3_UserStory6(self):
        resultsList = Story6("InputGedFiles/UserStory06_GED/deathbeforeDIV_wife.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Error: divorce occurs after wife death. Divorce Date: 2010-02-02 Wife Death: 2009-01-01'])
        
    def test4_UserStory6(self):
        resultsList = Story6("InputGedFiles/UserStory06_GED/normal.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])

    def test5_UserStory6(self):
        resultsList = Story6("InputGedFiles/UserStory06_GED/husband.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Error: divorce occurs after husband death. Divorce Date: 2050-02-02 Husband Death: 2030-01-01'])

if __name__ == "__main__":
    unittest.main()
