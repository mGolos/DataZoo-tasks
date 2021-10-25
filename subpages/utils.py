import streamlit as st


def st_query_radio(label, param, options, key=None):
    key = f"st_query_radio.{key or param}"

    choice = st.experimental_get_query_params().get(param, ("",))[0]
    choice = choice.replace("-", " ").title()

    def on_change():
        params = st.experimental_get_query_params()
        params[param] = st.session_state[key].replace(" ", "-").lower()

        st.experimental_set_query_params(**params)

    st.session_state[key] = choice if choice in options else next(iter(options))
    other_name = lambda e: options[e][0]
    st.sidebar.radio(label, tuple(options.keys()), on_change=on_change, key=key, format_func=other_name)
    
    return options[st.session_state[key]][1]