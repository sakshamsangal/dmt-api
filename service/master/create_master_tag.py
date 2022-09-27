import re

from lxml import etree

from dao import create as cr
from dao import delete as dt
from dao import insert as ins
from dao import read as rd
from dao import update as up
from service.master import create_master as cm

ct = ''
parent_dic = {}
temp = {}
tag_dic = {}
tag_ct = []
file_name = ''
prod_name = ''
file_size = ''
has_text_tag = set()


def xml_traverse(parent, root):
    tag_name = etree.QName(root).localname
    if tag_name not in tag_dic:
        tag_dic[tag_name] = (tag_name, 'yes', file_name, prod_name, ct, file_size, 'no')
        tag_ct.append((ct + '_' + tag_name, tag_name, 'skip', ct))

    parent_dic[tag_name] = parent
    pattern = '(\n|\s|\r)*'
    if root.text is not None and not re.fullmatch(pattern, root.text):
        has_text_tag.add((tag_name, ct))

    if root.tail is not None and not re.fullmatch(pattern, root.tail):
        has_text_tag.add((parent_dic[tag_name], ct))

    for child in root:
        if type(child) == etree._Element:
            x = etree.QName(child).localname
            # tag_dic[tag_name]['child'].add(x)

            xml_traverse(tag_name, child)


def add_tag_ct(loc):
    global tag_ct
    ins.insert_ignore(loc, 'tb_tag_ct', 4, tag_ct)
    tag_ct = []


def process_master_tag(loc, content_type, all_dir, products):
    global tag_dic, file_name, prod_name, file_size, ct, temp
    ct = content_type

    ls = []
    for root, f_name, p_name, f_size in cm.get_xml_root(loc, content_type, all_dir, products):
        file_name = f_name
        prod_name = p_name
        file_size = f_size
        xml_traverse('', root)
        ls.append((prod_name, ct))

    cr.create_tb_master_tag(loc, 'tb_temp_tag_map')
    # res = df.to_records(index=False).tolist()
    ins.insert(loc, 'tb_temp_tag_map', 7, tag_dic.values())
    rd.merge(loc, 'tb_master_tag', 'tb_temp_tag_map', 'tag')
    dt.drop_tb(loc, 'tb_temp_tag_map')

    ins.insert_ignore_processed(loc, ls)
    up.update_processed(loc, ls, 'master_tag', 1)

    add_tag_ct(loc)
    print(has_text_tag)
    up.update_has_text_tag(loc, list(has_text_tag))
    up.update_has_text_tag_tag_master(loc, list(has_text_tag))

    tag_dic = {}

