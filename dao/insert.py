from dao.exec import *


def insert(loc, tb_name, col_no, ls):
    val = ','.join(['?'] * col_no)
    sql = f'INSERT INTO {tb_name} VALUES({val})'
    executemany_statement(loc, sql, ls)


def insert_ignore(loc, tb_name, col_no, ls):
    val = ','.join(['?'] * col_no)
    sql = f'INSERT OR IGNORE INTO {tb_name}  VALUES({val})'
    executemany_statement(loc, sql, ls)


def insert_ignore_processed(loc, ls):
    sql = f'INSERT OR IGNORE INTO tb_processed (prod_name,ct) VALUES(?,?)'
    executemany_statement(loc, sql, ls)
