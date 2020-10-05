import unittest
import HtmlTestRunner

from test_userStory01 import TestUserStory01Class
from test_userStory02 import TestUserStory02Class
from test_userStory03 import TestUserStory03Class
from test_userStory04 import TestUserStory04Class
from test_userStory05 import TestUserStory05Class
from test_userStory06 import TestUserStory06Class
from test_userStory07 import TestUserStory07Class
from test_userStory08 import TestUserStory08Class
from test_userStory09 import TestUserStory09Class
from test_userStory10 import TestUserStory10Class



# Sprint1 class with all Sprint1 tests
class Test_Sprint1(unittest.TestCase):
    TestUserStory01Class()
    TestUserStory02Class()
    TestUserStory03Class()
    TestUserStory04Class()
    TestUserStory05Class()
    TestUserStory06Class()
    TestUserStory07Class()
    TestUserStory08Class()
    TestUserStory09Class()
    TestUserStory10Class()
    


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
