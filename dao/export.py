import pandas as pd

from dao.exec import *


def export_tb_map_tag(loc, ct, tb_name):
    sql = f'''SELECT * from {tb_name}'''
    result = execute_statement_return(loc, sql)
    df = pd.DataFrame(result)
    df.to_excel(f'{loc}/{ct}/excel/tag_map_{ct}.xlsx', index=False)
