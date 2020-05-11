import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
#root = ET.fromstring(test_data_as_string)
print(root.tag)
print(root.attrib)

for child in root:
       print (child.tag, child.attrib)
print('------------------------')
print(root[2][1].text)

print('----------------------')
print('FIRSTNAME  NUMBER')
for person in root.findall('person'):
    name=person.find('firstname').text
    number=person.find('number').text
    print(name,number)
print('---------------------')
print("All the nicknames:-")

for person in root.findall('person'):
    nick=person.find('nickname').text
    print(nick)