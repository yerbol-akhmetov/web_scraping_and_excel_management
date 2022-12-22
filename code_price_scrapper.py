# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:10:44 2022

@author: Yerbol
"""


from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


# method that extracts code and price of the items
def get_code_price(url):
    """
    

    Parameters
    ----------
    url : URL
        URL of the item to be scrapped.

    Returns
    -------
    code : STRING
        Unique code of the item (index).
    price : INTEGER
        The price of the item.

    """
    op = ChromeOptions()
    op.add_argument('headless')     # option to prevent browser opening
    # showing the path to the driver
    driver = Chrome(executable_path='driver/chromedriver',options=op)
    driver.get(url)     # accessing to url
    
    
    return code, price
    
