# JIRA integration script

## By
Author:   Peter Bassill

By:       Hedgehog Security - https://hedgehogsecurity.co.uk/services/managed-wazuh/

Version:  1.2

## Usage
This script is a Wazuh integration script for JIRA.

## Configuration

In your /var/ossec/etc/ossec.conf file, you will need to add this integration section:

````
  <!-- JIRA -->
  <integration>
    <name>custom-jira</name>
    <hook_url>https://hedgehogsec.atlassian.net/rest/api/2/issue/</hook_url>
    <level>12</level>
    <api-key>APIKEY</api-key>
    <alert_format>json</alert_format>
  </integration>

````

