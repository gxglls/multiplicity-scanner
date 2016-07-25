import sys
sys.path.append('../arp')
import Tools,socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket create"

server.connect((Tools.get_IP(),8000))
print "socket connect"
while 1:
	a=raw_input("what you what set?")

	server.send(a)
