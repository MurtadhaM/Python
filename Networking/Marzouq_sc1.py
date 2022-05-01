#!/usr/bin/python
# Author Murtadha Marzouq Type 2 Script (There are 3 levels in Mininet)
# This is the First senario

from mininet.cli import CLI
from mininet.log import info
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import Host, RemoteController
from mininet.node import OVSController


def myNetwork():
    net = Mininet(controller=lambda name: RemoteController(name), listenPort=6633)

    net = Mininet()
    info('Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=OVSController,
                           protocol='tcp',
                           port=6653)

    info('Add switches\n')
    s12 = net.addSwitch('s12')
    s13 = net.addSwitch('s13')
    s15 = net.addSwitch('s15')
    s9 = net.addSwitch('s9')
    s10 = net.addSwitch('s10')
    s11 = net.addSwitch('s11')
    s14 = net.addSwitch('s14')

    info('Add hosts\n')
    h10 = net.addHost('h10', cls=Host, ip='10.0.2.1/24', defaultRoute='h10-eth0')
    h3 = net.addHost('h3', cls=Host, ip='10.0.1.12', defaultRoute='via 10.0.1.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.1.11/24', defaultRoute='via 10.0.1.1')
    h9 = net.addHost('h9', cls=Host, ip='10.0.1.1/24', defaultRoute='via h9-eth0')
    h4 = net.addHost('h4', cls=Host, ip='10.0.1.13/24', defaultRoute='via 10.0.1.1')
    h7 = net.addHost('h7', cls=Host, ip='10.0.2.12/24', defaultRoute='via 10.0.2.1')
    h8 = net.addHost('h8', cls=Host, ip='10.0.2.13/24', defaultRoute='via 10.0.2.1')
    h6 = net.addHost('h6', cls=Host, ip='10.0.2.11/24', defaultRoute='via 10.0.2.1')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.10/24', defaultRoute='via 10.0.1.1')
    h5 = net.addHost('h5', cls=Host, ip='10.0.2.10/24', defaultRoute='via 10.0.2.1')

    info('Link them UP\n')
    net.addLink(h1, s11)
    net.addLink(h2, s11)
    net.addLink(h4, s12)
    net.addLink(h3, s12)
    net.addLink(h7, s15)
    net.addLink(h5, s14)
    net.addLink(h9, s9)
    net.addLink(h10, s9)
    net.addLink(s15, s13)
    net.addLink(s14, s13)
    net.addLink(s13, s9)
    # First Senario
    net.addLink(s12, s10, bw=15, delay='10ms')
    net.addLink(s11, s10)
    # First Senario
    net.addLink(s10, s9, bw=10)
    net.addLink(h8, s15)
    net.addLink(h6, s14)
    info('Let us start the Show\n')
    net.build()
    info('Get a Controller to Command The Switches\n')
    for controller in net.controllers:
        controller.start()
    info('Get The Useless Switches Going\n')
    net.get('s12').start([c0])
    net.get('s13').start([c0])
    net.get('s15').start([c0])
    net.get('s9').start([c0])
    net.get('s10').start([c0])
    net.get('s11').start([c0])
    net.get('s14').start([c0])
    # TO ALLOW FORWARDING WITHOUT MESSING WITH THE OPENVSWITCH CONTROLLER
    h9.cmd('sysctl net.ipv4.ip_forward=1')
    # ENABLE FORWARDING
    h10.cmd('sysctl net.ipv4.ip_forward=1')
    h10.cmd('route add -net 10.0.1.0/24   h10-eth0')
    s9.cmd('sysctl net.ipv4.ip_forward=1')
    h9.cmd('route add -net 10.0.2.0/24   h9-eth0')
    info('*** Post configure nodes\n')
    CLI(net)
    net.stop()

# For running Directly
if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
# For the --topo parameter in mn --custom file.py --topo one
TOPOS = {'one': (lambda: myNetwork())}
