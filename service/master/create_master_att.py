from lxml import etree

from dao import create as cr
from dao import delete as dt
from dao import insert as ins
from dao import read as rd
from dao import update as up
from service.master import create_master as cm

ct = ''
att_dic = {}
file_name = ''
prod_name = ''
file_size = ''


def xml_traverse_att(root):
    tag_name = etree.QName(root).localname
    for key, val in root.attrib.items():
        key = etree.QName(key).localname
        my_id = f'{tag_name}_{key}'
        if my_id not in att_dic:
            att_dic[my_id] = (my_id, tag_name, key, val, file_name, prod_name, ct)

    for child in root:
        if type(child) == etree._Element:
            xml_traverse_att(child)


def process_master_att(loc, content_type, all_dir, products):
    global att_dic, file_name, prod_name, ct
    ct = content_type

    ls = []
    for root, f_name, p_name, f_size in cm.get_xml_root(loc, content_type, all_dir, products):
        file_name = f_name
        prod_name = p_name
        xml_traverse_att(root)
        ls.append((prod_name, ct))

    cr.create_tb_master_att(loc, 'tb_temp_att_master')
    ins.insert(loc, 'tb_temp_att_master', 7, att_dic.values())
    rd.merge(loc, 'tb_master_att', 'tb_temp_att_master', 'id')
    dt.drop_tb(loc, 'tb_temp_att_master')

    ins.insert_ignore_processed(loc, ls)
    up.update_processed(loc, ls, 'master_att', 1)

    att_dic = {}
