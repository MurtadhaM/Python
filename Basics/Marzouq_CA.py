#!/usr/bin/env python

# AUTHOR MURTADHA MARZOUQ
# THIS IS A HARD ASSIGNMENT BUT I GOT IT AFTER 6 HOURS
"""

"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.log import setLogLevel


class CustomTree(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

        s9 = self.addSwitch('s9', datapath=None, protocols=None)
        s10 = self.addSwitch('s10', datapath=None, protocols=None)
        s11 = self.addSwitch('s11', datapath=None, protocols=None)
        s12 = self.addSwitch('s12', datapath=None, protocols=None)
        s13 = self.addSwitch('s13', datapath=None, protocols=None)
        s14 = self.addSwitch('s14', datapath=None, protocols=None)
        s15 = self.addSwitch('s15', datapath=None, protocols=None)

        # give me some hosts
        h1 = self.addHost('h1', cls=None, ip='10.0.1.10', defaultRoute=None)
        h2 = self.addHost('h2', cls=None, ip='10.0.1.11', defaultRoute=None)
        h3 = self.addHost('h3', cls=None, ip='10.0.1.12', defaultRoute=None)
        h4 = self.addHost('h4', cls=None, ip='10.0.1.13', defaultRoute=None)
        h5 = self.addHost('h5', cls=None, ip='10.0.2.10', defaultRoute=None)
        h6 = self.addHost('h6', cls=None, ip='10.0.2.11', defaultRoute=None)
        h7 = self.addHost('h7', cls=None, ip='10.0.2.12', defaultRoute=None)
        h8 = self.addHost('h8', cls=None, ip='10.0.2.13', defaultRoute=None)
        h9 = self.addHost('h9', cls=None, ip='10.0.1.1', defaultRoute=None)
        h10 = self.addHost('h10', cls=None, ip='10.0.2.1', defaultRoute=None)

        # Merry Fucking Christmas
        self.addLink(h1, s11)
        self.addLink(h2, s11)
        self.addLink(h3, s12)
        self.addLink(h4, s12)
        self.addLink(h5, s14)
        self.addLink(h6, s14)
        self.addLink(h7, s15)
        self.addLink(h8, s15)
        self.addLink(s11, s10)
        # Senario 1
        self.addLink(s12, s10, bw=15, delay='10ms')
        self.addLink(s14, s13)
        self.addLink(s15, s13)
        # Senario 1
        self.addLink(s10, s9, bw=10)
        self.addLink(s13, s9)
        self.addLink(h9, s9)
        self.addLink(h10, s9)


if __name__ == '__main__':
    setLogLevel('info')
    net = Mininet(topo=CustomTree(), build=False)
    c0 = net.addController('c0', controller=None, ip='127.0.0.1', protocol='tcp', port=6644)
    net.start()

       #    dumpNodeConnections(net.hosts)
    #net.pingAll()
    #  iperf :
    #h1, h9 = net.get('h1', 'h9')
    #net.iperf((h1, h9))
    CLI(net)
    net.stop()
topo = { 'one': ( lambda: CustomTree() ) }