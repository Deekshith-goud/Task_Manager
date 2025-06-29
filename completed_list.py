def make_task_complete():
    filename=input("Enter the name of the file: ") 
    task_name=input("Enter the name of the task to mark as completed: ")
    try:
        with open(filename,'a+') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() == task_name:
                    file.write(line.strip() + ' Completed\n')
                else:
                    file.write(line)
        print(f"Task '{task_name}' marked as completed.")

    except FileNotFoundError: 
        print(f"The file {filename} does not exist.")

        
def completed_task():
    filename=input("Enter the name of the file: ")
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            completed_tasks = [line.strip() for line in lines if line.strip().endswith('Completed')]
            if completed_tasks:
                print("Completed tasks:")
                for task in completed_tasks:
                    print(task)
            else:
                print("No completed tasks found.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


