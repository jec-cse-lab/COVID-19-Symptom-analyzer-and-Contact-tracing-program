#!/usr/bin/env python3

import csv
import re
import subprocess
import datetime

today = datetime.date.today()
today = str(today)

print("Available MAC addresses and their connection date in our database : ")
with open('mac_addresses.txt') as file:
    csv_f = csv.reader(file)
    for row in csv_f:
        mac_address,current_date = row
        print("You have connected with {} on {}".format(mac_address,current_date))

choice = input("Press 'y' to enter a MAC Address from the current database or from external resources\nPress 'n' to ignore and exit\n")
print()

if choice == 'y':
    mac = input("Enter MAC Addresses : ")
    with open('active_mac_addresses.txt','a') as file:
        file.write(mac+','+today+'\n')
    print("Your response has been successfully recorded")
    print()



