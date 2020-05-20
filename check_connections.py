#!/usr/bin/env python3

import csv

with open('mac_addresses.txt') as file:
    csv_f = csv.reader(file)
    for rows in csv_f:
        mac,date = rows
        print("You have came into contact with {} on {}".format(mac,date))
