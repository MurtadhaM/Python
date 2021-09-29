#!/usr/bin/python
# Author Murtadha Marzouq Type 3 Script (There are 3 levels in Mininet)
# This is the Second senario
from mininet.log import info
from mininet.topo import Topo

class MyTopo( Topo ):

    def build( self ):
        "Murtadha's Awesome Typo"
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s15 = self.addSwitch('s15')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s14 = self.addSwitch('s14')

        info('Add hosts\n')
        h10 = self.addHost('h10', cls=Host, ip='10.0.2.1/24', defaultRoute='h10-eth0')
        h3 = self.addHost('h3', cls=Host, ip='10.0.1.12', defaultRoute='via 10.0.1.1')
        h2 = self.addHost('h2', cls=Host, ip='10.0.1.11/24', defaultRoute='via 10.0.1.1')
        h9 = self.addHost('h9', cls=Host, ip='10.0.1.1/24', defaultRoute='via h9-eth0')
        h4 = self.addHost('h4', cls=Host, ip='10.0.1.13/24', defaultRoute='via 10.0.1.1')
        h7 = self.addHost('h7', cls=Host, ip='10.0.2.12/24', defaultRoute='via 10.0.2.1')
        h8 = self.addHost('h8', cls=Host, ip='10.0.2.13/24', defaultRoute='via 10.0.2.1')
        h6 = self.addHost('h6', cls=Host, ip='10.0.2.11/24', defaultRoute='via 10.0.2.1')
        h1 = self.addHost('h1', cls=Host, ip='10.0.1.10/24', defaultRoute='via 10.0.1.1')
        h5 = self.addHost('h5', cls=Host, ip='10.0.2.10/24', defaultRoute='via 10.0.2.1')

        info('Link them UP\n')
        self.addLink(h1, s11)
        self.addLink(h2, s11)
        self.addLink(h4, s12)
        self.addLink(h3, s12)
        self.addLink(h7, s15)
        self.addLink(h5, s14)
        self.addLink(h9, s9)
        self.addLink(h10, s9)
        self.addLink(s15, s13)
        # Second Senario
        self.addLink(s14, s13, bw=20, delay='5ms')
        # Second Senario
        self.addLink(s13, s9, bw=20)
        self.addLink(s12, s10)
        self.addLink(s11, s10)
        self.addLink(s10, s9)
        self.addLink(h8, s15)
        self.addLink(h6, s14)
        # TO ALLOW FORWARDING WITHOUT MESSING WITH THE OPENVSWITCH CONTROLLER
        h9.cmd('sysctl net.ipv4.ip_forward=1')
        # ENABLE FORWARDING
        h10.cmd('sysctl net.ipv4.ip_forward=1')
        h10.cmd('route add -net 10.0.1.0/24   h10-eth0')
        s9.cmd('sysctl net.ipv4.ip_forward=1')
        h9.cmd('route add -net 10.0.2.0/24   h9-eth0')

topos = { 'mytopo': ( lambda: MyTopo() ) }