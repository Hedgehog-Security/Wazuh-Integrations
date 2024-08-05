#/usr/bin/env python3

import sys
import requests
import json
from requests.auth import HTTPBasicAuth

"""
ossec.conf configuration structure
 <integration>
     <name>custom-discord</name>
     <hook_url>https://discord.com/api/webhooks/XXXXXXXXXXX</hook_url>
     <alert_format>json</alert_format>
 </integration>
"""

# read configuration
alert_file = sys.argv[1]
user = sys.argv[2].split(":")[0]
hook_url = sys.argv[3]

# read alert file
with open(alert_file) as f:
    alert_json = json.loads(f.read())

# extract alert fields
alert_level = alert_json["rule"]["level"]

if(alert_level >=8 and <= 12):
    # green
    color = "5763719"
elif(alert_level >= 13 and alert_level <= 15):
    # yellow
    color = "15105570a"
elif(alert_level >= 16 and alert_level <= 20):
    # yellow
    color = "15548997"
else:
    # red
    color = "10181046"

# agent details
if "agentless" in alert_json:
          agent_ = "agentless"
else:
    agent_ = alert_json["agent"]["name"]

# combine message details
payload = json.dumps({
    "content": "",
    "embeds": [
        {
            "title": f"SIEM365 Alert: Rule {alert_json['rule']['id']}",
                                "color": color,
                                "description": alert_json["rule"]["description"],
                                "fields": [{
                        "name": "Alert ID",
                        "value": id,
                        "inline": True
                        },
                        {
                                                "name": "Agent",
                                                "value": agent_,
                                                "inline": True
                                                }]
        }
    ]
})

# send message to discord
r = requests.post(hook_url, data=payload, headers={"content-type": "application/json"})
sys.exit(0)
