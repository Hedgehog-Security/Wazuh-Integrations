# Fortinet integration scripts

## By
Author:   Peter Bassill

By:       Hedgehog Security - https://hedgehogsecurity.co.uk/services/managed-wazuh/

Version:  0.12

## Usage
These active response components and integrations are designed to rely on using the Fortinet firewall to provide temporary blocking of probing IP addresses and permenant blocking of attacking IP addresses.

## Configuration

In your /var/ossec/etc/ossec.conf file, you will need to add this integration section:

````
  <integration>
    <name>custom-fortinet</name>
       ...
  </integration>
````

