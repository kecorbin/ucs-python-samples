from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan
from ucsmsdk.ucshandle import UcsHandle
"""
Sample python script for adding vlans to ucs domain
"""


def add_vlan(handle, vlan_id, name):
    mo = FabricVlan(parent_mo_or_dn="fabric/lan",
                    sharing="none",
                    name=name, id=vlan_id)
    handle.add_mo(mo)
    return handle.commit()


def main():
    hostname = raw_input("Enter UCSM IP address/hostname: ")
    username = raw_input("Enter username: ")
    password = raw_input("Enter password: ")
    vlanid = raw_input("Enter VLAN id to be added: ")
    name = raw_input("Enter VLAN name: ")

    handle = UcsHandle(hostname, username, password)
    handle.login()
    print(add_vlan(handle, vlanid, name))

if __name__ == '__main__':
    main()
