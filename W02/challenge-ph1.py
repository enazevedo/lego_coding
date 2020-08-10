# Phase1 - Work in a single entry

print('''
##### Step 1 - Check size list / Break the list''')

subnets = ['192.168.1.128/24', '192.168.2.0/24', '192.168.3.0/24']

gateway_list = {}

print("Size of list = ",len(subnets))


# IF
print(subnets[0])
print(subnets[1])
print(subnets[2])

print('''
##### Step 2 - Split In octets''')

ipandmask = subnets[0].split("/")
print(ipandmask)
ip = ipandmask[0:1]
print(ip)
mask = ipandmask[1:2]
print(mask)

print('''
##### Step 3 - Identify VLAN and GW''')

octets = ip[0].split(".")
print(octets)
vlan_number = octets[2].zfill(3)
print(vlan_number)
gw4oct = int(octets[3]) + 1
print(gw4oct)

print('''
##### Step 4 - Replace the last entry of octects and join them''')

octets[3] = str(gw4oct)
print(octets)
gw = '.'.join(octets)
print(gw)

vlan = "vlan_" + vlan_number
print(vlan)

print('''
##### Step 5 - Update the list and FUCK YES!''')
new_entry = {vlan : gw}
print (new_entry)

gateway_list.update(new_entry)
print (gateway_list)

# close if

# print(gateway_list)
