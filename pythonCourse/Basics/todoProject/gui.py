import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a To-Do")
input_box = FSG.InputText(tooltip="Enter todo", key = 'todo')
add_button = FSG.Button("Add")
window = FSG.Window("My To-Do App",
                    layout=[[label, input_box],[add_button]], 
                    font = ('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
    elif event == FSG.WIN_CLOSED:
        break
window.close()
