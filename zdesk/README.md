# zDesk integration script

## By
Author:   Peter Bassill

By:       Hedgehog Security - https://hedgehogsecurity.co.uk/services/managed-wazuh/

Version:  1.2

## Usage
This script is a Wazuh integration script for zDesk.

## Configuration

In your /var/ossec/etc/ossec.conf file, you will need to add this integration section:

````
  <integration>
    <name>custom-tickets</name>
    <alert_format>json</alert_format>
    <level>12</level>
    <api_key>APIKEY</api_key>
    <url>https://URL</url>
  </integration>
````

