#!/usr/bin/env python3

print("Before entering a zone as COVID-19 please make sure that your information is correct or has been collected from trusted or genuine sources")
choose = input("\nEnter 'y' to input the zone name\nEnter 'n' to ignore and exit\n")

if choose == 'y':
    active_zone = input("Enter the correct zone that is currently active under COVID-19 threat : \n")
    with open('active_zone.txt','a') as file:
        file.write(active_zone+'\n')
        print()
        print("Successfully entered {} in the list of COVID-19 active zones".format(active_zone))
        print()
if choose == 'n':
    print()
    print("Thanks for choosing to verify the information on the region")
    print()

