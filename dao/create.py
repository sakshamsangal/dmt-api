from dao.exec import *


def create_tb_master_pc(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        id text NOT NULL PRIMARY KEY,
        tag text,
        file_name text,
        prod_name text,
        ct text
    )"""
    execute_statement(loc, sql)


def create_tb_data_dic(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        feat text NOT NULL PRIMARY KEY
    )"""
    execute_statement(loc, sql)


def create_tb_tag_ct(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        id text NOT NULL PRIMARY KEY,
        tag text,
        map_tag text,
        ct text
    )"""
    execute_statement(loc, sql)


def create_tb_processed(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        prod_name text NOT NULL PRIMARY KEY,
        ct text,
        master_tag int default 0,
        master_att int default 0,
        master_xpath int default 0,
        master_pc int default 0
    )"""
    execute_statement(loc, sql)


def create_tb_map_xpath(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        pat text NOT NULL PRIMARY KEY,
        map_to text,
        ct text,
        priority int
    )"""
    execute_statement(loc, sql)


def create_tb_exception(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        pat text NOT NULL PRIMARY KEY,
        comp text,
        styling text,
        feat text,
        comm text,
        overwrite_feat int,
        ct text,
        priority int,
        pat_col text default 'm_xpath'
    )"""
    execute_statement(loc, sql)


def create_tb_master_tag(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        tag text NOT NULL PRIMARY KEY,
        rendered text,
        file_name text,
        prod_name text,
        ct text,
        file_size real default 0,
        has_text text
    )"""
    execute_statement(loc, sql)


def create_tb_master_att(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        id text NOT NULL PRIMARY KEY,
        tag text,
        att_key text,
        att_val text,
        file_name text,
        prod_name text,
        ct text
    )"""
    execute_statement(loc, sql)


def create_tb_pattern_feat(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        pat text NOT NULL PRIMARY KEY,
        feat text,
        priority int
    )"""
    execute_statement(loc, sql)


def create_tb_phase(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        feat text NOT NULL PRIMARY KEY,
        alpha1 int,
        alpha2 int,
        filter_on_col text,
        ct text
    )"""
    execute_statement(loc, sql)


def create_tb_comp_style(loc, tb_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {tb_name} (
        id text NOT NULL PRIMARY KEY,
        comp text,
        h1_style text,
        h2_style text,
        text_style text,
        feat text
    )"""
    execute_statement(loc, sql)


def add_column(loc, ct, tb_name):
    sql = f'ALTER TABLE {tb_name} ADD COLUMN {ct} text'
    return execute_statement(loc, sql)


def create_all_tb(loc):
    create_tb_map_xpath(loc, 'tb_map_xpath')
    create_tb_map_xpath(loc, 'tb_map_xpath_fixed')
    create_tb_exception(loc, 'tb_exception')
    create_tb_master_tag(loc, 'tb_master_tag')

    create_tb_tag_ct(loc, 'tb_tag_ct')

    create_tb_processed(loc, 'tb_processed')
    create_tb_pattern_feat(loc, 'tb_pattern_feat')
    create_tb_comp_style(loc, 'tb_comp_style')
    create_tb_phase(loc, 'tb_phase')
    create_tb_data_dic(loc, 'tb_data_dic')

    create_tb_master_att(loc, 'tb_master_att')
    create_tb_master_pc(loc, 'tb_master_pc')


if __name__ == '__main__':
    loc = 'C:/Users/saksangal/Pictures/saksham'
    ct = 'deskbook'
    create_tb_data_dic(loc, 'tb_data_dic')
    # create_all_tb(loc)
