from collections import defaultdict

from lxml import etree

from dao import create as cr
from dao import delete as dt
from dao import insert as ins
from dao import read as rd
from dao import update as up
from service.master import create_master as cm

pc_dic = {}
ct = ''
file_name = ''
prod_name = ''


def xml_traverse_pc(root):
    my_ls = []
    for child in root:
        if type(child) == etree._Element:
            child_name = etree.QName(child).localname
            my_ls.append(child_name)
            xml_traverse_pc(child)
    tag_name = etree.QName(root).localname

    counter = defaultdict(int)
    for letter in my_ls:
        counter[letter] += 1
    res = tag_name + '=>'
    for k, v in counter.items():
        res += f'_{k}({str(v)})'

    print(res)

    pc_dic[res] = (res, tag_name, file_name, prod_name, ct)


def process_master_pc(loc, content_type, all_dir, products):
    global pc_dic, file_name, prod_name, ct
    ct = content_type
    ls = []
    for root, f_name, p_name, f_size in cm.get_xml_root(loc, content_type, all_dir, products):
        file_name = f_name
        prod_name = p_name
        xml_traverse_pc(root)
        ls.append((prod_name, ct))

    cr.create_tb_master_pc(loc, 'tb_temp_pc_master')
    ins.insert(loc, 'tb_temp_pc_master', 5, pc_dic.values())
    rd.merge(loc, 'tb_master_pc', 'tb_temp_pc_master', 'id')
    dt.drop_tb(loc, 'tb_temp_pc_master')

    ins.insert_ignore_processed(loc, ls)
    up.update_processed(loc, ls, 'master_pc', 1)

    pc_dic = {}
