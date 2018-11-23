#Ja vim ze stredniky tu nepatri, ale mi to dela dobre :D

import os
import time
from stat import * # ST_SIZE etc
import shutil

prevChan = 0;

while True:
	#print "DNSmasq conf checker script initiated...";
	currChan = os.stat("/var/www/html/dnsmasq.conf")[ST_MTIME];
	if currChan != prevChan:
		print "DEBUG: dnsmasq config file changed!";
		#copyfile('/var/www/html/dnsmasq.conf', '/etc/dnsmasq.conf');
		prevChan = currChan;
	else:
		print "..";
	time.sleep(1);
