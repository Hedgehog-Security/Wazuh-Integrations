#!/usr/bin/env python

import sys
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import date
today = date.today()

# Set the project details
project_alias = 'ALIAS'
issue_name = 'Wazuh Alert'

# Read configuration parameters
alert_file = open(sys.argv[1])
user = sys.argv[2].split(':')[0]
api_key = sys.argv[2].split(':')[1]
hook_url = sys.argv[3]

# Read the alert file
alert_json = json.loads(alert_file.read())
alert_file.close()

# Extract issue fields
client = alert_json['agent']['labels']['group']
agent_name = alert_json['agent']['name']
agent_ip = alert_json['agent']['ip']
alert_level = alert_json['rule']['level']
description = alert_json['rule']['description']
ruleid = alert_json['rule']['id']
agentid = alert_json['agent']['id']

# Set the project attributes
project_key = 'KEY'
issuetypeid = 'ID'

# Generate request
headers = {'content-type': 'application/json'}
issue_data = {
    "update": {},
    "fields": {
        "summary": 'SIEM alert on ' + agent_name + ' [' + agent_ip + ']',
        "issuetype": {
            "id": issuetypeid
        },
        "project": {
            "key": project_key
        },
        "description": {
            'version': 1,
            'type': 'doc',
            'content':  [
                    {
                      "type": "paragraph",
                      "content": [
                        {
                          "text": 'Ticket generated for ' + client + '\n- State: ' + description + '\n- Rule ID: ' + str(ruleid) + '\n- Alert level: ' + str(alert_level) + '\n- Agent: ' + str(agentid) + ' ' + agent_name + ' ['+ agent_ip +']',
                          "type": "text"
                        }
                      ]
                    }
                  ],
        },
    }
}

# Send the request
print (requests.post(hook_url, data=json.dumps(issue_data), headers=headers, auth=(user, api_key)))
#response = requests.post(hook_url, data=json.dumps(issue_data), headers=headers, auth=(user, api_key))
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) # <--- Uncomment this line for debugging
sys.exit(0)
