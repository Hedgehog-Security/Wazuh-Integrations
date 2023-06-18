# OpenAI integration script

## By
Author:   Peter Bassill

By:       Hedgehog Security - https://hedgehogsecurity.co.uk/services/managed-wazuh/

Version:  1.1

## Usage
This script is meant as an example on how to improve the data being passed on tickets. It is more of an ideas starting point. We use this script within our ticket script to provide initial log data analysis for triage.

## Configuration

In your /var/ossec/etc/ossec.conf file, you will need to add these values into the integration section that you are utilising:

````
  <aiurl>https://api.openai.com/v1/completions</aiurl>
  <openapi_key>YOUR-OPEN-AI-KEY</openapi_key>
````

