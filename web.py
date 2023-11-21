import streamlit as st
from addfun import read, write

todos = read()


def add_item():
    todo = st.session_state['to-do'] + '\n'
    todos.append(todo)
    write(todos)


st.title("tanu app")
st.subheader('this is my first app')
st.write('this app increase my productivity')
st.checkbox('tanu ass')
for index,todo in enumerate(todos):
    x = st.checkbox(todo, key=todo)
    if x :
        todos.pop(index)
        write(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='add item', placeholder='enter item to add in the list', on_change=add_item, key='to-do')

