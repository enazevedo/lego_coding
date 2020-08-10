#add 1 to every octet in ip address
ip_list = ['192.168.1.1', '192.168.2.1', '192.168.3.1']

new_ip_list = []
for i in ip_list:

    ip = i.split('.')
    new_ip = []

    for j in ip:

        sum = int(j) + 1
        #print(sum)
        new_ip.append(str(sum))

    new_ip = ".".join(new_ip)
    print(new_ip)

    new_ip_list.append(new_ip)

print(new_ip_list)