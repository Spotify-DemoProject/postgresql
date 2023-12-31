# postgresql
Spotify API 데이터 수집 과정에서 반복적으로 사용되는 파라미터 정보를 적재합니다.<br>
주기적으로 데이터를 자동 백업하여 AWS S3 스토리지에 보관하고 있습니다.<br><br>

# Structure
<img width="581" alt="스크린샷 2024-01-01 오전 1 46 21" src="https://github.com/Spotify-DemoProject/postgresql/assets/130134750/be59bfdf-325a-4b7b-8aa9-e8c0b9c13b2f">
<br>

# Before Start
``` bash
sudo apt install postgresql postgresql-contrib
sudo systemctl enable postgresql
sudo systemctl start postgresql
```
``` bash
sudo -u postgres psql
postgres=# CREATE DATABASE 'spotify'; 
postgres=# CREATE USER api WITH PASSWORD '<password>'; 
postgres=# GRANT ALL PRIVILEGES ON DATABASE spotify TO api;
postgres=# exit;

psql -h localhost -U api spotify
```
``` sql
CREATE TABLE IF NOT EXISTS albums (
    album_id VARCHAR(30) PRIMARY KEY,
    release_date VARCHAR(10),
    insert_date DATE
);

CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(30) PRIMARY KEY,
    insert_date DATE
);

CREATE TABLE IF NOT EXISTS tracks (
    track_id VARCHAR(30) PRIMARY KEY,
    insert_date DATE
);
```
- install pip modules for S3 data backup
``` bash
pip install boto3
```
<br>

# Result
<img width="422" alt="스크린샷 2023-12-30 오후 9 54 32" src="https://github.com/Spotify-DemoProject/postgresql/assets/130134750/c51b3e2d-0628-4465-b95d-ef6abd161d36"><br><br>
<img width="709" alt="스크린샷 2024-01-01 오전 1 49 53" src="https://github.com/Spotify-DemoProject/postgresql/assets/130134750/f3577a60-34b5-4fcb-98d1-76d1332233d0">

