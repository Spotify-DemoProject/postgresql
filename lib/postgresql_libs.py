
def get_connection(DB_NAME:str):
    import psycopg2
    from configparser import ConfigParser
    import os
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../config/config.ini")
    config = ConfigParser()
    config.read(config_path)

    DB_HOST = config.get("PostgreSQL", "DB_HOST")
    DB_PORT = config.get("PostgreSQL", "DB_PORT")
    DB_USER = config.get("PostgreSQL", "DB_USER")
    DB_PASSWORD = config.get("PostgreSQL", "DB_PASSWORD")
    
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    return conn

def execute_query(QUERY:str, VALUES:tuple=None):
    conn = get_connection(DB_NAME="spotify")
    cursor = conn.cursor()

    if VALUES == None:
        cursor.execute(QUERY)
    else:
        cursor.execute(QUERY, VALUES)

    conn.commit()
    conn.close()

def fetchall_query(QUERY:str, VALUES:tuple=None):
    conn = get_connection(DB_NAME="spotify")
    cursor = conn.cursor()
    
    if VALUES == None:
        cursor.execute(QUERY)
    else:
        cursor.execute(QUERY, VALUES)
    
    rows = cursor.fetchall()
    conn.close()
    
    return rows
