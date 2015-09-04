from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Controller
import sys

def mininet_proj():

    "Create a Network and add nodes according..."
    commandargs=(sys.argv)
    hCount=int(commandargs[1])
    sCount=int(commandargs[2])

    print "no of hosts : "+commandargs[1]
    print "no of switches : "+commandargs[2]

    net = Mininet( controller=Controller )

    print('*** Adding Controller *** \n')
    net.addController('c0')

    print( '*** Adding switch ***\n' )
    switches=[]

    for i in range(sCount):
      switches.append(net.addSwitch('s'+str(i+1)))

    print( '*** Adding hosts *** \n' )
    hosts=[]

    for i in range(hCount):
      hosts.append(net.addHost('h'+str(i+1)))


    print( '*** Estabish links ***\n' )

    for si in range(sCount):
     if si+2 < sCount:
        net.addLink(switches[si],switches[si+2])
     if si%2 == 0 :
        net.addLink(hosts[2*si],switches[si])
        net.addLink(hosts[2*si+2],switches[si])
     else:
        net.addLink(hosts[2*si-1],switches[si])
        net.addLink(hosts[2*si+1],switches[si])

    print( '*** Starting network ***\n')
    net.start()

    print( '*** Running CLI ***\n' )
    CLI( net )

    print( '*** Stopping network ***' )
    net.stop()

if __name__ == '__main__':
    mininet_proj()
