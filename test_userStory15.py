import unittest
from userStories import userStory15

'''
User story 15:
Requirement: There can be no more than 15 siblings
'''
# Test Class for User Story 15
class TestUserStory15Class(unittest.TestCase):

    def test_UserStory15_1(self):
        resultsList = userStory15("InputGedFiles/UserStory15_GED/test.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ERROR: FAMILY: US15: 184: There must be fewer than 15 siblings. F1 has more than 15 siblings. 15 >= 15."])
    def test_UserStory15_2(self):
        resultsList = userStory15("InputGedFiles/UserStory15_GED/test2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList,[])

if __name__ == "__main__":
    unittest.main()
    
