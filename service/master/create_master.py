import glob
import os

from lxml import etree


def get_folder_name(loc, ct):
    ls = []
    for prod_path in sorted(glob.glob(f"{loc}/{ct}/xml/ox_{ct}/*"), key=os.path.getsize):
        ls.append(prod_path.rsplit('\\', 1)[1])
    return ls


def get_xml_root(loc, ct, all_dir, products):
    if all_dir:
        products = get_folder_name(loc, ct)
    for prod_name in products:
        # x = rd.check_if_record_exist(loc, prod_name)
        # if x[0] != 1:
        if True:
            path_of_xml = f"{loc}/{ct}/xml/ox_{ct}/{prod_name}/*.xml"
            for xml_file in sorted(glob.glob(path_of_xml), key=os.path.getsize):
                print(path_of_xml)
                file_name = os.path.basename(xml_file)
                file_size = round(os.stat(xml_file).st_size / 1024, 2)
                parser = etree.XMLParser(recover=True)
                tree = etree.parse(xml_file, parser)
                yield tree.getroot(), file_name, prod_name, file_size

            # ls.append((prod_name, ct))
    # ins.insert_prod_proc(loc, ls)
    # up.update_processed_prod(loc, ls, master_type)


if __name__ == '__main__':
    loc = 'C:\\Users\\saksangal\\Pictures\\saksham'
    ct = 'deskbook'
    for a, b, c, d in get_xml_root(loc, ct, True, []):
        print(a, b, c, d)
