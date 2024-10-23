# Task Manager with User Authentication

## Description

The Task Manager is a Python-based application that helps users manage their tasks in a structured way. It includes user authentication, allowing each user to register and log in with a unique username and password. Once logged in, users can create, view, update, and delete tasks. Each user's tasks are stored separately, ensuring that only the authenticated user can access their tasks.

## Features

- **User Authentication:** Allows for user registration and login with password hashing for secure storage.
- **Task Management:** Users can add new tasks, view existing tasks, mark tasks as completed, and delete tasks.
- **File Handling:** User credentials and tasks are stored in JSON files to persist data between program runs.
- **Interactive Menu-Driven Interface:** Provides a simple and user-friendly menu for navigation.

## Objectives

1. Implement a user authentication system (registration and login).
2. Create a task management system with options to:
   - Add, view, mark as completed, and delete tasks.
3. Use file handling to store user credentials and tasks persistently.
4. Create an interactive, menu-driven interface for task management.

## Requirements

- Python 3.x

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/task-manager-authentication.git
   ```
2. **Navigate to the Project Directory**
   ```bash
   cd task-manager-authentication
   ```
3. **Run the Application**
   ```bash
   python task_manager.py
   ```

## How to Use

1. **User Authentication**
   - Upon launching the program, you will be prompted to either register a new account or log in to an existing one.
   - Registration will require a unique username and a password, which is securely hashed and stored.
   - If you choose to log in, the program will verify your credentials against the stored user data.

2. **Task Management**
   - Once logged in, you can:
     - **Add a Task:** Provide a description for the task, which will be stored as "Pending" by default.
     - **View Tasks:** See a list of all your tasks with their statuses.
     - **Mark a Task as Completed:** Update the status of a task to "Completed" by providing its ID.
     - **Delete a Task:** Remove a task from your task list by its ID.
   - **Logout:** You can log out of the application to secure your session.

## File Structure

- `task_manager.py`: The main script that contains the code for the task manager and user authentication.
- `users.json`: Stores the user credentials (username and hashed password).
- `tasks.json`: Stores the tasks associated with each user.

## Example Output

```
Welcome to the Task Manager!

1. Register
2. Login
3. Exit
Choose an option: 
```

After logging in:
```
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Logout
Choose an option: 
```

## Security Considerations

- **Password Hashing:** The application uses SHA-256 to hash passwords before storing them in the `users.json` file, adding a layer of security to the user authentication system.
- **Data Isolation:** Each user's tasks are stored separately, ensuring data isolation and privacy.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README provides a clear overview of the project, setup instructions, and a guide on how to use the application.
