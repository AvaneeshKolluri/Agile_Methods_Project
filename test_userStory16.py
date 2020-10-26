import unittest
from userStories import userStory16

'''
User story 16:
Requirement: Return the last names of all the males
'''
# Test Class for User Story 16
class TestUserStory16Class(unittest.TestCase):

    def test_UserStory16_1(self):
        resultsList = userStory16("InputGedFiles/UserStory16_GED/test.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Johnson', 'Johnson', 'Johnson', 'Johnson', 'Johnson', 'Johnson', 'Johnson', 'Johnson', 'Johnson'])
    def test_UserStory16_2(self):
        resultsList = userStory16("InputGedFiles/UserStory16_GED/test2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Line'])
    def test_UserStory16_3(self):
        resultsList = userStory16("InputGedFiles/UserStory16_GED/FamilyTree.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ['Mapother', 'Mapother', 'Cruise'])

if __name__ == "__main__":
    unittest.main()
    
