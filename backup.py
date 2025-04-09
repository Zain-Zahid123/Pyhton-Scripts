import os
import shutil
import datetime
import zipfile

# CHANGE THESE TWO LINES with your own folder paths (using forward slashes)
source_directory = "C:/Users/Admin/Pyhton-Practice"  # Path to the folder you want to backup
backup_directory = "C:/Users/Admin/Pyhton-Practice/destination-empty-folder"  # Path where backups will be stored

# Create timestamp for unique backup file name
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file_name = f"backup_{timestamp}.zip"
backup_path = os.path.join(backup_directory, backup_file_name)

# Create backup directory if it doesn't exist
if not os.path.exists(backup_directory):
    os.makedirs(backup_directory)
    print(f"Created backup directory: {backup_directory}")

# Do the backup
try:
    # Check if source exists
    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
    else:
        # Create a zip file
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the directory and add files to the zip
            for root, dirs, files in os.walk(source_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Create a proper relative path for files in the zip
                    arcname = os.path.relpath(file_path, start=source_directory)
                    zipf.write(file_path, arcname)
        
        print(f"Compressed backup created successfully at: {backup_path}")
        print(f"Backup size: {os.path.getsize(backup_path)/1024/1024:.2f} MB")
except Exception as e:
    print(f"Backup failed: {e}")