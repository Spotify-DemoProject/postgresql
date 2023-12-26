import os, sys

lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../lib")
sys.path.append(lib_dir)

from s3_libs import upload_to_s3
from datetime import datetime

snapshot_folder_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../snapshot")
local_dir = f"{snapshot_folder_dir}/{datetime.now().strftime("%Y-%m-%d")}"

bucket_name = "spotify-snapshot-backup"
upload_to_s3(bucket_name=bucket_name, 
             local_dir=local_dir)
