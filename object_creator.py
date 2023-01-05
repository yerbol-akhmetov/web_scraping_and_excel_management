# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:24:58 2022

@author: Yerbol

This module stores all information of items as an object and returns them 
"""

import pandas as pd
from code_price_scrapper import get_code_price


# Item class
class Item(object):
    def __init__(self, name, url, price, code):
        self.name = name
        self.url = url
        self.code = code
        self.price = price
        


# function that stores information of items as an object
def get_item_list(content_df, name_coord_list, url_coord_list):
    """
    This method stores information of items as an object

    Parameters
    ----------
    content_df : Pandas DataFrame
        Content of excel file in DataFrame format.
    name_coord_list : LIST of TUPLES
        (j, i) coordinates of "Наименование" headers.
    url_coord_list : LIST of TUPLES
        (j, i) coordinates of "URL" headers.

    Returns
    -------
    items : List 
        List contains objects (items)

    """
    items = []  # initialize list to store objects
    
    
    for name_coord, url_coord in zip(name_coord_list, url_coord_list):
        # converting name and url header coordinates from tuple to list
        name_coord = list(name_coord)
        url_coord = list(url_coord)
        while not pd.isnull(content_df.iloc[name_coord[0]+1, name_coord[1]]) and \
              not pd.isnull(content_df.iloc[url_coord[0]+1, url_coord[1]]):
            
            name_coord[0] += 1  # coordinates of item name
            url_coord[0] += 1   # coordinates of item url
            
            # item name, url, code, and price
            item_name = content_df.iloc[name_coord[0], name_coord[1]]
            item_url = content_df.iloc[url_coord[0], url_coord[1]]
            item_code, item_price = get_code_price(item_url)
            
            # crating objects and appending to the list 
            items.append(Item(name=item_name,
                              url=item_url,
                              price=item_price,
                              code=item_code))
    
    return items