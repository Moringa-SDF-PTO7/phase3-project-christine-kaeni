# cli.py
from models.database import initialize_db, Session
from models.user import User
from models.task import Task
from models.habit import Habit

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Manage Users")
        print("2. Manage Tasks")
        print("3. Manage Habits")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            user_menu()
        elif choice == '2':
            task_menu()
        elif choice == '3':
            habit_menu()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Create User")
        print("2. View All Users")
        print("3. Find User by ID")
        print("4. Delete User")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            User.create(name, email)
            print(f"User '{name}' created.")
        elif choice == '2':
            users = User.get_all()
            for user in users:
                print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
        elif choice == '3':
            user_id = input("Enter user ID: ")
            user = User.find_by_id(user_id)
            if user:
                print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
            else:
                print("User not found.")
        elif choice == '4':
            user_id = input("Enter user ID to delete: ")
            user = User.find_by_id(user_id)
            if user:
                user.delete()
                print("User deleted.")
            else:
                print("User not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def task_menu():
    while True:
        print("\nTask Menu:")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. Find Task by ID")
        print("4. Delete Task")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            user_id = input("Enter user ID for this task: ")
            Task.create(title, description, user_id)
            print(f"Task '{title}' created.")
        elif choice == '2':
            tasks = Task.get_all()
            for task in tasks:
                print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, User ID: {task.user_id}")
        elif choice == '3':
            task_id = input("Enter task ID: ")
            task = Task.find_by_id(task_id)
            if task:
                print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")
            else:
                print("Task not found.")
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            task = Task.find_by_id(task_id)
            if task:
                task.delete()
                print("Task deleted.")
            else:
                print("Task not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def habit_menu():
    while True:
        print("\nHabit Menu:")
        print("1. Create Habit")
        print("2. View All Habits")
        print("3. Find Habit by ID")
        print("4. Delete Habit")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter habit name: ")
            frequency = input("Enter habit frequency (e.g., daily, weekly): ")
            user_id = input("Enter user ID for this habit: ")
            Habit.create(name, frequency, user_id)
            print(f"Habit '{name}' created.")
        elif choice == '2':
            habits = Habit.get_all()
            for habit in habits:
                print(f"ID: {habit.id}, Name: {habit.name}, Frequency: {habit.frequency}, User ID: {habit.user_id}")
        elif choice == '3':
            habit_id = input("Enter habit ID: ")
            habit = Habit.find_by_id(habit_id)
            if habit:
                print(f"ID: {habit.id}, Name: {habit.name}, Frequency: {habit.frequency}")
            else:
                print("Habit not found.")
        elif choice == '4':
            habit_id = input("Enter habit ID to delete: ")
            habit = Habit.find_by_id(habit_id)
            if habit:
                habit.delete()
                print("Habit deleted.")
            else:
                print("Habit not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    initialize_db()  # Create tables if they don't exist
    main_menu()
