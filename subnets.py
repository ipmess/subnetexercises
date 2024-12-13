#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:18:56 2019

@author: Angelos Vassiliou
"""

import random
import ipaddress

b1=random.randrange(1,223)
while b1 == 127:
  b1=random.randrange(1,223)
  
b2=random.randrange(0,255)
while (b1 == 169) and (b2 == 254):
  b2=random.randrange(0,255)

b3=random.randrange(0,255)
b4=random.randrange(0,255)
prefixlength=random.randrange(16,30)
print("IP address:" + str(b1) + "." + str(b2)+ "." + str(b3)+ "." + str(b4)+ "/" + str(prefixlength))

interfc = ipaddress.ip_interface(str(b1) + "." + str(b2)+ "." + str(b3)+ "." + str(b4)+ "/" + str(prefixlength))
all_hosts=list(interfc.network.hosts())

print("Mask: " + str(interfc.netmask))
print("Network: " + str(interfc.network.network_address))
print("First host: " + str(all_hosts[0]))
print("Last host: " + str(all_hosts[-1]))
print("Broadcast Address: " + str(interfc.network.broadcast_address))
print("Total number of valid IP addresses: " + str(interfc.network.num_addresses))
print("Total number of valid host IP addresses: " + str(interfc.network.num_addresses-2))
print("======================\n")