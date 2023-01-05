# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:10:44 2022

@author: Yerbol
"""


from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


# CSS Selector path for code and price of the items
CODE_CSS_SELECTOR = "div.q-ml-auto.text-ts1.text-color3"
PRICE_CSS_SELECTOR = "div.text-bold.text-ts5.text-color1"


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
    
    
    # fully item code from website
    item_code = driver.find_element(By.CSS_SELECTOR, CODE_CSS_SELECTOR)
    # full item price expression
    item_price = driver.find_element(By.CSS_SELECTOR, PRICE_CSS_SELECTOR)
    
    
    # extracting numeric code
    for elem in item_code.text.split():
        if elem.isdigit():
            code = elem
    
    # converting the price information into integer 
    price_list = []
    for elem in item_price.text.split():
        if elem.isdigit():
            price_list.append(elem) 
    price = int("".join(price_list))    # removing space separator
    
    return code, price
    
