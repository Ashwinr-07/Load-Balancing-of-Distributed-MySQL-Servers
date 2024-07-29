import mysql.connector
from mysql.connector import Error
import time

def connect_to_single_db():
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
            cursor.execute("SELECT @@hostname")
            server = cursor.fetchone()[0]
            return connection, server
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

def connect_to_multi_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=8080,  # Connect to the load balancer
            user='root',
            password='<Password>',
            database='<DB_Name>'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT @@hostname")
            server = cursor.fetchone()[0]
            return connection, server
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

def read_data(num_queries, multi_server=False):
    server_counts = {}
    start_time = time.time()

    for _ in range(num_queries):
        if multi_server:
            connection, server = connect_to_multi_db()
        else:
            connection, server = connect_to_single_db()

        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM students")
            count = cursor.fetchone()[0]
            server_counts[server] = server_counts.get(server, 0) + 1
            cursor.close()
            connection.close()
        time.sleep(0.1)  # Small delay to avoid overwhelming the servers

    end_time = time.time()

    print("\nLoad Balancing Results ({}):".format("Multiple Servers" if multi_server else "Single Server"))
    for server, count in server_counts.items():
        print(f"{server}: {count} queries")
    print(f"\nTotal time: {end_time - start_time:.2f} seconds")
    print(f"Average queries per second: {num_queries / (end_time - start_time):.2f}")

if __name__ == "__main__":
    num_queries = 1000

    print("Reading from a single server:")
    read_data(num_queries, multi_server=False)

    print("\nReading from multiple servers (load-balanced):")
    read_data(num_queries, multi_server=True)
