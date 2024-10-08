import streamlit as st
from sendEmail import sendEmail

st.header("Contact Me")
with st.form(key = "emailForm"):
    userName = st.text_input("Name")
    userEmail = st.text_input("Email Address")
    message = st.text_area("Message")
    message = message + userEmail
    button = st.form_submit_button(label='Submit')
    if button :
        # message = message + userEmail
        sendEmail(message)
        st.info("Email was sent succesfully")
        
        
    