import unittest
import numpy as np

from TestUtils import TestUtils

class FuctionalTests(unittest.TestCase):
    pred_mask = np.array([])
    org_mask = np.array([])
    jaccard_cofficient = 0.0
    dice_score = 0.0
    
    def original_predicted_mask_same_size(self):
        test_obj = TestUtils()

        if (self.pred_mask.size == self.org_mask.size):
            passed = True
            test_obj.yakshaAssert("OriginalPredictedMaskSameSize", True, "functional")
            print("OriginalPredictedMaskSameSize = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("OriginalPredictedMaskSameSize", False, "functional")
            print("OriginalPredictedMaskSameSize = Failed")
        assert passed
    

    def metric_value_test(self):
        test_obj = TestUtils()
        
        if self.jaccard_cofficient > 0.8 and self.dice_score > 0.8:
            passed = True
            test_obj.yakshaAssert("ModelEvaluation", True, "functional")
            print("ModelEvaluation = Passed\nModel is good")
        else:
            passed = False
            test_obj.yakshaAssert("ModelEvaluation", False, "functional")
            print("ModelEvaluation = Failed\nModel is not good")
        assert passed



def model_tests(org_mask, pred_mask, jaccard_cofficient, dice_score):
    FuctionalTests.pred_mask = pred_mask
    FuctionalTests.org_mask = org_mask
    FuctionalTests.jaccard_cofficient = jaccard_cofficient
    FuctionalTests.dice_score = dice_score
    unittest.main() 
