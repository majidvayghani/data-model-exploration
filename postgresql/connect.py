import psycopg2
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='../.env')

# Get database credentials
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')  
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5433'

# Configure logging
logging.basicConfig(
    filename='queries.log',
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

# Function to log SQL query
def log_query(query):
    logging.info(f"Executed query: {query}")


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
    logging.info("Connected to the database. You can now execute queries.")
    print("Type 'exit' to close the connection.")

    # Interactive query execution
    while True:
        query = input("SQL> ").strip()
        if query.lower() == 'exit':
            break
        try:
            log_query(query)
            cursor.execute(query)

            if cursor.description:
                results = cursor.fetchall()
                for row in results:
                    print(row)
            else:
                logging.info("Query executed successfully.")
                print("Query executed successfully.")
        except Exception as query_error:
            logging.error(f"Error executing query: {query_error}")
            print(f"Error executing query: {query_error}")

    cursor.close()
    connection.close()
    logging.info("Connection closed.")
    print("Connection closed.")

except Exception as conn_error:
    logging.info(f"Error connecting to the database: {conn_error}")
    print(f"Error connecting to the database: {conn_error}")
