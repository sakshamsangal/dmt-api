import re

import pandas as pd

from dao import read as rd


def fill_feature(loc, ct):
    ls = rd.get_feat(loc)
    df = pd.read_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_tag.xlsx', sheet_name='Sheet1')

    for tu in ls:
        # my_patt = tu[0].replace('*', '(.*?)')
        pat = re.compile(tu[0])
        for index, row in df.iterrows():
            if re.fullmatch(pat, row['m_xpath']):
                df.iat[index, 0] = pat.sub('\\1', row['m_xpath'])
                if pd.isnull(df.iloc[index, 3]):
                    df.iat[index, 3] = tu[1]  # feat

    df.to_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_feat.xlsx', index=False)
    return ls
