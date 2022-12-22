# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:44:39 2022

@author: Yerbol

This module reads excel spreadsheet and returns the content as DataFrame
"""


import os
import pandas as pd


# function to read excel sheet and return Pandas dataframe
def excel_reader(filename, directory):
    """
    This function to read excel sheet and return Pandas dataframe
    Parameters
    ----------
    filename : STRING
        The name of the excel file.
    directory: STRING
        Directory of the excel file

    Returns
    -------
    content_df : Pandas DataFrame
        Pandas Dataframe containing content of excel sheet.

    """
    # joining directories to obtain full path
    full_path = os.path.join(directory, filename)
    # reading excel file
    content_df = pd.read_excel(full_path, header=None)
    
    return content_df