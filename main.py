#!/usr/bin/env python3

#This program has been developed by :
#Bikash Kalita
#Abhinab Dey
#Rituraj Pathak
#Hudson Vankal

import subprocess
import re
import os
import sys

subprocess.run(['clear'])

run = 'y'

while run == 'y':
    print("WELCOME TO COVID-19 ANALYZER : ")
    print()
    print("1.Symptom Analyzer")
    print("2.Advices by Government of India")
    print("3.Scan your network for people near you")
    print("4.Check link with COVID-19 active people")
    print("5.Check number of connections till now")
    print("6.Check the list of infected zones")
    print("7.Add infected zones")
    print("8.Print report of the user input data")
    print("9.Trace your contacts till now")
    print("10.Add MAC Addresses of infected people")
    print("11.Press 'n' to exit")
    print()

    user_input = input("Please select your operation : \n")

    if user_input == '1':
        subprocess.run(['./symptom_analyzer.py'])
        continue
    if user_input == '2':
        subprocess.run(['./advice.py'])
        continue
    if user_input == '3':
        subprocess.run(['./check_network.py'])
        print("Your connections have been successfully recorded in our database")
        print()
        continue
    if user_input == '4':
        subprocess.run(['./check_link.py'])
        continue
    if user_input == '5':
        subprocess.run(['./check_connections.py'])
        continue
    if user_input == '6':
        subprocess.run(['./check_infected_zones.py'])
        continue
    if user_input == '7':
        subprocess.run(['./add_infected_zones.py'])
        continue
    if user_input == '8':
        subprocess.run(['./print_report.py'])
        continue
    if user_input == '9':
        subprocess.run(['./check_connections.py'])
        continue
    if user_input == '10':
        subprocess.run(['./add_mac.py'])
        continue
    if user_input == 'n' or '11':
        run = 'n'
        print()
        print("Thanks for being with us :)")
        print("STAY SAFE")
        print("STAY HOME")
        print()

