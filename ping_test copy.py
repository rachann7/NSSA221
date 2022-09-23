#!/usr/bin/python 
# Rachel Leone, September 22nd, 2022

import os 
import urllib.request # imported to used if it can access the internet 
import socket

while True: # while number equals 1-4
    print("Enter Selection:") # user friendly display

    print("         1 - Test connectivity to your gateway.")
    print("         2 - Test for remote connectivity.")
    print("         3 - Test for DNS resolution.")
    print("         4 - Display gateway IP Address.")
    print("         5 - quit program")

    number = input("Enter your choice: ")

    if number == 1:
        gateway = "192.168.1.1" #hard-coded gateway
        response = os.system("ping -c 4" + gateway)

        if response == 0:
            print("Successful")
        else:
            print("Failure")


    if number == 2:
        remote_ip_address = "129.21.3.17" #remote ip address
        response = os.system("ping -c 4" + remote_ip_address)

        if response == 0:
            print("Success")
        else:
            print("Failure")
        

    if number == 3: # DNS resolution, testing internet connection
        def internet_connection(host="http://google.com"):
            try:
                urllib.request.urlopen(host)
                return True
            except:
                return False
        print("Success" if internet_connection() else "Failure")

    if number == 4: # it displays the current gateway ip address
        hostname = socket.gethostname()
        IPaddress = socket.gethostbyname(hostname)
        print(IPaddress)

    if number == 5: #quits the program
        quit()











        
