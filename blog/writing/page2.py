import streamlit as st


def app():
    st.title('APP2')

    # markdown like this doesn't render when it's imported from separate file from main
    """
    ## This is blog page 2

    I wonder if the markdown will render
    """

    st.text('stuff')


def test():
    print("poop2")