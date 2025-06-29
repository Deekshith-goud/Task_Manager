from datetime import datetime

def check_deadlines():
    filename = input("Enter filename to check deadlines (e.g., tasks.txt): ")
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found in the file.")
            return

        current_date = datetime.now().date()
        results = []
        for task in tasks:
            task_details = task.strip().split(' | ')
            try:

                deadline_str = task_details[1].split(': ')[1]
                

                deadline_date = datetime.strptime(deadline_str, '%Y-%m-%d').date()

                task_name = task_details[0].split(': ')[1]

                if deadline_date <= current_date:
                    results.append(f"Task '{task_name}' has reached its deadline on {deadline_date}!")

                    
            except (IndexError, ValueError):
                continue  # Skip malformed entries

        if results:
            print("\nDeadline Alerts:")
            for alert in results:
                print(alert)
        else:
            print("No tasks have reached their deadlines.")


    except FileNotFoundError:
        print(f"File '{filename}' not found.")
