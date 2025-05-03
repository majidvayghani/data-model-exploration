import psycopg2
import os
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

# Database credentials
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5433'

# Connect to the database
connection = psycopg2.connect(
    dbname=DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)
connection.autocommit = True
cursor = connection.cursor()

# Ask user if tables should be cleared
answer = input("Do you want to clear existing tables before inserting new data? (yes/no): ").strip().lower()

if answer == 'yes':
    print("Clearing tables...")
    cursor.execute("DELETE FROM tokens_token;")
    cursor.execute("DELETE FROM transactions_transaction;")
    cursor.execute("DELETE FROM transactions_transactioncategory;")
    cursor.execute("DELETE FROM accounts_profile;")
    cursor.execute("DELETE FROM accounts_user;")
    print("Tables cleared.")
else:
    print("Existing data will be kept.")

# Read generated data
with open('generated_data.json', 'r') as f:
    data = json.load(f)

# Insert users
for user in data['users']:
    cursor.execute("""
        INSERT INTO accounts_user
        (_id, password, last_login, is_superuser, email, is_staff, is_active, created_at, updated_at, soft_deleted_at, hard_deleted_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL, NULL);
    """, (
        user["_id"],
        user["password"],
        user["last_login"],
        user["is_superuser"],
        user["email"],
        user["is_staff"],
        user["is_active"],
        user["created_at"],
        user["updated_at"]
    ))

# Insert profiles
for profile in data['profiles']:
    cursor.execute("""
        INSERT INTO accounts_profile
        (_id, _user_id, first_name, last_name, created_at, updated_at, soft_deleted_at, hard_deleted_at)
        VALUES (%s, %s, %s, %s, %s, %s, NULL, NULL);
    """, (
        profile["_id"],
        profile["_user_id"],
        profile["first_name"],
        profile["last_name"],
        profile["created_at"],
        profile["updated_at"]
    ))

# Insert categories
for category in data['categories']:
    cursor.execute("""
        INSERT INTO transactions_transactioncategory
        (_id, name, parent_id, category_type, created_at, updated_at, soft_deleted_at, hard_deleted_at)
        VALUES (%s, %s, %s, %s, %s, %s, NULL, NULL);
    """, (
        category["_id"],
        category["name"],
        category["parent_id"],
        category["category_type"],
        category["created_at"],
        category["updated_at"]
    ))

# Insert transactions
for transaction in data['transactions']:
    cursor.execute("""
        INSERT INTO transactions_transaction
        (_id, _user_id, date, amount, _category_id, description, tag, created_at, updated_at, soft_deleted_at, hard_deleted_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL, NULL);
    """, (
        transaction["_id"],
        transaction["_user_id"],
        transaction["date"],
        transaction["amount"],
        transaction["_category_id"],
        transaction["description"],
        transaction["tag"],
        transaction["created_at"],
        transaction["updated_at"]
    ))

# Insert tokens
for token in data['tokens']:
    cursor.execute("""
        INSERT INTO tokens_token
        (_id, _user_id, is_active, token, expired_at, created_at, updated_at, soft_deleted_at, hard_deleted_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, NULL, NULL);
    """, (
        token["_id"],
        token["_user_id"],
        token["is_active"],
        token["token"],
        token["expired_at"],
        token["created_at"],
        token["updated_at"]
    ))

print("Data inserted successfully.")

# Close connection
cursor.close()
connection.close()

