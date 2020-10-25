import unittest
from sprint1UserStories import userStory12
import HtmlTestRunner

class TestUserStory12Class(unittest.TestCase):

    
    """ Test the marriage_after_14 function from US10 """


    def test_user_story_12_1(self):

        resultsList = userStory12("InputGedFiles/UserStory12_GED/testUserStory12-1.ged")
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US12: I7: Mother I7 is more than 60 years older than her child (I1): Willard Carroll Smith.'])

    def test_user_story_12_2(self):

        resultsList = userStory12("InputGedFiles/UserStory12_GED/testUserStory12-2.ged")
        self.assertEqual(resultsList,['ERROR: INDIVIDUAL: US12: I1: Father I1 is more than 80 years older than his child (I3): Trey Smith.',
                                      'ERROR: INDIVIDUAL: US12: I1: Father I1 is more than 80 years older than his child (I5): Jaden Christopher Syre Smith.',
                                      'ERROR: INDIVIDUAL: US12: I1: Father I1 is more than 80 years older than his child (I6): Willow Camille Reign Smith.'])

    def test_user_story_12_3(self):

        resultsList = userStory12("InputGedFiles/UserStory12_GED/testUserStory12-3.ged")
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US12: I1: Father I1 is more than 80 years older than his child (I3): Trey Smith.', 'ERROR: INDIVIDUAL: US12: I1: Father I1 is more than 80 years older than his child (I5): Jaden Christopher Syre Smith.', 'ERROR: INDIVIDUAL: US12: I1: Father I1 is more than 80 years older than his child (I6): Willow Camille Reign Smith.', 'ERROR: INDIVIDUAL: US12: I2: Mother I2 is more than 60 years older than her child (I3): Trey Smith.'])

    def test_user_story_12_4(self):

        resultsList = userStory12("InputGedFiles/UserStory12_GED/testUserStory12-4.ged")
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US12: I7: Mother I7 is more than 60 years older than her child (I9): Julia Elk.'])

    def test_user_story_12_5(self):

        resultsList = userStory12("InputGedFiles/UserStory12_GED/testUserStory12-5.ged")
        self.assertEqual(resultsList, ['ERROR: INDIVIDUAL: US12: I7: Mother I7 is more than 60 years older than her child (I1): Willard Carroll Smith.'])

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
