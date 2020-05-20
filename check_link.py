#!/usr/bin/env python3

import csv
import re
import subprocess

#Check link with COVID-19 active people

#Make sure that you have earlier declared the MAC Addresses of COVID-19 active people in covid_active.txt

contact_count = 0

with open("active_mac_addresses.txt") as file1:
    csv_f1 = csv.reader(file1)
    with open("mac_addresses.txt") as file2:
        csv_f2 = csv.reader(file2)
        for row1 in csv_f1:
            mac1,date1 = row1
            for row2 in csv_f2:
                mac2,date2 = row2
                if mac1 == mac2:
                    print("ALERT! You have came into contact with {}  on {} who have been declared active on {}".format(mac1,date2,date1))
                    contact_count = contact_count+1

if contact_count == 0:
    print()
    print("You haven't came into contact with any of the COVID-19 active persons in our database")
    print()
if contact_count > 0:
    print()
    print("ALERT. You have came into contact with COVID-19 active persons {} times.".format(contact_count))
    print("ALERT : Immediately contact COVID-19 help centres or call 104")
    print("ALERT : Get yourself quarantined and ALERT the people you have came into contact since the past 30 days")
    print()

