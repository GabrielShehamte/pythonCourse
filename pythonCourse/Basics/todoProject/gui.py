import functions
import FreeSimpleGUI as FSG


FSG.theme('DarkGrey9')

label = FSG.Text("Type in a To-Do")
input_box = FSG.InputText(tooltip="Enter todo", key = 'todo')
add_button = FSG.Button("Add")

list_box = FSG.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45, 10])

edit_button = FSG.Button("Edit")
complete_button = FSG.Button("Complete")
exit_button = FSG.Button("Exit")

window = FSG.Window("My To-Do App",
                    layout=[[label, input_box],[add_button], [list_box, edit_button], 
                            [complete_button, exit_button]],
                    font = ('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    
    if event == FSG.WIN_CLOSED or event == "Exit":
        print("Goodbye!!")
        break
    
    if event == "Add":
            new_todo = values['todo'].strip()
            if new_todo:
                todos = functions.get_todos()
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            
    elif event == "Edit":
        try:
            selected_todo = values['todos'][0]
            new_todo = values['todo'].strip()
            if new_todo:
                todos = functions.get_todos()
                index = todos.index(selected_todo)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            else:
                FSG.popup_error("Please enter the edits.")
        except IndexError:
            FSG.popup_error("Please selecte a task to edit.")
                        
    elif event == "Complete":
        try:
            
            todo_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_complete)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        except IndexError:
            FSG.popup("Please select a task to complete.")
            
            
        
    elif event =='todos':
        if values['todos']:
            window['todo'].update(value = values['todos'][0])
        # new_todo = input(Input the new todo)
        # print()
    
window.close()
