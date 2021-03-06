# -*- encoding: iso-8859-1 -*-

# pH @ LNA 06/04/2007

import struct
import socket
import select
import time
import array
import os

class Packet (object):

    """Packet.

    Packet represents the basic unit of communication between client and server. Each packet
    has a length (in bytes) and an identification number.

    Currently there are fourk kind of packets: Command, Data, Ack and Image.

    Packets have two representations: binary and python object. The python object representation is what you manipulates using
    this object. The binary one represents what the server expect to receive (this is mandated by SI's implementation, so don't care about it).

    The binary representation uses Python's struct module to fo back and forth from binary to object representations. Pckets have
    two method to do this transformation: fromStruct and toStruct. Command packets have a toStruct method, since server doesn�t
    return Command packets, we have to build them. Data, Ack and Image have fromStruct method since we only receive them, server generates them.

    Note: cam_id is unknow by now, and is always set to 1
    """

    def __init__ (self):

        # private
        self.id = 0
        self.cam_id = 1

        self._fmt = ">IBB"

    def fromStruct (self, data):

        results = struct.unpack (self._fmt, data)

        self.length = results[0]
        self.id = results[1]
        self.cam_id = results[2]

        return True

    def __len__ (self):
        return struct.calcsize (self._fmt)
