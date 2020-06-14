import xml.etree.ElementTree as ET
tree = ET.parse('data1.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

#print root tag and dict of attributes
for child in root:
    print(child.tag, child.attrib)

#sum of all gdppc
num_list = list()
for gdppc in root:
    num_list.append(int(gdppc[2].text))
print(sum(num_list))

#.iter() help in iteration over all the sub-tree
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

#get() accesses the attributes of element
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1  
    rank.text = new_rank
    rank.set('updated', 'yes')
    print(rank.text)

#remove countries with rank higher than 50
for country in root.findall('country'):
    rank = country.find('rank').text
    if rank > 50:
        root.remove(country)

#element and subelement function convenient way  to create element and sub-element of tree
ele = ET.Element('a')
ele1 = ET.SubElement(ele, 'b')
ele2 = ET.SubElement(ele, 'c')
ele3 = ET.SubElement(ele2, 'd')
ET.dump(ele)

#Node with name='Singapore' that have a 'year' child
for country in root.findall('country'):
    if country.get('name') == 'Singapore':
        print(country.find('year').text)
