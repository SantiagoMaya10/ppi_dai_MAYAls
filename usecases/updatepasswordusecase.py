from databaseconfig.dbconfig import MySqLConnectionCreator

def update_password_usecase(new_password: str ,username: str):
    connector = MySqLConnectionCreator()
    conn = connector.db_conn
    cursor = conn.cursor()
    query = """UPDATE user 
    SET password = %s
    WHERE username = %s """    
    
    cursor.execute(query, (new_password,username))
    conn.commit()
    connector.close_db_connection(conn)

