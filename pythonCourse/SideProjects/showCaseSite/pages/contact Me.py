import streamlit as st

st.header("Contact Me")
with st.form(key = "emailForm"):
    userName = st.text_input(label='Name')
    userEmail = st.text_input(label="Email")
    message = st.text_area(label='message')
    button = st.form_submit_button(label='Submit')
    # if button :
        # message = message + userEmail
        
    