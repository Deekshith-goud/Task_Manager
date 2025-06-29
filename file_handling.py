import os


def add_task():
    filename = input("Enter filename to save tasks (e.g., tasks.txt): ")
    task = input("Enter task description: ")
    date = input("Enter task deadline (YYYY-MM-DD): ")
    
    with open(filename, 'a') as file:
        file.write(f"Task: {task} | Deadline: {date}\n")
    
    print("Task added successfully.")

def view_tasks():
    filename = input("Enter filename to view tasks (e.g., tasks.txt): ")
    
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
            print("Tasks in file:")
            for task in tasks:
                print(task.strip())

            
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


