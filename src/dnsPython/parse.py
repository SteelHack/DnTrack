# Parses AdBlock/uBlockOrigin filters into /etc/hosts entries  

import sys
import re
import urllib

file = open("autoDNS.txt", "a")
filter = urllib.request.urlopen("https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt") # it's a file like object and works just like a file
    
for line in filter:
    line = line.decode("utf-8")
    if not line.startswith("!"): # ignore comments
        match = False
        m = re.search("([A-Za-z0-9]+?([A-Za-z0-9_\-]*?[A-Za-z0-9]+?)*\.)+?[A-Za-z0-9]{2,}", line) # is there a domain name?
        if(isinstance(m, re.Match)):
            m = re.match("^\|\|(.+?)\^(\$[a-zA-Z0-9\-]+?)?$", line)
            if(isinstance(m, re.Match)):
                file.write("127.0.0.1 " + m.group(1) + "\n")
