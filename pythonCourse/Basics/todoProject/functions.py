def get_todos(filepath = "todos.txt"):
    try:
        with open(filepath,'r') as file:
            todos = file.readlines()
    except FileNotFoundError:
        todos = []
    return todos
    
def write_todos(todos_arg, filepath = 'todos.txt'):
    with open(filepath,'w') as file:
        todos = file.writelines(todos_arg)
