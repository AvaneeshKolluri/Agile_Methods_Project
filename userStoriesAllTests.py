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
from test_userStory11 import TestUserStory11Class
from test_userStory12 import TestUserStory12Class
from test_userStory13 import TestUserStory13Class
from test_userStory14 import TestUserStory14Class
from test_userStory15 import TestUserStory15Class
from test_userStory16 import TestUserStory16Class
from test_userStory17 import TestUserStory17Class
from test_userStory18 import TestUserStory18Class
from test_userStory19 import UserStory19Test
from test_userStory20 import UserStory20Test
from test_userStory21 import UserStory21Test
from test_userStory22 import UserStory22Test

# Sprint1 and Sprint2 class with all Sprint1 and Sprint2 tests
class Test_Sprint1n2(unittest.TestCase):
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
    TestUserStory11Class()
    TestUserStory12Class()
    TestUserStory13Class()
    TestUserStory14Class()
    TestUserStory15Class()
    TestUserStory16Class()
    TestUserStory17Class()
    TestUserStory18Class()
    UserStory19Test()
    UserStory20Test()
    UserStory21Test()
    UserStory22Test()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./sprint1n2Reports'))