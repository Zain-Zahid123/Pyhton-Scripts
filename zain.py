# Script to take a backup from local to s3 
import os
import tarfile
import boto3
from datetime import datetime

# Configuration
LOCAL_DIR = "/path/to/local/directory"  # Change this to the directory you want to backup
S3_BUCKET = "your-s3-bucket-name"
S3_BACKUP_PREFIX = "backups/"  # Folder in S3 where backups will be stored
BACKUP_RETENTION_DAYS = 7  # Number of days to keep backups in S3
AWS_REGION = "us-east-1"  # Change this to your AWS region

# Create an S3 client
s3 = boto3.client("s3", region_name=AWS_REGION)

def create_backup():
    """Creates a compressed .tar.gz backup of the local directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join("/tmp", backup_filename)  # Temporarily store backup

    with tarfile.open(backup_path, "w:gz") as tar:
        tar.add(LOCAL_DIR, arcname=os.path.basename(LOCAL_DIR))

    print(f"Backup created: {backup_path}")
    return backup_path, backup_filename

def upload_to_s3(file_path, file_name):
    """Uploads the backup file to S3."""
    s3_key = S3_BACKUP_PREFIX + file_name
    s3.upload_file(file_path, S3_BUCKET, s3_key)
    print(f"Uploaded {file_name} to s3://{S3_BUCKET}/{s3_key}")

def cleanup_old_backups():
    """Deletes backups older than the retention period from S3."""
    objects = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_BACKUP_PREFIX).get("Contents", [])
    cutoff_time = datetime.now().timestamp() - (BACKUP_RETENTION_DAYS * 86400)

    for obj in objects:
        obj_time = obj["LastModified"].timestamp()
        if obj_time < cutoff_time:
            s3.delete_object(Bucket=S3_BUCKET, Key=obj["Key"])
            print(f"Deleted old backup: {obj['Key']}")

if __name__ == "__main__":
    backup_path, backup_filename = create_backup()
    upload_to_s3(backup_path, backup_filename)
    cleanup_old_backups()
    os.remove(backup_path)  # Clean up local backup file
    print("Backup process completed successfully!")

