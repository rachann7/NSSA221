import urllib.request
import os

# testing internet connection to google 
def internet_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

# validating the remote IP address and the gateway 
def validate_ip(ip_address):
    if ip_address.count('.') != 3:  
        return 'Invalid Ip address'  
   
    ip_list = list(map(str, ip_address.split('.')))  
    
    for element in ip_list:  
        if int(element) < 0 or int(element) > 255 or (element[0]=='0' and len(element)!=1):   # check range of each number between periods 
            return 'Invalid IP address'  
   
    return 'Valid IP address'  

# tests
print( "Connected" if internet_connection() else "No internet!" )
print(validate_ip("129.21.3.17"))
print(validate_ip("192.168.1.1"))

# pinging remote ip address, testing connectivity
remote_ip_address = "129.21.3.17" #example
response = os.system("ping -c 4 " + remote_ip_address)

#and then check the response...
if response == 0:
  print(remote_ip_address, 'is up!')
else:
  print(remote_ip_address, 'is down!')

#pinging gateway, testing connectivity
gateway = "192.168.1.1" #example
response = os.system("ping -c 4 " + gateway)

#and then check the response...
if response == 0:
  print(gateway, 'is up!')
else:
  print(gateway, 'is down!')
