from scapy.all import *
arpTable={
	'10.10.10.131':'00:0c:29:f1:11:a4',
	'10.10.10.1':'00:50:56:c0:00:08',
	'10.10.10.254':'00:50:56:fb:be:a0',
	'10.10.10.2':'00:50:56:f5:33:5e',
	'10.10.10.128':'00:0c:29:a4:88:bb'
}
def arp_filter(pkt):
	if ARP in pkt and pkt[ARP].op in (1,2) and pkt[ARP].psrc in arpTable.keys():
		if pkt[ARP].hwsrc != arpTable[pkt[ARP].psrc]:
			print '这个arp有毒!'
			print pkt.summary()
sniff(prn=arp_filter,timeout=5)
