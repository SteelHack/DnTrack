#Ja vim ze stredniky tu nepatri, ale mi to dela dobre :D

import os
import time
from stat import * # ST_SIZE etc
import shutil

prevuChan = 0;
prevaChan = 0;

seCounter = 0;

while True:
	#print "DNSmasq conf checker script initiated...";
	seCounter++;
	curruChan = os.stat("/var/www/html/conf/userDNS.txt")[ST_MTIME];
	curraChan = os.stat("/var/www/html/conf/autoDNS.txt")[ST_MTIME];
	if curruChan != prevuChan or curraChan != prevaChan:
		print "Some configuration changed!";
		userDNSs = open("/var/www/html/conf/userDNS.txt", 'r');
		autoDNSs = open("/var/www/html/conf/autoDNS.txt", 'r');
		hostsConf = open("/var/www/html/conf/dnsmasq.hosts", 'w');
		udns = userDNSs.read();
		adns = autoDNSs.read();
		hostsConf.write(udns + "\n\n" + adns);
		userDNSs.close();
		autoDNSs.close();
		hostsConf.close();
		copyfile("/var/www/html/dnsmasq.hosts", "/etc/dnsmasq.hosts");
		os.system("sudo service dnsmasq restart");
		prevuChan = curruChan;
		prevaChan = curraChan;
	if seCounter == 60:
		os.system("parse.py");
	time.sleep(1);
