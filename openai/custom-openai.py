#!/var/ossec/framework/python/bin/python3

import sys
import json
import requests
from requests.exceptions import HTTPError

# Read configuration parameters
alert_file = open(sys.argv[1])
apikey = sys.argv[2]

# Read the alert file
alert_json = json.loads(alert_file.read())
alert_file.close()

# Extract issue fields
full_log = alert_json['full_log']

# Set up the open.ai variables
aiModel = "text-davinci-003"
aikey = "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"
beforePrompt = 'Please explain the following log entry seen on the SIEM: "'
url = 'https://api.openai.com/v1/completions'

qdata = {
            'model': aiModel,
            'prompt': beforePrompt + full_log,
            'max_tokens': 1500,
            'temperature': 0,
            'top_p': 1,
            'presence_penalty': 0,
            'frequency_penalty': 0.5,
            'best_of': 1,
            'n': 1
}

headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + apikey
}

try:
    response = requests.post(url, headers=headers, json=qdata)
    response.raise_for_status()
    jsonResponse = response.json()
    print(jsonResponse["choices"][0]["text"])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

sys.exit(0)
