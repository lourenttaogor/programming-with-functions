"""
Author: Okuku Ogorchukwu Lourentta
Purpose: The program is designed to help users efficiently manage tasks and events by providing a structured,
interactive system for organizing their daily activities. it allows users to add, view and delete tasks.
"""

import datetime
import csv


def add_task(filename, task_name, task_details, task_date):

    #store task information in localStorage
    # For a simple script, we'll use a file to simulate localStorage
    with open(filename, "at") as file:
        file.write(f"{task_name}|{task_details}|{task_date}\n")
    try:
        task_date = datetime.datetime.strptime(task_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    

def view_tasks(file_name):
    try:
        with open(file_name, "rt") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
                return
            for task in tasks:
                name, details, date = task.strip().split("|")
                print(f"Task: {name}, Details: {details}, Date: {date}")
    except FileNotFoundError:
        print("No tasks found.")

def delete_task(file_name, task_name):
    with open(file_name, "rt") as filename:
        file_lines = filename.readlines()
    # Filter tasks matching the task_name (case-insensitive)
    matching_tasks = [line for line in file_lines if line.lower().startswith(task_name.lower())]

    if not matching_tasks:
        print("No tasks found with the given name.")
        return

    # Display matching tasks with indices
    print("Matching tasks:")
    for idx, task in enumerate(matching_tasks, start=1):
        name, details, date = task.strip().split("|")
        print(f"{idx}. Task: {name}, Details: {details}, Date: {date}")

    try:
        del_index = int(input("Enter the number of the task you wish to delete: "))
        if del_index < 1 or del_index > len(matching_tasks):
            print("Invalid index selected.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Remove the selected task from file_lines
    task_to_delete = matching_tasks[del_index - 1]
    file_lines.remove(task_to_delete)

    # Write the updated tasks back to the file
    with open(file_name, "wt") as filename:
        filename.writelines(file_lines)
    print("Task deleted successfully.")
        



def main():
    while True:
        try:
            print("Welcome to the Event Planner!")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Close eventplanner")
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                task_name = input("Enter the task name: ")
                task_details = input("Enter the task details: ")
                task_date = input("Enter the task date (YYYY-MM-DD): ")
                add_task("tasks.txt", task_name, task_details, task_date)
            elif choice == "2":
                view_tasks("tasks.txt")
            elif choice == "3":
                task_name = input("Enter the name of the task to delete: ")
                delete_task("tasks.txt", task_name)
            elif choice == "4":
                print("Done.")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3 or 4.")
        except ValueError:
            print("invalid! make a valid chioice.")

if __name__ == "__main__":
    main()