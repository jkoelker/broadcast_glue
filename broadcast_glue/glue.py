# -*- coding: utf-8 -*-

import netaddr
import netifaces

from gevent import server
from gevent import socket


class Glue(server.DatagramServer):
    def __init__(selfie, interfaces, port):
        super(Glue, selfie).__init__(':%s' % port)

        interfaces = [i for i in netifaces.interfaces() if i in interfaces]

        selfie._addr_map = []
        for interface in interfaces:
            for addr in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                net = '%s/%s' % (addr['addr'], addr['netmask'])
                net = netaddr.IPNetwork(net)
                broadcast = addr.get('boadcast')

                if broadcast:
                    selfie._addr_map.append((net, broadcast))

        selfie._send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def handle(selfie, data, address):
        host = netaddr.IPAddress(address[0])
        port = address[1]

        for net, broadcast in selfie._addr_map:
            if host in net:
                continue

            selfie._send_socket.sendto(data, (broadcast, port))
