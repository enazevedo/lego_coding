gateway = {}	#this will be used to store the vlan_id and gateway ip

subnets = ['192.168.1.0/24', '192.168.2.0/24', '192.168.3.0/24']  #input list
print(subnets)


#Tip#1: Use for loop to go through each value of subnet. Use indent for succeeding lines of codes
for i in subnets:

	
	#Tip#2: Use split function to divide the ip into individual values for a list

    #Tip#3: Convert 3rd octet to  mathematical operation

    #Tip#4: get the 4th octet value and add 1

    #Tip#5: bring it all together in a single dictionary using update command

print(gateway)