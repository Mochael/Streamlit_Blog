import home
import about
import streamlit as st

from code_components.sidebar import create_sidebar

PAGES_DICT = { 
    "Home": {
        "Home": home,
        "About": about
    },
    "About": {
        "Home": home,
        "About": about,
    }
}


def app():
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Home"
        home.app()

app()
create_sidebar(PAGES_DICT, title = "Navigation")