#!/usr/bin/python3
# Parses AdBlock/uBlockOrigin filters into /etc/hosts entries  

import sys
import re
import urllib.request
import subprocess

file = open("/var/www/html/conf/autoDNS.txt", "w")
filter = urllib.request.urlopen("https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt")

cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True)

for line in filter:
    line = line.decode("utf-8")
    if not line.startswith("!"): # ignore comments
        match = False
        m = re.search("([A-Za-z0-9]+?([A-Za-z0-9_\-]*?[A-Za-z0-9]+?)*\.)+?[A-Za-z0-9]{2,}", line) # is there a domain name?¨
        if not m == None:
            m = re.match("^\|\|(.+?)\^(\$[a-zA-Z0-9\-]+?)?$", line)
            if not m == None:
                file.write(IP.decode("utf-8").rstrip() + " " + m.group(1) + "\n")

