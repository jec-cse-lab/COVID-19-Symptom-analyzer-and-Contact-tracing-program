#!/usr/bin/env python3

import subprocess
import re
import datetime

curdate = datetime.date.today()
curdate = str(curdate)

subprocess.run(['./get_ip.sh'])

with open('ip_address.txt') as file:
    for line in file:
        result = re.search(r"[0-9\.]*",line)

#Here result[0] stores the ip address in string format

with open('ip_address.txt','w') as file:
    file.write(result[0])

#Obtaining the required ipv4 address for nmap scanning
ip = result[0]
ip = ip.split('.') # To convert the IPv4 in string format into a list of 4 numbers
ip[len(ip)-1] = '1'
ip = '.'.join(ip) #Convert ipv4 in list format into string format

subprocess.run(['./get_mac.sh',ip])

#Now we will filter the mac addresses to a text file
with open('mac_log.txt') as file:
    for line in file:
        result = re.search(r"..\:..\:..\:..\:..\:..",line)
        with open('mac_addresses.txt','a') as f:
                f.write(result[0]+','+curdate+'\n')


    



