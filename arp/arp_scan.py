#!/usr/bin/python2.7
# -*- coding=utf-8 -*-
import re,scapy,os,getopt,sys
from Tools import *
from scapy.all import *
def arp_scan(localIP,subNet):
	localMac=get_MAC()
	net=subNet.split('.')
	IPList=[]
	for i in range(1,255):
		IPList.append(net[0]+'.'+net[1]+'.'+net[2]+'.'+str(i))
	#result_raw  返回一个元组两个元素,第一个元素是应答数据包，第二个元素是无应答的数据包
	result_raw=srp(Ether(src=localMac,dst='ff:ff:ff:ff:ff:ff')/ARP(op=1,hwsrc=localMac,psrc=localIP,hwdst='00:00:00:00:00:00',pdst=IPList),timeout=1)
	# print result_raw
	#result_raw[0].res 响应的数据包元组对组成的List
	result_list=result_raw[0].res
	# print result_list
	for i in result_list:
		#i 第i对元组(arp请求和arp相应)
		#i[0] 第i对元组的arp请求部分的
		#i[0][1] 第i对元组的arp请求部分的第二层数据(第一层以太，第二层arp)
		#i[0][1].fields 第i对元组的arp请求部分的第二层数据的首部字段和值组成的字典
		#i[0][1].fields['pdst'] 
		print i[0][1].fields['pdst']
		# print i[0][1].fields['pdst']





if __name__ == '__main__':
	localIP=None
	subNet=None
	try:
		opts,argvs=getopt.getopt(sys.argv[1:],"l:s:",["help"])
	except:
		print "argvs error!"
	for o,v in opts:
		if o=="-l":
			localIP=v
		if o =="-s":
			subNet=v
	arp_scan(localIP,subNet)

