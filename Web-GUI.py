import streamlit as st
from Modules import Todo_Functions


todos = Todo_Functions.get_todos()

st.title("My Todo App")
st.subheader("Welcome to your Web Based To do app!")
#st.write("hello funded trader!")


for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="", placeholder="Enter a Todo!", label_visibility="hidden")




