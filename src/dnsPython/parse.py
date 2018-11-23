# Parses AdBlock/uBlockOrigin filters into /etc/hosts entries  

import sys
import re

file = open("autoDNS.txt", "a")
while True:    
    try:        
        line = input()
        if not line.startswith("!"): # ignore comments
            match = False
            m = re.search("([A-Za-z0-9]+?([A-Za-z0-9_\-]*?[A-Za-z0-9]+?)*\.)+?[A-Za-z0-9]{2,}", line) # is there a domain name?
            if(isinstance(m, re.Match)):
                m = re.match("^\|\|(.+?)\^(\$[a-zA-Z0-9\-]+?)?$", line)
                if(isinstance(m, re.Match)):
                    file.write("127.0.0.1 " + m.group(1) + "\n")
    except EOFError:
        file.close()
        break
