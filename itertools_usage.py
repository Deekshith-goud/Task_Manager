import itertools

def generate_task_combinations():
    filename = input("Enter filename to generate task combinations (e.g., tasks.txt): ")
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
            if len(tasks) < 3:
                print("At least 3 tasks are required to generate combinations.")
                return
            task_combinations = list(itertools.combinations(tasks, 2))
            print("\nTask combinations (pick two tasks to do):")
            for combo in task_combinations:
                print(" - ".join([task.strip() for task in combo]))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

