# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:30:02 2022

@author: Yerbol

This module performs test of the proposed method
"""

import os
import unittest
import filecmp
from main import main_extractor
from excel_reader import excel_reader
from pandas.testing import assert_frame_equal


# directory of excel datasheet
TEST_FILENAME = "TestTask_1_input_2.xlsx"
OUT_FILE_TEST = "TestTask_1_output_2.xlsx"
TEST_DIRECTORY = "./test_data"

OUT_FILE_ACTUAL = "TestTask_1_output_1.xlsx"
OUT_DIRECTORY = "./data"


class TestExcelExtractor(unittest.TestCase):

    def test_table_relocation(self):
        
        # generation of test output excel file
        main_extractor(in_filename=TEST_FILENAME, in_dir=TEST_DIRECTORY, 
                       out_filename=OUT_FILE_TEST, out_dir=TEST_DIRECTORY)
        
        # content of correct referece output
        ref_df = excel_reader(filename=OUT_FILE_ACTUAL, 
                              directory=OUT_DIRECTORY)
        # content of test output
        test_df = excel_reader(filename=OUT_FILE_TEST, 
                              directory=TEST_DIRECTORY)
        
        try:
            assert_frame_equal(ref_df, test_df)
        except AssertionError as e:
            raise self.failureException("Contents are not equal") from e
            

    
if __name__ == "__main__":
    unittest.main()

    