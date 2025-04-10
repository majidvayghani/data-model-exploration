import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='../.env')

# Get the database credentials from environment variables
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
    print("Connection to the database was successful!")

    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Example query: Check the version of the database
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Database version: {db_version[0]}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error: {error}")

