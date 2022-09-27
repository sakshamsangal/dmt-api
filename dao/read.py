from dao.exec import *


def check_if_record_exist(loc, prod_name):
    sql = f'''
        SELECT EXISTS(SELECT 1 FROM tb_processed WHERE prod_name="{prod_name}");
    '''

    return execute_statement_return_single(loc, sql)


def merge(loc, t1, t2, col_to_comp):
    sql = f"""
        INSERT INTO {t1} 
        SELECT * FROM {t2} A 
        WHERE NOT EXISTS (SELECT 1 FROM {t1} X WHERE A.{col_to_comp} = X.{col_to_comp})
        """
    execute_statement(loc, sql)


def get_selected_file_name(loc):
    sql = '''SELECT distinct file_name, prod_name from tb_master_tag'''
    return execute_statement_return(loc, sql)


def get_tag_map(loc, ct):
    sql = f'''SELECT tag,map_tag from tb_tag_ct where ct="{ct}"'''
    return execute_statement_return_lot(loc, sql)


def get_feat(loc):
    sql = f'''SELECT * from tb_pattern_feat order by priority'''
    return execute_statement_return_lot(loc, sql)


def get_comp_style(loc):
    sql = f'''SELECT * from tb_comp_style'''
    # sql = f'''SELECT * from tb_comp_style where ct="{ct}" and is_proc=0 order by priority'''
    return execute_statement_return_lot(loc, sql)


def get_exception_data(loc, ct):
    sql = f'''SELECT * from tb_exception where ct in ("{ct}", "gen") order by priority'''
    return execute_statement_return_lot(loc, sql)


def get_has_text(loc, ct, has_text):
    sql = f'''SELECT tag from tb_master_tag where ct="{ct}" and has_text="{has_text}"'''
    return execute_statement_return_lot(loc, sql)


def get_phase(loc, ct, alpha_no):
    sql = f'''SELECT * from tb_phase where ct="{ct}" order by alpha{alpha_no} desc'''
    return execute_statement_return_lot(loc, sql)


def get_patt_to_be_replaced(loc, ct):
    sql = f'''SELECT pat, map_to from tb_map_xpath where ct="{ct}" order by priority'''
    return execute_statement_return_lot(loc, sql)


def get_patt_to_be_replaced_fixed(loc):
    sql = f'''SELECT pat, map_to from tb_map_xpath_fixed where ct="gen" order by priority'''
    return execute_statement_return_lot(loc, sql)


def read_data_dic(loc, ct):
    sql = f'''SELECT feat, {ct} from tb_data_dic'''
    return execute_statement_return_lot(loc, sql)
