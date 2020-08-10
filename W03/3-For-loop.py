#add 1 to every octet in ip address
ip = '192.168.1.1'
print(ip)

new_ip=[]

ip_octet = ip.split('.')

print(ip_octet)


for i in ip_octet:
    sum = int(i) + 1
    print(sum)

    new_ip.append(str(sum))


a = ".".join(new_ip)
print(a)


"""
#ip_octet contains the list


for i in ip_octet:

    #print(i)

    sum = int(i) + 1

    #print(sum)
    new_ip.append(str(sum))
    #print(new_ip)


new_ip = []
print(new_ip)
a = ".".join(new_ip)
print(a)
"""