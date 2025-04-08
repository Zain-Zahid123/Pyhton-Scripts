import os  # Importing the OS module to execute system-related commands

# Displaying total and available physical memory
print(os.system('systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"'))  

# Displaying disk drive size
print(os.system('wmic diskdrive get size'))  

# Displaying system boot time
print(os.system('systeminfo | find "System Boot Time"'))  

# Displaying CPU load percentage
print(os.system('wmic cpu get loadpercentage'))  

# Checking for disk errors on the C: drive
print(os.system('chkdsk C:'))  