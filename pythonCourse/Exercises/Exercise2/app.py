import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet")
label_inches = sg.Text("Enter inches")

input_box = sg.Input()
input_box2 = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Converter",layout=[[label_feet, input_box],[label_inches, input_box2],[button]])

window.read()
window.close()