import streamlit as st
from streamlit import session_state

import mods as mods

todos = mods.get_todos()


st.title("Todo App✔️")
st.text("check to remove todos...")

def add_todo():
    new_todo = st.session_state['new-todo']
    todos.append(new_todo + '\n')
    mods.write_todos(todos)
    # if not todos.__contains__(new_todo):
    #     todos.append(new_todo + '\n')
    #     mods.write_todos(todos)
    # else:
    #     "theis todo already exists"
for todo in todos:
    st.checkbox(todo , key=todo)

st.text_input(label="",placeholder="Enter a todo" , on_change=add_todo , key="new-todo")

for session in st.session_state:
    if st.session_state[session]:
        todos.remove(session)
        st.session_state.pop(session)
        mods.write_todos(todos)
        st.rerun()


