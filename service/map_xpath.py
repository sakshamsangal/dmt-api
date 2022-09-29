import os

import pandas as pd

from dao import read as rd


def map_xpath_to_tag(loc, ct, file_name, sn):
    os.makedirs(f'{loc}/{ct}/excel/dm_sheet', exist_ok=True)
    df = pd.read_excel(f'{loc}/{ct}/excel/{file_name}.xlsx', sheet_name=sn)
    t = ('m_xpath', 'comp', 'style', 'feat', 'comment', 'phase')
    for i, x in enumerate(t):
        df.insert(i, x, '')
    df['m_xpath'] = df['Legacy Xpaths']
    ls = rd.get_patt_to_be_replaced(loc, ct)
    for tu in ls:
        df['m_xpath'].replace(to_replace=fr'{tu[0]}\\b', value=tu[1], regex=True, inplace=True)
    df.to_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_xpath.xlsx', index=False)
    return True

