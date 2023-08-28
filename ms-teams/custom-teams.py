#!/var/ossec/framework/python/bin/python3

# ----------------------------------------------------
# custom-teams.py - a Wazuh Integration for MS Teams
#
# Version:  1.0
# Date:     24/08/2023
# Author:   Peter Bassill

import sys
import json
import requests
from datetime import date
today = date.today()

# Read configuration parameters
client = ''
alert_file = open(sys.argv[1])
# webhook_url = sys.argv[2]
webhook_url='https://xxxx.webhook.office.com/webhookb2/xxxx'

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

alert_level = int(alert_json['rule']['level'])
description = str(alert_json['rule']['description'])
ruleid = str(alert_json['rule']['id'])
full_log = alert_json['full_log']

alert_text = f'ALERT GENERATED - please review the alert and any associated tickets... \n- Rule ID: ' + ruleid + '\n- Alert level: ' + str(alert_level) + '\n- Agent: ' + agentid + ' ' + agent_name + ' ['+ agent_ip +'] \n- State: ' + description + '\n- Log Data: ' + full_log

alert_data = {
        'text': alert_text
        }

json_alert = json.dumps(alert_data)

# ------------------------------------------------------------------------------------------------

def post_to_teams_webhook(webhook_url):
    try:

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(webhook_url, data=json_alert, headers=headers)

        if response.status_code == 200:
            print("Data posted successfully to Teams.")
        else:
            print("Failed to post data to Teams. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    post_to_teams_webhook(webhook_url)


sys.exit(0)
