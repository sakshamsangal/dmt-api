import pandas as pd

if __name__ == '__main__':
    loc = ''
    ct = ''
    df = pd.read_excel(f'{loc}/{ct}/excel/dm_sheet/{ct}_tag.xlsx', sheet_name='Sheet1')
    df.to_csv(f'{loc}/{ct}/excel/{ct}_csv.csv', encodings='utf-8')

    source_path = ".csv"
    for i, chunk in enumerate(pd.read_csv(source_path, chunksize=40000, dtype=dtypes)):
        chunk.to_csv('../tmp/split_csv_pandas/chunk{}.csv'.format(i), index=False)
