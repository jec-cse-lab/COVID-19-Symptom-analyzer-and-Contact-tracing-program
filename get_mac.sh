#!/bin/bash

nmap -sn $1/24 | grep MAC >> mac_log.txt

