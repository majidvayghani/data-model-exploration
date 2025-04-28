import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='../.env')

# Get database credentials
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')  
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5433'

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    connection.autocommit = False  # Optional: To automatically save changes
    cursor = connection.cursor()

    print("Connected to the database. You can now execute queries.")
    print("Type 'exit' to close the connection.")

    # Interactive query execution
    while True:
        query = input("SQL> ").strip()
        if query.lower() == 'exit':
            break
        try:
            cursor.execute(query)

            if cursor.description:
                results = cursor.fetchall()
                for row in results:
                    print(row)
            else:
                print("Query executed successfully.")
        except Exception as query_error:
            print(f"Error executing query: {query_error}")

    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as conn_error:
    print(f"Error connecting to the database: {conn_error}")
