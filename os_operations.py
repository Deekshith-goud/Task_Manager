import os

def make_directory():  # Renamed to match the dictionary key
    category = input("Enter task category (e.g., Urgent, Completed): ")
    base_dir = "tasks_directory"
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    category_dir = os.path.join(base_dir, category)
    if not os.path.exists(category_dir):
        os.mkdir(category_dir)
        print(f"Category '{category}' directory created.")
    else:
        print(f"Category '{category}' already exists.")
    filename = input("Enter filename to add to folder: ")
    file_path = os.path.join(category_dir, filename)  
    with open(file_path, 'w') as file:
        file.write("")  
    print(f"File '{filename}' created in '{category}' folder.")  
