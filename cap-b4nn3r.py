# -*- coding: utf-8 -*-

import socket
import sys
import time 

if( len(sys.argv) < 2 ):
	print '+ capture banner +\nExample: python {} <host>\n'.format(sys.argv[0])
	sys.exit()

host = sys.argv[1]
inicio = 0
fim = 65535

print '\n++ captuting banners ++\n'
while( inicio < fim ):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.05)
		s.connect((host, inicio))
		r = s.recv(1024)
		
		if r:
			print '{}/tcp\n|_banner: {}\n'.format(inicio, r)

		else:
			print '{}/tcp\n|_banner: (acess danied)\n'.format(inicio)
		
		inicio += 1
		s.shutdown

	except socket.error:
		inicio += 1
