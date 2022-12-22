# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:44:39 2022

@author: Yerbol

This module reads excel spreadsheet and returns the content as DataFrame
"""


import os
import pandas as pd


# directory of excel datasheet
FILENAME = "TestTask_1_input_1.xlsx"
DIRECTORY = "./data"


# function to read excel sheet and return Pandas dataframe
def excel_reader():
    """
    This function to read excel sheet and return Pandas dataframe

    Returns
    -------
    content_df : Pandas DataFrame
        Pandas Dataframe containing content of excel sheet.

    """
    # joining directories to obtain full path
    directory = os.path.join(DIRECTORY, FILENAME)
    # reading excel file
    content_df = pd.read_excel(directory, header=None)
    
    return content_df