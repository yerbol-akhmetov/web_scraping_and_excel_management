"""
This module extracts j,i coordinates of important headers of tables from 
Pandas DataFrame 

"""


KEY_WORDS = ["наименование", "ссылка"]  # key words of the header


# method for extracting the j,i coordinates of headers
def get_header_coord(content_df, key_words=KEY_WORDS):
    """
    This method returns j, i coordinates of "Наименование" and "URL" headers

    Parameters
    ----------
    content_df : Pandas Dataframe
        The input dataframe containing the excel sheet information.

    Returns
    -------
    name_idx_list : LIST of TUPLES
        (j, i) coordinates of "Наименование" header for tables.
    url_idx_list : LIST of TUPLES
        (j, i ) coordinates of "URL" header for tables.

    """
    headers_idx_list = []  
    len_key_words = len(key_words)
    
    # looping through each cell of DataFrame to find headers
    for j in range(content_df.shape[0]):
        for i in range(content_df.shape[1]):
            name_idx_i, name_idx_j = 0, 0
            url_idx_i, url_idx_j = 0, 0
            # finding cell with "Наименование", "URL" headers
            for key_word in key_words:
                if str(content_df.iloc[j,i]).lower() == key_word:
                    headers_idx_list.append((j, i))    # appending coordinates
                
    if len_key_words == 2:
        return headers_idx_list[0::2], headers_idx_list[1::2]
    elif len_key_words == 4:
        return headers_idx_list[0::4], headers_idx_list[1::4], headers_idx_list[2::4], headers_idx_list[3::4]