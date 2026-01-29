import json

TODO_FILE = "todos.json"

def mark_done():
    todos = load_todos()
    list_todos()
    task_num = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_num < len(todos):
        todos[task_num]["done"] = True
        save_todos(todos)
        print("Task marked as done!")
    else:
        print("Invalid task number.")
def main():
    while True:
        print("\n1. Add Task")
        print("\n2. List Tasks")
        print("\n3. Mark Task as Done")
        print("\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_todo()
        elif choice == '2':
            list_todos()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
def list_todos():
    todos = load_todos()
    for index, todo in enumerate(todos):
        status = "Done" if todo["done"] else "Not done"
        print(f"{index + 1}. {todo['task']} - {status}")
def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file)
def load_todos():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def add_todo():
    todos = load_todos()
    task = input("Enter a new task: ")
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print("Task added!")

if __name__ == "__main__":
    main()
