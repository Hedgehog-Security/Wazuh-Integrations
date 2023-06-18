#!/var/ossec/framework/python/bin/python3
# custom-foritnet.py
# by Peter Bassill (@peterbassill)
# Hedgehog Security (https://hedgehogsecurity.co.uk/services/managed-wazuh/)

# IMPORTANT - ALPHA RELEASE - NOT PRODUCTIONISED!

import sys
import subprocess

firewall = sys.argv[1]
ip = sys.argv[2]
time = sys.argv[3]
if time == temp:
  duration = 14400
else:
  duration = 604800 
  
subprocess.run(("ssh", "wazuh@" + firewall, "diagnose user quarantine add src4 " + ip + duration + " admin"))

sys.exit(0)
