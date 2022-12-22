# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:22:08 2022

@author: Yerbol
"""


import os
import pandas as pd
from header_coord_extractor import get_header_coord
from excel_reader import excel_reader


content_df = excel_reader()

print(get_header_coord(content_df))

