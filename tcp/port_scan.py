#!/usr/bin/python2.7
# -*- coding=utf-8 -*-
import sys
sys.path.append('../arp')
import Tools,getopt,re
from scapy.all import *
def syn_scan_final(hostname,lport,hport):
	result_raw = sr(IP(dst=hostname)/TCP(dport=(lport,hport),flags="S"), verbose = False)
	result_list = result_raw[0].res
	for i in range(len(result_list)):
		tcpfields = result_list[i][1][1].fields
		if tcpfields['flags'] == 18:
			print('端口号: ' + str(tcpfields['sport']) + '  is Open!!!')



if __name__ == '__main__':
	targetIP=None
	minport=None
	maxport=None
	try:
		opts,argvs=getopt.getopt(sys.argv[1:],'t:l:h:',["help"])
	except:
		print "argv error!"
	for o,v in opts:
		if o=='-t':
			targetIP=v
		if o=='-l':
			minport=int(v)
		if o=='-h':
			maxport=int(v)
	syn_scan_final(targetIP,minport,maxport)
