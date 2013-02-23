netcalc
=======

Netcalc is a tornado application that calculates network information based on user input.  The user can access a form that upon submit provides a table with network information for the IP and subnet mask entered.  This form is available at /netcalc.  

A user can also post JSON to /netcalc/api.  The following is an example payload:

{"ip":"192.168.15.5", "netmask":"255.255.252.0"}

The output for the above request would be:

{"network_id": "192.168.12.0", "net_cidr": "192.168.12.0/22", "network_range": "192.168.12.0-192.168.15.255"}

You can sample the application at:

http://antenesse.net/netcalc
