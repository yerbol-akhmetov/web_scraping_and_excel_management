# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:11:42 2022

@author: Yerbol

Excel writer file
"""

import os
import pandas as pd
from excel_reader import excel_reader
from header_coord_extractor import get_header_coord


DIRECTORY = "./data"
OUT_TEMPLATE= "TestTask_1_output_blank_template.xlsx"


def excel_writer(filename, directory, items, key_headers):
    """
    This method writes item information to excel file

    Parameters
    ----------
    filename : STRING (.xlsx)
        Name of the output filename.
    directory : STRING
        Directory of output file.
    items : LIST of OBJECTS
        List of information about the items.
    key_headers : LIST of STRING
        Header names whose data will be written to excel file.

    Returns
    -------
    None.

    """
    
    # the content of output excel file
    out_df = excel_reader(filename=OUT_TEMPLATE, directory=directory)
    # copying the headers from template
    full_path = os.path.join(directory, filename)
    writer = pd.ExcelWriter(full_path, engine='openpyxl')
    out_df.to_excel(writer, sheet_name='Sheet1',
                    header=False, index=False)
    writer.close()
    
    # header locations in output excel file
    name_idx, code_idx, \
    url_idx, price_idx = get_header_coord(out_df, key_words=key_headers)
    
    # forming lists of item names, codes, urls, and prices
    name_list, code_list = [], []
    url_list, price_list = [], []
    for item in items:
        name_list.append(item.name)
        code_list.append(item.code)
        url_list.append(item.url)
        price_list.append(item.price)
    
    # creation of dataframes to be written to excel file
    df_name = pd.DataFrame(name_list)
    df_code = pd.DataFrame(code_list)
    df_url = pd.DataFrame(url_list)
    df_price = pd.DataFrame(price_list)
    df_number = pd.DataFrame(range(1,len(name_list)+1))
    
    # creation of excel writer 
    full_path = os.path.join(directory, filename)
    writer = pd.ExcelWriter(full_path, engine='openpyxl', 
                            mode='a', if_sheet_exists='overlay')
    
    # writing name, code, url, price, number information to excel sheet
    df_name.to_excel(writer, sheet_name='Sheet1',
                     startrow=name_idx[0][0]+1, startcol=name_idx[0][1], 
                     header=False, index=False)
    df_code.to_excel(writer, sheet_name='Sheet1',
                     startrow=code_idx[0][0]+1, startcol=code_idx[0][1], 
                     header=False, index=False)
    df_url.to_excel(writer, sheet_name='Sheet1',
                    startrow=url_idx[0][0]+1, startcol=url_idx[0][1], 
                    header=False, index=False)
    df_price.to_excel(writer, sheet_name='Sheet1',
                      startrow=price_idx[0][0]+1, startcol=price_idx[0][1], 
                      header=False, index=False)
    df_number.to_excel(writer, sheet_name='Sheet1',
                       startrow=name_idx[0][0]+1, startcol=name_idx[0][1]-1, 
                       header=False, index=False)
    
    writer.close()