import hashlib
import os
import json

# File paths for storing user credentials and tasks
USERS_FILE = 'users.json'
TASKS_FILE = 'tasks.json'

# Helper function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Check if the user file exists, otherwise create an empty one
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f)

    # Load existing users
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)

    # Check if the username is unique
    if username in users:
        print("Username already exists. Please choose a different one.")
        return False

    # Save the hashed password for the new user
    users[username] = hash_password(password)
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

    print("User registered successfully!")
    return True

# Function to authenticate an existing user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Load existing users
    if not os.path.exists(USERS_FILE):
        print("No users registered. Please register first.")
        return None

    with open(USERS_FILE, 'r') as f:
        users = json.load(f)

    # Validate credentials
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Function to add a task
def add_task(username):
    task_description = input("Enter the task description: ")

    # Check if the task file exists, otherwise create an empty one
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump({}, f)

    # Load existing tasks
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    # Generate a unique task ID
    task_id = len(tasks.get(username, [])) + 1
    task = {
        'id': task_id,
        'description': task_description,
        'status': 'Pending'
    }

    # Add the task to the user's task list
    if username not in tasks:
        tasks[username] = []
    tasks[username].append(task)

    # Save tasks back to the file
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

    print("Task added successfully!")

# Function to view tasks
def view_tasks(username):
    if not os.path.exists(TASKS_FILE):
        print("No tasks found.")
        return

    # Load tasks
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    # Display tasks for the logged-in user
    user_tasks = tasks.get(username, [])
    if not user_tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for task in user_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

# Function to mark a task as completed
def mark_task_completed(username):
    task_id = int(input("Enter the task ID to mark as completed: "))

    if not os.path.exists(TASKS_FILE):
        print("No tasks found.")
        return

    # Load tasks
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    # Find the task for the logged-in user
    user_tasks = tasks.get(username, [])
    for task in user_tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            with open(TASKS_FILE, 'w') as f:
                json.dump(tasks, f)
            print("Task marked as completed.")
            return

    print("Task not found.")

# Function to delete a task
def delete_task(username):
    task_id = int(input("Enter the task ID to delete: "))

    if not os.path.exists(TASKS_FILE):
        print("No tasks found.")
        return

    # Load tasks
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)

    # Remove the task for the logged-in user
    user_tasks = tasks.get(username, [])
    for task in user_tasks:
        if task['id'] == task_id:
            user_tasks.remove(task)
            with open(TASKS_FILE, 'w') as f:
                json.dump(tasks, f)
            print("Task deleted successfully.")
            return

    print("Task not found.")

# Main function for the interactive menu
def task_manager():
    print("Welcome to the Task Manager!")

    # User authentication
    logged_in_user = None
    while not logged_in_user:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            logged_in_user = login_user()
        elif choice == '3':
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

    # Interactive menu for task management
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Delete Task\n5. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(logged_in_user)
        elif choice == '2':
            view_tasks(logged_in_user)
        elif choice == '3':
            mark_task_completed(logged_in_user)
        elif choice == '4':
            delete_task(logged_in_user)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_manager()
