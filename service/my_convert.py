import re

from dao import read as rd
from dao import update as up


def convert_dd_to_tm(loc, ct):
    ls = rd.read_data_dic(loc, ct)
    my_ls = []
    for tu in ls:
        if tu[1]:
            s = re.sub(",|\n|\r|\t", " ", tu[1])
            temp_ls = s.split()
            for item in temp_ls:
                my_ls.append((tu[0], item, ct))
    up.update_tag_master_data_dic(loc, my_ls)
    return True


def convert_tm_to_dd(loc, ct):
    ls = rd.get_tag_map(loc, ct)
    dd = {}
    for tu in ls:
        if tu[1] in dd:
            dd[tu[1]].append(tu[0])
        else:
            dd[tu[1]] = [tu[0]]

    res = []
    for k, v in dd.items():
        res.append((','.join(v), k))

    up.update_data_dic(loc, ct, res)
    return True
