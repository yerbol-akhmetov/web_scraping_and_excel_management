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
    
    # looping through each cell of DataFrame to find headers
    for j in range(content_df.shape[0]):
        for i in range(content_df.shape[1]):
            name_idx_i, name_idx_j = 0, 0
            url_idx_i, url_idx_j = 0, 0
            # finding cell with "Наименование" content
            if str(content_df.iloc[j,i]).lower() == KEY_WORDS[0]:
                name_idx_list.append((j, i))    # appending coordinates
            # finding cell with item URLs
            if str(content_df.iloc[j,i]).lower() == KEY_WORDS[1]:
                url_idx_list.append((j, i))     # appending header coordinates
    
    return name_idx_list, url_idx_list