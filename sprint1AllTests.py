import unittest
import HtmlTestRunner

from test_userStory01 import TestUserStory01Class
from test_userStory02 import TestUserStory02Class
from test_userStory07 import TestUserStory07Class
from test_userStory08 import TestUserStory08Class


# Sprint1 class with all Sprint1 tests
class Test_Sprint1(unittest.TestCase):
    TestUserStory01Class()
    TestUserStory02Class()
    TestUserStory07Class()
    TestUserStory08Class()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
