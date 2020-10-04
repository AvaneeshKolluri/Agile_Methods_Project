import unittest
import HtmlTestRunner
from sprint1UserStories import userStory08

'''
User story 08:
Requirement: Children should be born after marriage of parents (and not more than 9 months after their divorce)
'''
# Test Class for User Story 08
class TestUserStory08Class(unittest.TestCase):

    def test_UserStory08_1(self):
        resultsList = userStory08("InputGedFiles/UserStory08_GED/testUserStory08-1.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, ["ANOMALY: FAMILY: US08: F1: Child I5 born 1988-07-08 before marriage on 1997-12-31"])

    def test_UserStory08_2(self):
        resultsList = userStory08("InputGedFiles/UserStory08_GED/testUserStory08-2.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [])
    def test_UserStory08_3(self):
        resultsList = userStory08("InputGedFiles/UserStory08_GED/testUserStory08-3.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ANOMALY: FAMILY: US08: F3: Child I1 born 1869-09-25 before marriage on 1962-08-24"])

    def test_UserStory08_4(self):
        resultsList = userStory08("InputGedFiles/UserStory08_GED/testUserStory08-4.ged")
        resultsList.sort()
        self.maxDiff = None
        self.assertEqual(resultsList, ["ANOMALY: FAMILY: US08: F1: Child I5 born 1853-07-08 before marriage on 1997-12-31",
                                       "ANOMALY: FAMILY: US08: F1: Child I6 born 1870-10-31 before marriage on 1997-12-31",
                                       "ANOMALY: FAMILY: US08: F2: Child I3 born 1866-11-11 before marriage on 1967-05-09",
                                       "ANOMALY: FAMILY: US08: F3: Child I1 born 1868-09-25 before marriage on 1962-08-24"])

    def test_UserStory08_5(self):
        resultsList = userStory08("InputGedFiles/UserStory08_GED/testUserStory08-5.ged")
        self.maxDiff = None
        self.assertEqual(resultsList, [ "ANOMALY: FAMILY: US08: F2: Child I3 born 1996-09-11 after divorce on 1995-12-10"])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
