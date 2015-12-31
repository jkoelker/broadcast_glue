# -*- coding: utf-8 -*-

import argparse

from . import glue


def main():
    description = 'Glue In-Home Streaming discovery broadcasts between subnets'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('interfaces', metavar='INTF', nargs='+',
                        help='Interfaces to bridge')
    parser.add_argument('-p', '--port', type=int, default=27036,
                        help='Port to listen/broadcast')
    parser.add_argument('--peer', action='append',
                        help='IP address of peer to ALWAYS replicate to')

    args = parser.parse_args()
    g = glue.Glue(interfaces=args.interfaces, port=args.port, peers=args.peer)
    g.serve_forever()


if __name__ == '__main__':
    main()
