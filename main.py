import sys
import struct
import os
import binascii

sys.path.append("src")

testfile = 'test.mp3'

framesyncmask = 0x07FF
framesyncshift = 21
versionmask =  0x03
versionshift = 19

layermask = 0x03
layershift = 17

protectedmask = 0x01
protectedshift = 16

bitratemask = 0x07
bitrateshift = 12

sampleratemask = 0x03
samplerateshift = 10

paddingmask = 0x01
paddingshift = 9

channelmodemask = 0x03
channelmodeshift = 6

with open(testfile, 'rb') as imagefile:
    frameheader, = struct.unpack('>I', imagefile.read(4))


    print  '{0:011b}'.format((frameheader >> framesyncshift) & framesyncmask)
    print  '{0:02b}'.format((frameheader >> versionshift) & versionmask)

    print  '{0:02b}'.format((frameheader >> layershift) & layermask)

    print  '{0:01b}'.format((frameheader >> protectedshift) & protectedmask)

    print  '{0:04b}'.format((frameheader >> bitrateshift) & bitratemask)

    print  '{0:02b}'.format((frameheader >> samplerateshift) & sampleratemask)

    print  '{0:01b}'.format((frameheader >> paddingshift) & paddingmask)

    print  '{0:02b}'.format((frameheader >> channelmodeshift) & channelmodemask)