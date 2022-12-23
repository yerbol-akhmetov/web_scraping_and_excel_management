# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:22:08 2022

@author: Yerbol
"""


import os
import pandas as pd
from header_coord_extractor import get_header_coord
from excel_reader import excel_reader
from code_price_scrapper import get_code_price
from object_creator import get_item_list
from excel_writer import excel_writer


# directory of excel datasheet
FILENAME = "TestTask_1_input_1.xlsx"
DIRECTORY = "./data"
OUT_TEMPLATE= "TestTask_1_output_blank_template.xlsx"
OUT_FILENAME = "TestTask_1_output_1.xlsx"
OUT_KEY_WORDS = ["наименование", "артикул", "ссылка", "цена"]


def main_extractor(in_filename, in_dir, out_filename, out_dir):
    # extarcting content of input excel file
    content_df = excel_reader(filename=in_filename, directory=in_dir)
    # extracting "Наименование" and "URL" header coordinates
    name_coord_list, url_coord_list = get_header_coord(content_df)
    # obtaining list of objects containing information about items
    items = get_item_list(content_df, name_coord_list, url_coord_list)
    
    
    # writing the extracted data to output excel file
    excel_writer(filename=out_filename, directory=out_dir, 
                 items=items, key_headers=OUT_KEY_WORDS)



if __name__ == "__main__":
    
    main_extractor(in_filename=FILENAME, in_dir=DIRECTORY, 
                   out_filename=OUT_FILENAME, out_dir=DIRECTORY)
    