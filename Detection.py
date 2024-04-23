import streamlit as st
import os

import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import pandas as pd
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_download_link(file_path):
    """Generate a download link for the file."""
    return f'<a href="{file_path}" download>Click here to download the file</a>'

def Detection_constructor():
    st.header('Weed Detection')
    import pandas as pd
    from io import StringIO

    uploaded_files = st.file_uploader("Choose file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            # Create a folder to store the uploaded data if it doesn't exist
            if not os.path.exists("uploaded_data"):
                os.makedirs("uploaded_data")

            # Save the uploaded file to the folder
            file_path = os.path.join("uploaded_data", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.success("File uploaded successfully!")

            # Display the path to the uploaded file
            st.write("File path:", file_path)

            # Display a download link for the uploaded file
            st.markdown(get_download_link(file_path), unsafe_allow_html=True)






