FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    try:
        with open(filepath,'r') as file:
            todos = file.readlines()
            todos = [todo.strip() for todo in todos if todo.strip()]
    except FileNotFoundError:
        todos = []
    print("Debug - Read todos:", todos)
    return todos
    
def write_todos(todos_arg, filepath = FILEPATH):
    with open(filepath,'w') as file:
        todos_newlines = [todo + "\n" for todo in todos_arg]
        file.writelines(todos_newlines)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())