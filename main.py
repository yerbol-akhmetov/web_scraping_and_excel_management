# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:22:08 2022

@author: Yerbol
"""


import os
import pandas as pd
from header_coord_extractor import get_header_coord


FILENAME = "TestTask_1_input_1.xlsx"
DIRECTORY = "./data"
content_df = pd.read_excel(os.path.join(DIRECTORY, FILENAME),header=None)

print(get_header_coord(content_df))

