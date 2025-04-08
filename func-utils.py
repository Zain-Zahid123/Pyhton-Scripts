import os
import datetime  # Importing datetime module

# Function to check Disk Drive Size
def get_disk_drive_size():
    print("Disk Drive Size:")
    os.system("wmic diskdrive get size")
    print("-" * 50)

# Function to check RAM (Total and Available Physical Memory)
def get_ram_size():
    print("RAM Information:")
    os.system('systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"')
    print("-" * 50)

# Function to check System Boot Time
def get_system_boot_time():
    print("System Boot Time:")
    os.system('systeminfo | find "System Boot Time"')
    print("-" * 50)

# Function to check CPU Load Percentage
def get_cpu_load():
    print("CPU Load Percentage:")
    os.system('wmic cpu get loadpercentage')
    print("-" * 50)

# Function to get the current Date and Time
def date_time():
    current_time = datetime.datetime.now()  # Get the current date and time
    print("Current Date and Time:")
    print(current_time.strftime("%Y-%m-%d %H:%M:%S"))  # Format the date and time to be more readable
    print("-" * 50)

# Main Execution
get_disk_drive_size()      # Calling the function to get disk size
get_ram_size()             # Calling the function to get RAM info
get_system_boot_time()     # Calling the function to get system boot time
get_cpu_load()             # Calling the function to get CPU load percentage
date_time()                # Calling the function to get the current date and time