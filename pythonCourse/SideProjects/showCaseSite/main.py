import streamlit as st


st.set_page_config(page_title="My ShowCase", layout = "wide")

# st.markdown("""
#             <style>
#             .contact-me {
#                 position: absolute;
#                 right: 20px;
#                 top: 20px;
#                 font-size: 18px;
#                 font-weight: bold;
#             }
#             </style>
#             <div class = "contact-me">
#             <a href="\contacts" target="\contacts">Contact Me</a>
#             </div>       
#             """, unsafe_allow_html=True)
# st.write("My Projects and tools")


col1, col2, col3 = st.columns([1,2,1])

with col1:
     st.image("Images/Image2.png", width=200)
    
st.title("Homepage")
st.subheader("Favourite Quote") # Replace the favourite quote with an actual quote.

with col2:
    st.title("Gabriel Shehamte")
    content = """

st.markdown("---")    
    
    """
    st.write("""Professionally, I aspire to work for a major tech firm like Google, Microsoft, or Apple,
             while building the foundations for my own consulting company in the tech industry. 
             My ultimate goal is to achieve financial freedom, enabling me to travel the world, 
             spend quality time with family and friends, and truly enjoy all that life has to offer.
             """)
   
    st.write("""I hold a degree in Management Engineering and am passionate about fitness,
            whether it's hitting the gym, playing basketball, or enjoying a game of football. 
            I love exploring and experiencing new cultures through traveling, it's always been a dream of mine 
            to be able to see the world, and I aim to leverage my career successs to allow me 
            to do so.         
             """)
    
    st.write("""
             I created this web app to showcase my skills but also allow others to interact with it, by
             implementing games, python packages, and code chunks anyone can implement into their company.
    """)

# with col3:
#     st.write("Contact Me")
    


cols = st.columns(4)

tools = [
    {"name":"Task Organizer",  "imageArea": "TaskOrganizer.png", "button_text": "Link/Source1"},
    {"name":"Portfolio Site",  "imageArea": "portfolioimage.png", "button_text": "Link/Source2"},
    {"name":"Games",  "imageArea": "Games.png", "button_text": "Link/Source3"},
    {"name":"PDF Generator",  "imageArea": "PDF_Generator_API.png", "button_text": "Link/Source4"}
]


for i, tool in enumerate(tools):
    with cols[i]:
        st.write(f"### {tool['name']}")
        st.image("images/" + f"{tool['imageArea']}")
        st.button(tool['button_text'])
        
        
st.write("Projects i'm working on:")

projects = [
    {"name": "NBA Predictor", "imageArea": "NBA_Analytics.png","button_text": "Link/Source5"},
    # {"name": "BurniX", "imageArea": "BurniX_Logo.png","button_text": "Link/Source5"}
    # {"name": "Project 2", "imageArea": "image6", "button_text": "Link/Source6"},
    # {"name": "Project 3", "imageArea": "image7", "button_text": "Link/Source7"}
]
    
proj_cols = st.columns(3)

for i, project in enumerate(projects):
    with proj_cols[i]:
        st.write(f"{project['name']}")
        st.image("images/" + f"{project['imageArea']}", width=200)
        st.button(project['button_text']) #Embed a website link into the button, might need an "a href"
        
        
        
# with tool_col1:
#     st.write("Task Organizer")
#     st.image()
#     st.button("Link/Source")
