#!/usr/local/bin/python2.7

from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct
import time
from datetime import datetime

def getNTPTime(host = "pool.ntp.org"):
    port = 123
    buf = 1024
    address = (host, port)
    msg = '\x1b' + 47 * '\0'

    # reference time (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800L # 1970-01-01 00:00:00

    # connect to server
    client = socket.socket(AF_INET, SOCK_DGRAM)
    client.sendto(msg, address)
    msg, address = client.recvfrom(buf)

    t = struct.unpack("!12I", msg)[10]
    t -= TIME1970
    return datetime.utcfromtimestamp(t).isoformat()

if __name__ == "__main__":
    try:
        host = "pool.ntp.org"
        if len(sys.argv) > 1:
            host = sys.argv[1]

        print "Time on %s is %s" % (host, getNTPTime(host))

    except SystemExit:
        print "Exception::systemExit"

