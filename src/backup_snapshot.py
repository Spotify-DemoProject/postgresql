from configparser import ConfigParser
from datetime import datetime
import subprocess
import os, sys

lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../lib")
sys.path.append(lib_dir)

from os_libs import check_mkdirs

snapshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../snapshot")
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../config/config.ini")
config = ConfigParser()
config.read(config_path)

DB_HOST = config.get("PostgreSQL", "DB_HOST")
DB_PORT = config.get("PostgreSQL", "DB_PORT")
DB_USER = config.get("PostgreSQL", "DB_USER")
DB_PASSWORD = config.get("PostgreSQL", "DB_PASSWORD")

check_mkdirs(dir=f'{snapshot_path}/{datetime.now().strftime("%Y-%m-%d")}')
backup_dir = f'{snapshot_path}/{datetime.now().strftime("%Y-%m-%d")}/{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}.sql'

dump_command = [
    'pg_dump',
    '-h', DB_HOST,
    '-p', str(DB_PORT),
    '-U', DB_USER,
    '-F', 'c',
    '-b',
    '-v',
    '-f', backup_dir,
    'spotify'
]

os.environ['PGPASSWORD'] = DB_PASSWORD

subprocess.run(dump_command)
print(f"Backup completed. Backup file: {backup_dir}")

os.environ.pop('PGPASSWORD', None)
