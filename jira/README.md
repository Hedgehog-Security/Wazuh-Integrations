# JIRA integration script

## By
Author:   Peter Bassill

By:       Hedgehog Security - https://hedgehogsecurity.co.uk/services/managed-wazuh/

Version:  1.2

## Usage
This script is a Wazuh integration script for JIRA.

## Configuration
You will to place both files in your /var/ossec/integrations folder and ensure they are owned by root in group wazuh

`chown root:wazuh /var/ossec/integrations/custom-jir*`

In your /var/ossec/etc/ossec.conf file, you will need to add this integration section:

````
  <!-- JIRA -->
  <integration>
    <name>custom-jira</name>
    <hook_url>https://YOURPREFIX.atlassian.net/rest/api/2/issue/</hook_url>
    <level>12</level>
    <api-key>APIKEY</api-key>
    <alert_format>json</alert_format>
  </integration>
````

You will need to change the HOOK_URL to use your particular hook url. 

Change the level to generate the alert level you want to be raising tickets on.

The APIKEY should be changed to your jira api key.

In /var/ossec/integrations/custom-jira.py, you need to set FOUR variables:

````
# Set the project details
project_alias = 'ALIAS'
issue_name = 'Wazuh Alert'
````

Project Alias should the the alias of your project as you have set in JIRA.
The issue_name can be configured to what ever you want the issue name to be. We use "Wazuh Alert".

````
# Set the project attributes
project_key = 'KEY'
issuetypeid = 'ID'
````

The project key is set within Jira. The Project Key is the prefix of the issue number.  In the example of HEDGEHOG-123, the "HEDGEHOG" portion of the issue number is the Project Key. 
The issuetypeid is set within Jira. You can find the issuetypeid here: https://confluence.atlassian.com/jirakb/how-to-get-issue-id-from-the-jira-user-interface-1115156394.html

## Manual Testing
To manually fire the script, try:

/var/ossec/framework/python/bin/python3 /var/ossec/integrations/custom-jira.py ./test.json USER:JIRA_API JIRA_URL
