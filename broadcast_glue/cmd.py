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

    args = parser.parse_args()
    g = glue.Glue(interfaces=args.interfaces, port=args.port)
    g.serve_forever()


if __name__ == '__main__':
    main()
