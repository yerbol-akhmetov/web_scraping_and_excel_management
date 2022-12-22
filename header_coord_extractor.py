"""
This module extracts j,i coordinates of important headers of tables from 
Pandas DataFrame 

"""


KEY_WORDS = ["наименование", "ссылка"]  # key words of the header


# method for extracting the j,i coordinates of headers
def get_header_coord(content_df):
    """
    This method returns j, i coordinates of "Наименование" and "URL" headers

    Parameters
    ----------
    content_df : Pandas Dataframe
        DESCRIPTION.

    Returns
    -------
    name_idx_list : list of coordinates of "Наименование" header for tables
        DESCRIPTION.
    url_idx_list : list of coordinates of "URL" header for tables
        DESCRIPTION.

    """
    name_idx_list = []  
    url_idx_list = []
    
    
    
    return name_idx_list, url_idx_list