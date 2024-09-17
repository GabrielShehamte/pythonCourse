import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a To-Do")
input_box = FSG.InputText(tooltip="Enter todo", key = 'todo')
add_button = FSG.Button("Add")
list_box = FSG.Listbox(values=functions.get_todos(), 
                       key='todos', enable_events=True, size=[45, 10])
edit_button = FSG.Button("Edit")
window = FSG.Window("My To-Do App",
                    layout=[[label, input_box],[add_button], [list_box, edit_button]],
                    font = ('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    
    if event == "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].strip()
            if new_todo:
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            
    elif event == "Edit":
        todo_edit = values['todos'][0]
        new_todo = values['todo']
        todos = functions.get_todos()
        index = todos.index(todo_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values = todos)
        
    elif event =='todos':
        window['todo'].update(value = values['todos'][0])
        # new_todo = input(Input the new todo)
    
    elif event == FSG.WIN_CLOSED:
        break

window.close()
