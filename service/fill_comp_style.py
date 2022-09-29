import re

import pandas as pd

from dao import read as rd


def remove_processed_record(df, df_new):
    rows = df.loc[pd.isnull(df['comp']) == False, :]
    df_new = pd.concat([df_new, pd.DataFrame.from_records(rows)])
    df.drop(rows.index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df, df_new


def remove_processed_record1(df, df_new):
    rows = df.loc[df['comp'] != df['Component'], :]
    df_new = pd.concat([df_new, pd.DataFrame.from_records(rows)])
    df.drop(rows.index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df, df_new


def update_df(df, short_str, comp, style, feat):
    for index, row in df.iterrows():
        if row['m_xpath'].endswith(short_str):
            df.iat[index, 1] = comp  # comp
            df.iat[index, 2] = style  # style
            if pd.isnull(df.iloc[index, 3]):
                df.iat[index, 3] = feat  # feat
    return df


def my_ends_with(loc, df, df_new):
    ls = rd.get_comp_style(loc)
    # id comp=1 h1=2 h2=3 text=4 feat=5
    for tu in ls:
        df = update_df(df, f'/text', tu[1], tu[4], tu[5])
        df, df_new = remove_processed_record(df, df_new)

    for tu in ls:
        df = update_df(df, f'/{tu[0]}', tu[1], tu[2], tu[5])
        df = update_df(df, f'/{tu[0]}/h1', tu[1], tu[2], tu[5])
        df = update_df(df, f'/{tu[0]}/h2', tu[1], tu[3], tu[5])
        df, df_new = remove_processed_record(df, df_new)

    return df, df_new


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


def fill_comp_style(loc, ct, fn):
    df = pd.read_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_feat.xlsx', sheet_name='Sheet1')
    df_new = pd.DataFrame(columns=df.columns)
    df, df_new = fill_exception(loc, ct, df, df_new)
    df, df_new = my_ends_with(loc, df, df_new)

    df_new.to_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_dm.xlsx', index=False)
    df.to_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_feat.xlsx', index=False)
    c = df.shape[0]

    df_new1 = pd.DataFrame(columns=df.columns)
    df, df_new = remove_processed_record1(df_new, df_new1)
    df_new.drop(df_new.columns[0:6], axis=1, inplace=True)
    df_new.to_excel(f'{loc}/{ct}/excel/{fn}.xlsx', index=False)

    return c


