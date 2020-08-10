import json

#firmware counter dictionary that will contain the firmware version as key and count as value
firmware_counter = {}
#not running configured version dictionary that will contain the S/N and URL for devices with firmware not running configured version
not_running_configured_version = {}
# Opening JSON file
f = open('getOrganizationDevices.json', )
# returns JSON object as a dictionary
data = json.load(f)
f.close()

loop = 0

#Tip#1: Use for loop to iterate through json data - for i in data:
while loop < len(data):
    #Tip#2:  print variable i to get information on the key value pair for the json data. Take note of keys firmware, serial number and url
    #print(i)
    firmware = data[loop].get("firmware")
    serial = data[loop].get("serial")
    url = data[loop].get("url")
    loop += 1
    #Tip#3: Use if statement to check if firmware exists in firmware_counter dictionary and then add the count. Else, update the dictionary with firmware and 1
    if not firmware in firmware_counter:
        new_entry_firmware = {firmware: int(1)}
        firmware_counter.update(new_entry_firmware)
    else:
        firmware_counter[firmware] += 1
    #Tip#4: Use if statement to compare firmware with "Not running configured version" then update the the dictionary with S/N and URl
    if firmware == "Not running configured version":
        new_entry_not_running = {serial: url}
        not_running_configured_version.update(new_entry_not_running)

# Closing file
print(firmware_counter)
print(not_running_configured_version)





