# from functions import get_todos, write_todos
import functions
import time
i =0
tester = True


def todoList(userPrompt):
    global tester 

    if userPrompt.startswith('add') or userPrompt.startswith('a'):
        todo = input("Enter an input: ") + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif userPrompt== 'show'or userPrompt=='s':
        todos = functions.get_todos()
        if todos:
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1} - {item}"
                print(row)     
        else:
            print("List is empty")

    elif userPrompt =='update' or userPrompt=='u':
        try:
            number = int(input("Input the index of which 'Todo' to edit: ")) 
            numbRep = number -1# does not account for user knowing indexing

            todos = functions.get_todos()
            if 0 <= numbRep < len(todos):
                new_todo = input("Enter the new Todo: ") + "\n"
                todos[numbRep] = new_todo
                functions.write_todos(todos)
            else:
                print("Invalid index. Task does not exist.")
        except ValueError:
            print("Invalid input. Please eneter a number")

    elif userPrompt == 'complete' or userPrompt =='c':
        number = int(input("which task would you like to complete? "))
        index = number - 1
        todos = functions.get_todos()
        if 0<= index <len(todos):
            todos.pop(index) #to account for indexing
            functions.write_todos(todos)
            print("Task completed")
        else:
            print("Invalid number. ")

    elif userPrompt == 'exit' or userPrompt=='e':
        tester = False
        print("Goodbye")
    else :
        print("invalid input, please try again"+ "\n")        
        


now = time.strftime("%B %d, %Y -  %I:%M%p")    
print("It is ", now)
while tester:
    userPrompt = input("Type 'add', 'show', 'update','complete', 'exit' " )
    userPrompt = userPrompt.strip().lower() # just fixes capitalization error by user
    todoList(userPrompt)








