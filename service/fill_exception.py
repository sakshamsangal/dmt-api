import re

import pandas as pd

from dao import read as rd
from service.fill_comp_style import remove_processed_record


def fill_exception(loc, ct, df, df_new):
    ls = rd.get_exception_data(loc, ct)
    for tu in ls:
        pat = re.compile(tu[0])
        for index, row in df.iterrows():
            if re.fullmatch(pat, row[tu[8]]):
                df.iat[index, 1] = tu[1]  # comp
                df.iat[index, 2] = tu[2]  # styling
                if tu[5] == 1:
                    df.iat[index, 3] = tu[1]  # feat
                else:
                    if pd.isnull(df.iloc[index, 3]):
                        df.iat[index, 3] = tu[1]  # feat
                df.iat[index, 4] = tu[4]  # comm

        df, df_new = remove_processed_record(df, df_new)
    return df, df_new
