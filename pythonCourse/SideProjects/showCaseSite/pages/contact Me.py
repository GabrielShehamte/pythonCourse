import streamlit as st
from sendEmail import sendEmail

st.header("Contact Me")
with st.form(key = "emailForm"):
    userName = st.text_input("Name")
    userEmail = st.text_input("Email Address")
    topic = st.selectbox("From what perspective are you viewing this site?", 
                         ("Select an Option","Recruiter", "Student", "Employer", "None of the Above"), )
    rawMessage = st.text_area("Message")
    message = f"""\
Subject: New email from {userName}, from position of {topic}
From: {userEmail}
{rawMessage}
"""

    button = st.form_submit_button(label='Submit')
    if button :
        # message = message + userEmail
        sendEmail(message)
        st.info("Email was sent succesfully")
        
        
    