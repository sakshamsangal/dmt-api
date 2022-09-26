from dao.exec import *


def delete_prod(loc, ls_prod):
    sql = f"delete from tb_master_tag where prod_name=?"
    executemany_statement(loc, sql, ls_prod)

    sql = f"delete from tb_processed where prod_name=?"
    return executemany_statement(loc, sql, ls_prod)


def delete_ct(loc, ls_ct, mt):
    if mt == 'master_tag':
        sql = f"delete from tb_master_tag where ct=?"
        executemany_statement(loc, sql, ls_ct)

        sql = f"delete from tb_tag_ct where ct=?"
        executemany_statement(loc, sql, ls_ct)

    elif mt == 'master_pc':
        sql = f"delete from tb_master_pc where ct=?"
        executemany_statement(loc, sql, ls_ct)

    elif mt == 'master_att':
        sql = f"delete from tb_master_att where ct=?"
        executemany_statement(loc, sql, ls_ct)


def drop_tb(loc, tb_name):
    sql = f"drop table {tb_name}"
    return execute_statement(loc, sql)


def remove_file(loc, tb_name, file_name):
    sql = f"delete from {tb_name} where file_name='{file_name}'"
    return execute_statement(loc, sql)
