import mysql.connector
from mysql.connector import Error

def insert_data():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3301,  # Connect to the master
            user='root',
            password='<Password>',
            database='<DB_Name>'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS <DB_Name>")
            cursor.execute("USE <DB_Name>")
            cursor.execute("DROP TABLE IF EXISTS students")
            cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
            
            names = ['User1', 'User2', 'Ashlin']
            for i in range(10000):
                name = names[i % len(names)]
                cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
            
            connection.commit()
            print("Data inserted successfully")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_data()
