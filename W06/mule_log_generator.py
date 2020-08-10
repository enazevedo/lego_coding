# This script searches for a match in the log file and creates another file only with line that have a match.
#Git Test
# Application input
search_object = "dhcp"
log_file = "event_messages.txt"

# Read the content of the file and create a list.
with open(log_file, 'r') as file:
    content = file.read()
content_list = content.split('\n')

# Check for a match and add the line to a new file.
for i in content_list:
    if search_object in i:
        with open(f'mule_{search_object}.txt', 'w+') as f:
            f.write(i + '\n')


