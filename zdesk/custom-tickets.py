#!/var/ossec/framework/python/bin/python3

import sys
import json
import requests
from datetime import date
today = date.today()

# Read configuration parameters
alert_file = open(sys.argv[1])
api_key = sys.argv[2]
url = sys.argv[3]
default_assign = sys.argv[4]

# Read the alert file
alert_json = json.loads(alert_file.read())
alert_file.close()

# Extract issue fields

# Check if agent key exists and extract the data
if "agent" in alert_json:
    agent_name = alert_json['agent']['name']
    agent_ip = alert_json['agent']['ip']
    agentid = alert_json['agent']['id']
    if "labels" in alert_json['agent']:
        client = alert_json['agent']['labels']
    else:
        client = "Unknown"
else:
    agent_name = "syslog"
    agent_ip = ""
    agent_id = ""

alert_level = alert_json['rule']['level']
description = alert_json['rule']['description']
ruleid = alert_json['rule']['id']

full_log = alert_json['full_log']

# Set the ticket priority
if alert_level <= 12:
    priority = 'low'
elif alert_level <=17:
    priority = 'medium'
else:
    priority = 'high'

# Send it
form_data = {
        'api': 'v1',
        'app': 'tickets',
        'key': api_key,
        'action': 'newticket',
        'assign': str(default_assign),
        'priority': priority,
        'subject': 'Wazuh raised alert on ' + agent_name + ' [' + str(agent_ip) + ']',
        'description': 'Ticket generated for ' + client + '\n- Rule ID: ' + str(ruleid) + '\n- Alert level: ' + str(alert_level) + '\n- Agent: ' + str(agentid) + ' ' + agent_name + ' ['+ str(agent_ip) +'] \n- State: ' + description + '\n- Log Data: ' + full_log
        }

server = requests.post(url, data=form_data)
output = server.text

print('The response from the server is:\n', output)
print(form_data['description'])
sys.exit(0)
