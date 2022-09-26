import xml.etree.ElementTree as ET

tree = ET.parse('temp.xml')
root = tree.getroot()
new_root_element = ET.Element('root')
root_element_tag = root.tag
i = 1
# for transact in root.findall('.//note'):
for transact in root.iter('body'):
    sub_element = ET.SubElement(new_root_element, root_element_tag, root.attrib)
    sub_element.append(transact)
    f = open(f'out_{i}.txt', 'wb')
    f.write(ET.tostring(sub_element))
    # sub_element.clear()
    f.close()
    i += 1



