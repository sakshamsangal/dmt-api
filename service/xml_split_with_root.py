import glob
import os

import xml.etree.ElementTree as ET


def xml_helper(loc, ct, ls_tag, xml_file_path):
    prod_name = os.path.splitext(os.path.basename(xml_file_path))[0]
    directory = f'{loc}/{ct}/xml/cx_{ct}/{prod_name}'
    os.makedirs(directory, exist_ok=True)

    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    new_root_element = ET.Element('root')
    root_element_tag = root.tag
    for item in ls_tag:
        i = 1
        print(item)
        # for transact in root.findall(f'.//{item}'):
        for chunk in root.iter(item):
            print(21)
            sub_element = ET.SubElement(new_root_element, root_element_tag, root.attrib)
            sub_element.append(chunk)
            fn = f'{directory}/{prod_name}_{item}_{i}.xml'
            print(fn)
            f = open(fn, 'wb')
            f.write(bytearray('<?xml version="1.0" encoding="utf-8" ?>\n', 'utf-8'))
            f.write(ET.tostring(sub_element))
            sub_element.clear()
            f.close()
            i += 1


def get_folder_name(loc, ct):
    ls = []
    for prod_path in sorted(glob.glob(f"{loc}/{ct}/xml/ox_{ct}/*"), key=os.path.getsize):
        ls.append(prod_path.rsplit('\\', 1)[1])
    return ls


def process_xml_chunk_root(loc, ct, ls_tag, all_dir, products):
    if all_dir:
        products = get_folder_name(loc, ct)
    for prod_name in products:
        path_of_xml = f"{loc}/{ct}/xml/ox_{ct}/{prod_name}/*.xml"
        for xml_file in sorted(glob.glob(path_of_xml), key=os.path.getsize):
            xml_helper(loc, ct, ls_tag, xml_file)
