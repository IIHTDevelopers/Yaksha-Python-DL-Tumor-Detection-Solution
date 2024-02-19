import os
import unittest
from TestUtils import TestUtils

class ExceptionalTests(unittest.TestCase):
    model_path = "model_path"

    def test_model_exists(self):
        test_obj = TestUtils()
        try:
            model_exists = os.path.exists(self.model_path)
            if model_exists:
                passed  = True
                test_obj.yakshaAssert("TestModelExists", True, "exception")
                print("TestModelExists= Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestModelExists", False, "exception")
                print("TestModelExists = Failed")
                exit()
        except:
            passed = False
            test_obj.yakshaAssert("TestModelExists", False, "exception")
            print("TestModelExists = Failed")
            exit()
        assert passed



def path_test(model_path):
    ExceptionalTests.model_path = model_path
    unittest.main() 