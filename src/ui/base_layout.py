import streamlit as st

def style_background_home():
    st.markdown("""
    <style>
        .stApp{
        background: linear-gradient(to right, #ff9472, #f2709c) !important; /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
         }
        .stApp div[data-testid="stColumn"]{
        background-color:#FFB6C1 !important;
        padding:2.5rem !important;
        border-radius:5rem !important;        
        }
    </style>
""",unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
    <style>
        .stApp{
        background: #E0E3FF  !important; 
         }
    </style>
""",unsafe_allow_html=True)


def style_base_layout():
    ##color
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Top bar of streamlit */
        
        #MainMenu,footer,header{
        visibility:hidden}
        
        /* Remove extra space from top */
        .block-container{
        padding-top:1.5rem !important;
        }
        /* Header */
        h1{
        font-family:'Climate Crisis',sans-serif !important;
        font-size:4rem !important;
        line-height:1.1 !important;
        margin-bottom:0rem !important;
        
        }

        h2{
        font-family:'Climate Crisis',sans-serif !important;
        font-size:2rem !important;
        line-height:0.9 !important;
        margin-bottom:0rem !important;
        
        }

        h3,h4,p{
        font-family: 'Outfit',sans-serif;
        }

        /* Buttons */
        button{
        border-radius: 1.5rem !important;
        background-color:#5865F2  !important;
        color: white !important;
        padding: 10px 20px !important
        border:none !important;
        transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"]{
        border-radius: 1.5rem !important;
        background-color: #EB459E !important;
        color: white !important;
        padding: 10px 20px !important
        border:none !important;
        transition: transform 0.25s ease-in-out !important;
        }
        
        button[kind="tertiary"]{
        border-radius: 1.5rem !important;
        background-color:black!important;
        color: white !important;
        padding: 10px 20px !important
        border:none !important;
        transition: transform 0.25s ease-in-out !important;
        }

        button:hover{
        transform: scale(1.1)}
    </style>
""",unsafe_allow_html=True)