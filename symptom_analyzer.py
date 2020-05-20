#!/usr/bin/env python3

import csv
import subprocess
import datetime

subprocess.run(['clear'])

curdate = datetime.date.today()
curdate = str(curdate)

print()
print("Welcome to symptom analyzer")
print("Please give the correct and accurate information to analyze your COVID-19 symptoms")
print("Your response for date " + curdate + " will be recorded for the purpose of tracing")
print()
name = input("Enter your name : ")
age = int(input("Enter your age :  "))
phone = input("Enter your phone number : ")
print("For the following questions respond 'y' for yes and 'n' for no")
print()
cough = input("Are you experiencing Cough or Sore Throat?\n")
fever = input("Are you experiencing Fever?\n")
breath = input("Are you experiencing difficulty in breathing or shortness in breathing?\n")
diarrhoea = input("Are you suffering from Diarrhoea?\n")
chest = input("Are you suffering chestpain or fever?\n")
time = int(input("How long have you been suffering from these symptoms?\nEnter number of days :"))

travel = "Not travelled through COVID-19 active regions since the last 30 days"   #Default travel history
places = "Not travelled through COVID-19 active regions since the last 30 days"
if cough == 'y' or fever == 'y' or breath == 'y' or diarrhoea == 'y' or chest == 'y':
    if time <= 30:
        travel = input("\nHave you travelled through COVID-19 active regions recently.\nEnter 'y' for yes and 'n' for no?\n")
        if travel == 'y':
            places = input("Enter the places you have passed through in the past 30 days :\n")
            print("\nSince you have passed through COVID-19 active regions and also show symptoms of covid 19")
            print("Please get to COVID-19 helpcentres or call 104 and inform about your travel history")
    if not time <= 30:
        print()
        print(name , ", since you show some symptoms of COVID-19, please get yourself home quarantined for atleast 14 days for safety of everyone.")
        print("If the symptoms worsen immediately contact COVID-19 healthcentres or call 104")

if age <= 10 or age >= 60:
    print(name,", please take special attention.\nAttack of the virus on your age can be severe>")

if cough == 'n' and fever == 'n' and breath == 'n' and diarrhoea == 'n' and chest == 'n':
    print()
    print(name , ", your current health status haven't matched any of the COVID-19 symptoms.")
    print("Please don't travel through any of the COVID-19 active regions")
    print("If you suffer from any of the above problems in future or conditions worsen. Please contact COVID-19 healthcentres or call 104")
print()

with open("data.csv","a") as file:
    file.write(curdate+","+name+","+str(age)+","+phone+","+cough+","+fever+","+breath+","+diarrhoea+","+chest+","+str(time)+","+travel+","+places+"\n")
