# MakerSpaceScanner

This software is written to be run for the Colorado School of Mines Maker Society
in Brown Hall as a system to lock 3D printers to require students to scan their
Blaster Cards in order to register themselves with a 3D printer in order to print

This is meant to be run off of a Raspberry Pi hooked up to an HDMI monitor
with main.py running in terminal using a USB magnetic strip card reader.

Each of the electromagnetic locks are running off 12V DC running through a
general purpose relay with the relay hooked up to GPIO pins on the RPi, these
pins will be labeled later below.
