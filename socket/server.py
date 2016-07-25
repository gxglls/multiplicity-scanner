import sys
sys.path.append('../arp')
import Tools,socket,threading,signal,os
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket create"
print Tools.get_IP()
server.bind((Tools.get_IP(),8000))
print "socket bind"
server.listen(5)
print "socket listen"

def connet_handle(conn):
	while 1:
		date=conn.recv(1024)
		print date
def ctrl_c_handle(a,b):
	global server
	server.close()
	print "bye"
	os._exit(0)

signal.signal(signal.SIGINT,ctrl_c_handle)

while 1:
	conn,conn_ip=server.accept()
	print conn_ip," ","connect!"
	t=threading.Thread(target=connet_handle,args=(conn,))
	t.start()


