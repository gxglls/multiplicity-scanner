#!/usr/bin/python2.7
#conding:utf-8
import re,os
from scapy.all import *
def get_MAC():
	ipconfig=os.popen('ifconfig').read()
	result_raw=re.findall(".{2}:.{2}:.{2}:.{2}:.{2}:.{2}",ipconfig)	
	return result_raw[0]

def get_IP():
	ipconfig=os.popen('ifconfig').read()
	result_raw=re.findall("\d{1,3}\..{1,3}\..{1,3}\..{1,3}",ipconfig)
	return result_raw[0]

def IP_to_MAC(IPadd):
	result=srp(Ether()/ARP(op=1,hwsrc=get_MAC(),psrc=get_IP,hwdst='00:00:00:00:00:00',pdst=IPadd))
	#return (result[0].res)[1][ARP].hwsrc
	return (result[0].res)[0][1][ARP].hwsrc

if __name__ == '__main__':
	print IP_to_MAC('10.10.10.2')
	print "Mac address is",get_MAC()
	print "IP address is",get_IP()