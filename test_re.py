''' This script provides the IP address of the current host PC'''
import re
import subprocess
# Run ipconfig to get IP data
# output = subprocess.check_output(["ipconfig.exe"])
# For 
output = subprocess.check_output(["ifconfig"])
# Filter inet address, if found. Note: check_output() for python3 returns a byte-string, so we need to 
# indicate 'output' as byte-string via string-modifier 'b'. 
result = re.search(b"inet\s+([\d.]+)", output)
print ("regex-result:", result)
if result:
    print (result.group(1))
