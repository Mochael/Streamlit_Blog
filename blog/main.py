import streamlit as st

from code_components.sidebar import create_sidebar, PAGES_DICT, modules


def app():
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Home"
        st.session_state.writing_page = None

app()
create_sidebar(PAGES_DICT, modules, title = "Navigation")

# Hides the made with streamlit text
hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)