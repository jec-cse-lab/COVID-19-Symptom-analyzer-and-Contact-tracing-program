
Note : Running this script requires root priviledges as some of the scripts in this project works for root users only
Note : This program is designed for UNIX based devices. Running it non-UNIX based Operating System will cause the program to fail creating serious bugs

Use python3 for best experience.
Using python2 will generate errors since some of the libraries and methods used in the program are available in python3 but not in python2

For the purpose of network tracing make sure you have nmap installed in your device.
To install nmap:
sudo apt-get install nmap

Make sure the following packages are already installed on your device:
os
re
sys
subprocess
datetime
csv

Give executable permissions to all the python and bash scripts, using the following commands in this directory:
sudo chmod +x *.py
sudo chmod +x *.sh
