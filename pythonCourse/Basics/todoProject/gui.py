import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Tyoe in a To-Do")
input_box = FSG.InputText(tooltip="Enter todo")
add_button = FSG.Button("Add")
window = FSG.Window("My To-Do App",layout=[[label, input_box],[add_button]])
window.read()
window.close()
