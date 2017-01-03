import xml.etree.ElementTree as ET
from collections import defaultdict


# Open up the XML file that we wish to parse
tree = ET.parse('testdata.xml')
root = tree.getroot()

count = 0
database =[]
# Create a dictionary to keep a running total of all unique items.
d = defaultdict(int)

# Iterate through each iteam that is stored with the tag Device
for elem in root.getiterator(tag='Device'):
    # Store all the data
    SerialNumber =  str(elem.find('SerialNumber').text)
    HostName = str(elem.find('HostName').text)
    Model = str(elem.find('Model').text)
    Version = str(elem.find('Version').text)

    # Increment the counter in the dictionary to store the number of devices
    d[Model] += 1
    key = elem.find('SerialNumber').text
    database.append((key,elem))

    count=count+1



# Sort the Database according to the device model number
database.sort()

#Optional Code to print out each element
#for elem in database:

#    SerialNumber = str(elem[1].find('SerialNumber').text)
#    HostName = str(elem[1].find('HostName').text)
#    Model = str(elem[1].find('Model').text)
#    Version = str(elem[1].find('Version').text)

#    print '{0:40} {1:20} {2:20} {3:20}'.format(HostName, SerialNumber, Model, Version)


print '{0:40} {1}'.format("Model Type","Count")
print '{0:40} {1}'.format("========================================","=======")
for info in sorted(d):
    print '{0:40} {1}'.format(info,d[info])
print "\nTotal Device Count: " + str(count)
