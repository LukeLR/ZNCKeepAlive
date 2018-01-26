# ZNCKeepAlive
*A keep alive module for the znc bouncer*

## The Problem
Unfortunately, not all IRC networks get as much traffic nowadays as a few years ago. When bouncers are connected to such IRC networks, very few traffic passes the TCP connections of the bouncer to the network. While usually not being a problem, bouncers that are behind a NAT or firewall are disconnected from the network after some idle time. Why? Because the NAT / Firewall closes the connection.

## The Solution
This module wants to solve that issue by regularily sending `/ping` commands to the network. Therefore, packets pass the NAT every 5 minutes, and the socket is kept alive. Hence the name :)

## Keep using IRC, it's great!
