from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../.env')
DATABASE_USER = os.getenv("MONGO_ROOT_USERNAME")
DATABASE_PASSWORD = os.getenv("MONGO_ROOT_PASSWORD")
DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME")
DATABASE_HOST = 'localhost'

# The root user is created in the "admin" database during MongoDB initialization,
# so we must authenticate against the "admin" database even if we're using another DB.
client = MongoClient(
    f"mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:27018/{DATABASE_NAME}?authSource=admin"
)
db = client[DATABASE_NAME]
todos = db["todos"]

def add_task(title):
    task = {
        "title": title,
        "completed": False,
        "created_at": datetime.utcnow()
    }
    todos.insert_one(task)
    print("Task added successfully.")

def list_tasks():
    print("\n Your TODO list:")
    for idx, task in enumerate(todos.find().sort("created_at", -1), 1):
        status = "Done" if task["completed"] else "Doing"
        print(f"{idx}. {task['title']} {status} (id: {task['_id']})")

def mark_completed(task_id):
    try:
        result = todos.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})
        if result.modified_count:
            print("Task marked as completed.")
        else:
            print("Task not found or already completed.")
    except Exception as e:
        print(f"Error: {e}")

def delete_task(task_id):
    try:
        result = todos.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count:
            print("Task deleted.")
        else:
            print("Task not found.")
    except Exception as e:
        print(f"Error: {e}")

def menu():
    while True:
        print("\n TODO Menu")
        print("1. Add new task")
        print("2. Show all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = input("Task ID: ")
            mark_completed(task_id)
        elif choice == "4":
            task_id = input("Task ID: ")
            delete_task(task_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()