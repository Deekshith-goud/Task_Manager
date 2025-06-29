from file_handling  import add_task, view_tasks
from os_operations import make_directory
from calendar_usage import check_deadlines
from itertools_usage import generate_task_combinations
from completed_list import make_task_complete, completed_task
def main():
    print("""
1 - Write to file
2 - Read from file
3 - Make directory and show sample file path
4 - Show current date, day, year
5 - Show current month calendar
6 - Mark task as completed
7 - Show completed tasks
          
""")  
    choice = int(input("Enter your choice: "))
    dictionary = {
        1: add_task, 
        2: view_tasks,
        3: make_directory,
        4: check_deadlines,
        5: generate_task_combinations,
        6: make_task_complete,
        7: completed_task
    }

  
    if choice<=len(dictionary):
        dictionary[choice]()
    else:
        print("Invalid choice.")
if __name__ == "__main__":
  main()