#!/usr/bin/env python
from ucsmsdk.ucshandle import UcsHandle
"""
Sample python script for gathering and displaying inventory information
by using class based queries
"""


def main():
    # some housekeeping strings we'll use later
    template = "{0:25} {1:20} {2:15}"
    line = template.format("---------------------", "---------------", "---------")

    # Create a connection to UCSM aka as "handle"
    handle = UcsHandle("192.168.51.134", "ucspe", "ucspe")
    # Login to the server
    handle.login()

    # Gather blade chassis info and display simple table
    chassis = handle.query_classid('equipmentChassis')
    print(template.format("Chassis DN", "Model", "Serial Number"))
    print(line)
    for c in chassis:
        print(template.format(c.dn, c.model, c.serial))

    print("\n")

    # Gather Fabric Interconnect info and display simple table
    fis = handle.query_classid('networkElement')
    print(template.format("Fabric Interconnect DN", "Model", "Serial Number"))
    print(line)
    for fi in fis:
        print(template.format(fi.dn, fi.model, fi.serial))

    print("\n")

    # Gather blade info and display simple table
    blades = handle.query_classid('computeBlade')
    print(template.format("Blade DN", "Model", "Serial Number"))
    print(line)
    for bl in blades:
        print(template.format(bl.dn, bl.model, bl.serial))


if __name__ == '__main__':
    main()
