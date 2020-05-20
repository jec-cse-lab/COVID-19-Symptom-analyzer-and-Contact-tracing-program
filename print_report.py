#!/usr/bin/env python3

import subprocess
import csv

subprocess.run(['clear'])
with open('data.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print()
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("The data was uploaded on date : {}".format(row["curdate"]))
        print("Name : {}",format(row["name"]))
        print("Age : {}",format(row["age"]))
        print("Phone Number : {}".format(row["phone"]))
        if row["cough"] == 'y':
            print("{}, suffering from cough : YES".format(row["name"]))
        if row["cough"] == 'n':
            print("{}, suffering from cough : NO".format(row["name"]))
        if row["fever"] == 'y':
            print("{}, suffering from fever : YES".format(row["name"]))
        if row["fever"] == 'n':
            print("{}, suffering from fever : NO".format(row["name"]))
        if row["breath"] == 'y':
            print("{}, is suffering from breathing problems : YES".format(row["name"]))
        if row["breath"] == 'n':
            print("{}, is suffering from breathing problems : NO".format(row["name"]))
        if row["diarrhoea"] == 'y':
            print("{}, is suffering from diarrhoea : YES".format(row["name"]))
        if row["diarrhoea"] == 'n':
            print("{}, is suffering from diarrhoea : NO".format(row["name"]))
        if row["chest"] == 'y':
            print("{}, is suffering from chest problems : YES".format(row["name"]))
        if row["chest"] == 'n':
            print("{}, is suffering from chest problems : NO".format(row["name"]))
        print("{}, has been suffering from the above symptoms since : {} days".format(row["name"],row["time"]))
        print("Whether travelled through COVID-19 active regions since last 30 days from {} : {}".format(row["curdate"],row["travel"]))
        print("Places travelled through : {}".format(row["places"]))
        print()
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print()
