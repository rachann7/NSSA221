#!/usr/bin/python3

import socket
import os 
import re
import platform
import psutil
import multiprocessing 
import shutil


def device_information():
    print('\033[92mDevice Information\033[0m')
    print("Hostname         " + re.sub("\..*", "", socket.gethostname()))
    domain = socket.getfqdn()
    res = domain[domain.index('.') + 1:]
    print("Domain           " + res)

def network_information():
    print('\n\033[92mNetwork Information\033[0m')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("IP Address:      " + s.getsockname()[0])
    host_name = socket.getfqdn(socket.gethostname())
    print("Gateway:         " + socket.gethostbyname(host_name))
    print("Network Mask:    ")
    print("DNS1:            ")
    print("DNS2:            ")

def os_information():
    print('\n\033[92mOS Information\033[0m')
    print("Operating System: " + platform.system())
    print("Operating Version: " + platform.version())
    print("Kernel Version: " + platform.release())

def storage_information():
    print('\n\033[92mStorage Information\033[0m')
    path = '/'
    print("Hard Drive Capacity: " + str(shutil.disk_usage(path).total)[:2] + "G")
    print("Availale Space: " + str(shutil.disk_usage(path).free)[:2] + "G")

def processor_information():
    print('\n\033[92mProcessor Information\033[0m')
    print("CPU Model: " + platform.processor())
    print("Numer of processors: " + str(multiprocessing.cpu_count()))
    print("Number of cores: " + str(psutil.cpu_count()))

def memory_information():
    print('\n\033[92mMemory Information\033[0m')
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf("SC_PHYS_PAGES")
    mem_gib = mem_bytes/(1024.**3)
    print("Total RAM: " + "{:.1f}".format(mem_gib) +"Gi")
    print("Available RAM: " + str(psutil.virtual_memory().available)[:2] + "Gi")
    
def main():
    device_information()
    network_information()
    os_information()
    storage_information()
    processor_information()
    memory_information()

if __name__ == "__main__":
    main()