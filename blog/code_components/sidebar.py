from collections import OrderedDict
from os.path import dirname, basename, isfile, join
import glob
import streamlit as st

import home
import about
import test

PAGES_DICT = { 
    "Home": {
        "Home": home,
        "About": about,
    },
    "About": {
        "Home": home,
        "About": about,
    }
}

modules = glob.glob(join(dirname("blog/writing/"), "*.py"))
modules = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

def create_sidebar(pages_dict, file_names, title = "Navigation"):
    create_page_nav(pages_dict, title = title)
    create_writing_list(file_names)


def create_page_nav(pages_dict, title = "Navigation"):
    st.sidebar.title(title)
    def sidebar_callback():
        page_ref = pages_dict[st.session_state.current_page]
        st.write(st.session_state.current_page)
        page = page_ref[st.session_state.current_page]
        if st.session_state.current_page != "Home" and st.session_state.current_page != "About":
            page.app()
    st.sidebar.radio("Go to", list(pages_dict[st.session_state.current_page].keys()), on_change=sidebar_callback, key="current_page")


def create_writing_list(file_names):
    file_dict = OrderedDict()
    file_dict['-'] = None
    for file_name in file_names:
        mod = __import__("writing.%s" % (file_name), fromlist=["main"])
        file_dict[file_name] = mod
    my_page = st.sidebar.selectbox("Choose an article", list(file_dict.keys()), index=0)
    if my_page !=  "-":
       file_dict[my_page].app()
    elif st.session_state.current_page == "Home":
        home.app()
    elif st.session_state.current_page == "About":
        about.app()