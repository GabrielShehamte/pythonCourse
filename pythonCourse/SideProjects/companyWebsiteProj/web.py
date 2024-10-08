import streamlit as st


st.set_page_config(page_title="'Company Name'", layout='centered')

st.markdown()

col1, col2, col3 = st.columns(1,2,1)


with col1:
    st.image()
st.title("Company Name")
st.subheader("Company values or words to go by")

with col2:
    st.title()
    
    
    st.write("""Talk about products and services the company [rpvodes] provide
     ------Product 1 and the values or something
    """)
    
    st.write() #For every product write one of these and an image to help explain is
    
    
    