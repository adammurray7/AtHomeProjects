#Import systems used for handling exceptions
#Import socket which will do all port/internet things for us
#Import date and time to print date and time in banner
import sys
import socket
from datetime import datetime

target = input(str("Target IP: "))


#Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)


#Script to detect all open ports on the server
try:
    #Scan every port on the target ip
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open port
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

#Catching keyboard interrupts
except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()
#Catching socket errors
except socket.error:
    print("\ Host not responding :(")
    sys.exit()
     