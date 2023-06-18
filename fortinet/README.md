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
    <firewall>qqq.rrr.ssss.ttt</firewall>
    <ip>www.xxx.yyy.zzz</ip>
    <time>perm</time>
  </integration>
````

## Notes

To block a probing IP address for 4 hours:

`diagnose user quarantine add src4 xxx.xxx.xxx.xxx 14400 admin` 

To block an attacking IP address for 1 week:

`diagnose user quarantine add src4 xxx.xxx.xxx.xxx 604800 admin` 
