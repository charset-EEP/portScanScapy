#!/usr/bin/python3

import sys
from scapy.all import *

conf.verb=0
print("Enviado um pacote para",sys.argv[1])
#dors to tcp ping (-sS in nmap)
ports=[21,22,23,25,80,443]
pIP=IP(dst=sys.argv[1])
pTCP=TCP(dport=ports,flags="S")
pkg=pIP/pTCP
resp,noresp=sr(pkg)
#print(resp[0][0][TCP].sport)  0=envio 1=resposta
for resposta in resp:
    porta=resposta[1][TCP].sport
    flag = resposta[1][TCP].flags
    print("%d %s" %(porta,flag) )
