
def upload_to_s3(bucket_name:str, local_dir:str):
    import os, sys

    lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../lib")
    sys.path.append(lib_dir)

    from os_libs import send_line_notification
    import boto3, os
    from configparser import ConfigParser
    
    config = ConfigParser()
    config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../config/config.ini")
    config.read(config_dir)

    aws_access_key_id = config.get("AWS", "access_key")
    aws_secret_access_key = config.get("AWS", "secret_key")

    s3 = boto3.client('s3', 
                      aws_access_key_id=aws_access_key_id, 
                      aws_secret_access_key=aws_secret_access_key)
                
    try:
        for root, dirs, files in os.walk(local_dir):
            s3_root = root.split("/")[-1]
            
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, local_dir)
                s3_path = os.path.join(s3_root, relative_path).replace("\\", "/") 
                s3.upload_file(local_path, bucket_name, s3_path)
                print(f'Uploaded {local_path} to {s3_path}')
                
    except Exception as E:
        print(f"Upload SNAPSHOT : Error Appeared - {E}")
        send_line_notification(message=E)
