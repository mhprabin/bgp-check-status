import re

with open('bgp_sum') as device_info:
    for lines in device_info:
        this_dev1 = re.sub(' +', ' ',lines)
        #print (this_dev1)
        this_dev = this_dev1.strip().split(' ')
        device_info ={}
        device_info['Neighbor'] = this_dev[0]
        device_info['State'] = this_dev[8]
        #print (this_dev)
        if this_dev[8] == 'Active': # we can add multiple statement here. for testing only i'm using 'Active'
            print ('BGP neighbor ' + device_info['Neighbor'] + ' is down')
