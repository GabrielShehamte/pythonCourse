import FreeSimpleGUI as sg
from converters import convert

label_feet = sg.Text("Enter feet")
label_inches = sg.Text("Enter inches")

input_box = sg.Input()
input_box2 = sg.Input()





button = sg.Button("Convert")
window = sg.Window("Converter",layout=[[label_feet, input_box],[label_inches, input_box2],[button, label_conversion]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    
    result = convert(feet, inches)
    window["output"].update(values = f"{result} m")
window.close()

