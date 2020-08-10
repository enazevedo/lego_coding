subnets = ['192.168.1.0/24', '192.168.2.0/24', '192.168.3.0/24']

gateway_list = {}
loop = 0
subnets_item = 0

while loop < len(subnets):
    ipandmask = subnets[subnets_item].split("/")
    ip = ipandmask[0:1]
    mask = ipandmask[1:2]
    
    octets = ip[0].split(".")
    vlan_number = int(octets[2]) + 10
    vlan_number = str(vlan_number).zfill(3)
    gw4oct = int(octets[3]) + 1
    
    octets[3] = str(gw4oct)
    gw = '.'.join(octets)
    vlan = "vlan_" + (vlan_number)
    
    new_entry = {vlan : gw}
    gateway_list.update(new_entry)
    loop += 1
    subnets_item += 1

print(gateway_list)