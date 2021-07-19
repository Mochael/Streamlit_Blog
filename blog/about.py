import streamlit as st


def app():
    st.title('About')

    st.markdown('## We are the smartest human beings who ever lived, and we have come to deliver you salvation from your stupidity.')

    # st.sidebar.title('Navigation')
    # selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    # page = PAGES[selection]
    # if page is not None:
    #     page.app()
    # else:
    #     app()