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

# Check if agent key exists and extract the data
if "agent" in alert_json:
    if "name" in alert_json['agent']:
        agent_name = str(alert_json['agent']['name'])
    else:
        agent_name = "Agent name is unknown"
    if "ip" in alert_json['agent']:
        agent_ip = str(alert_json['agent']['ip'])
    else:
        agent_ip = "Agent IP is unknown"
    if "id" in alert_json['agent']:
        agentid = str(alert_json['agent']['id'])
    else:
        agentid = "AgentID is unknown"
    if "labels" in alert_json['agent']:
        client = str(alert_json['agent']['labels'])
    else:
        client = "Unknown"
else:
    agent_name = "syslog"
    agent_ip = "Agent IP is unknown"
    agentid = "AgentID is unknown"
    client = "Unknown"


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
        'assign': str(assign),
        'priority': priority,
        'subject': f'Wazuh raised alert on ' + agent_name + ' [' + agent_ip + ']',
        'description': f'Ticket generated for ' + client + '\n- Rule ID: ' + ruleid + '\n- Alert level: ' + str(alert_level) + '\n- Agent: ' + agentid + ' ' + agent_name + ' ['+ agent_ip +'] \n- State: ' + description + '\n- Log Data: ' + full_log
        }


server = requests.post(url, data=form_data)
output = server.text

print('The response from the server is:\n', output)
print(form_data['description'])
sys.exit(0)
