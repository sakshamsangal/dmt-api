import contextlib
import sqlite3


def execute_statement(loc, sql):
    with contextlib.closing(sqlite3.connect(f'{loc}/dmt_master.db')) as conn:  # auto-closes
        with conn:  # auto-commits
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                try:
                    cursor.execute(sql)
                    return 'success'
                except Exception as e:
                    return str(e)


def get_list_of_dic(result):
    ls = []
    for item in result:
        ls.append({k: item[k] for k in item.keys()})
    return ls


def execute_statement_return(loc, sql):
    with contextlib.closing(sqlite3.connect(f'{loc}/dmt_master.db')) as conn:  # auto-closes
        conn.row_factory = sqlite3.Row
        with conn:  # auto-commits
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                cursor.execute(sql)
                result = cursor.fetchall()
                return get_list_of_dic(result)


def execute_statement_return_lot(loc, sql):
    with contextlib.closing(sqlite3.connect(f'{loc}/dmt_master.db')) as conn:  # auto-closes
        with conn:  # auto-commits
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                cursor.execute(sql)
                return cursor.fetchall()


def execute_statement_return_single(loc, sql):
    with contextlib.closing(sqlite3.connect(f'{loc}/dmt_master.db')) as conn:  # auto-closes
        with conn:  # auto-commits
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                cursor.execute(sql)
                return cursor.fetchone()


def executemany_statement(loc, sql, ls):
    with contextlib.closing(sqlite3.connect(f'{loc}/dmt_master.db')) as conn:  # auto-closes
        with conn:  # auto-commits
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                cursor.executemany(sql, ls)
                return True
