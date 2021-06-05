import page1
import page2
import streamlit as st

PAGES = {
    "Home": None,
    "Page1": page1,
    "Page2": page2
}

def app():
    st.title('Home')
    """
    # Here is the Intro Page

    Welcome and we hope you enjoy
    """

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
if page is not None:
    page.app()
else:
    app()