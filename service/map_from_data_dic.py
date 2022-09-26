import re

import pandas as pd

from dao import read as rd


def map_tag(loc, ct, ls_data_dic_mapping):
    df = pd.read_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_xpath.xlsx', sheet_name='Sheet1')

    for tu in ls_data_dic_mapping:
        df['m_xpath'].replace(to_replace=r'/' + tu[0] + '\\b', value='/' + tu[1], regex=True, inplace=True)
        # df['m_xpath'].replace(to_replace='/' + tu[0] + '$', value='/' + tu[1], regex=True, inplace=True)

    ls = rd.get_patt_to_be_replaced_fixed(loc)
    for tu in ls:
        df['m_xpath'].replace(to_replace=tu[0], value=tu[1], regex=True, inplace=True)

    df.to_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_tag.xlsx', index=False)
    return True


def process_data_dic(loc, ct):
    ls = rd.read_data_dic(loc, ct)
    my_ls = []
    for tu in ls:
        if tu[1]:
            s = re.sub(",|\n|\r|\t", " ", tu[1])
            temp_ls = s.split()
            for item in temp_ls:
                my_ls.append((item, tu[0]))
    map_tag(loc, ct, my_ls)
