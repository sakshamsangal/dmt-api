import pandas as pd

from dao import read as rd


def map_tag(loc, ct):
    df = pd.read_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_xpath.xlsx', sheet_name='Sheet1')

    ls = rd.get_tag_map(loc, ct)
    for tu in ls:
        if tu[1] == 'dual_nat':
            x = '/' + tu[0]
        else:
            x = '/' + tu[1]
        df['m_xpath'].replace(to_replace=r'/' + tu[0] + '\\b', value=x, regex=True, inplace=True)

    ls = rd.get_patt_to_be_replaced_fixed(loc)
    for tu in ls:
        df['m_xpath'].replace(to_replace=tu[0], value=tu[1], regex=True, inplace=True)

    df.to_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_tag.xlsx', index=False)
    return True
