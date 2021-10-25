import streamlit as st
import subpages


if __name__ == '__main__':
    st.set_page_config(
        page_title="DataZoo Tasks",
        initial_sidebar_state="expanded",
        )
    st.sidebar.image('files/logo.png')
    st.markdown("<style>.css-ng1t4o {padding: 1rem 1rem;} .css-12oz5g7 {padding: 1rem 1rem;}</style>", unsafe_allow_html=True)

    
    subpages.utils.st_query_radio("Menu", "page", {
        "Chessboard": ('Task1 Chessboard', subpages.chessboard),
        'Today': ("Task2 Today", subpages.today),
        'Audit': ("Task2 History", subpages.history),
    })()