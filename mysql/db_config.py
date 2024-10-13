import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            user='root',  
            password='rushitemgire',
            host='localhost',      
            database='pdbc'   
        )
        return connection
    except Exception:
        print("Some problem occured")
        return None