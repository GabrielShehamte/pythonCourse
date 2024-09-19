import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write(" This app is to increase your productivity.")

for index, todo in enumerate(todos):
    todo_text = todo.strip()
    checkbox = st.checkbox(todo, key =todo)
    if checkbox:
        st.session_state.confirm_todo = (todo_text, index)
        st.warning(f"Please confirm you completed: {st.session_state.confirm_todo}")
        
        confirm = st.button("Confirm")
        cancel = st.button("Cancel")
        
        if (st.session_state.confirm_todo) and (confirm):
            todos.pop(st.session_state.confirm_todo[1])
            # todos.remove(st.session_state.confirm_todo + "\n")
            functions.write_todos(todos)
            
            st.session_state.confirm_todo = None
            st.experimental_rerun()
        
        if cancel:
            del st.session_state[st.session_state.confirm_todo[0]]
            # del st.session_state[st.session_state.confirm_todo]
            st.session_state.confirm_todo = None
            st.experimental_rerun()
        
    
    
st.text_input(label="",placeholder="Add new Tasks...",
              on_change=add_todo, key='new_todo')
