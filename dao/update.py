from dao.exec import *


def update(loc, tb_name, ls):
    sql = f'UPDATE {tb_name} set master_tag=1 where prod_name=? and ct=?'
    executemany_statement(loc, sql, ls)


def update_data_dic(loc, ct, ls):
    sql = f'UPDATE tb_data_dic set {ct}=? where feat=?'
    executemany_statement(loc, sql, ls)
    # ls = rd.get_has_text(loc, ct, has_text)
    # text_str = (','.join(map(lambda x: str(x[0]), ls)))
    # sql = f'UPDATE tb_data_dic set {ct}="{text_str}" where feat="{cond}"'
    # execute_statement(loc, sql)


def update_processed(loc, ls, col_name, flag):
    sql = f'UPDATE tb_processed set {col_name}={flag} where prod_name=? and ct=?'
    executemany_statement(loc, sql, ls)


def update_processed_remove(loc, ls, col_name, flag):
    sql = f'UPDATE tb_processed set {col_name}={flag} where ct=?'
    executemany_statement(loc, sql, ls)


def update_tag_master_data_dic(loc, ls):
    sql = f'UPDATE tb_tag_ct set map_tag=? where tag=? and ct=?'
    executemany_statement(loc, sql, ls)


def update_has_text_tag(loc, ls):
    sql = f'UPDATE tb_tag_ct set map_tag="text" where tag=? and ct=?'
    executemany_statement(loc, sql, ls)


def update_has_text_tag_tag_master(loc, ls):
    sql = f'UPDATE tb_master_tag set has_text="yes" where tag=? and ct=?'
    executemany_statement(loc, sql, ls)
