import streamlit as st


# """
# pages_dict: dictionary 
# {
#     "Home": {
#         "Home": main,
#         "About": about,
#     },
#     "Writing": {
#         "Home": main,
#         "Page1": page1,
#         "Page2": page2,
#     },

# }
# """
# def create_sidebar(pages_dict, title="Navigation"):
#     st.sidebar.title(title)
#     new_page = st.sidebar.radio("Go to", list(pages_dict[st.session_state.current_page].keys()))
#     page = pages_dict[st.session_state.current_page][new_page]
#     st.session_state.current_page = new_page
#     # Go to new page
#     page.app()



def create_sidebar(pages_dict, title = "Navigation"):
    st.sidebar.title(title)
    def sidebar_callback():
        page_ref = pages_dict[st.session_state.current_page]
        st.write(st.session_state.current_page)
        page = page_ref[st.session_state.current_page]
        print(page)
        print(__name__)
        if page != "home":
            page.app()

    new_page = st.sidebar.radio("Go to", list(pages_dict[st.session_state.current_page].keys()), on_change=sidebar_callback, key="current_page")
