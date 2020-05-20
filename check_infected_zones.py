#!/usr/bin/env python3

print()
print("Following list is only based on the data input on our server.\nFor the latest updates by the government source, please go through the url : www.coronatracker.com\n")
print("The list of infected zones are : ")
with open('active_zone.txt') as file:
    print(file.read().strip())
print()

