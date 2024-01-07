import streamlit as st
import pandas as pd
import urllib.request
import requests
import threading
import json
import random
from streamlit_option_menu import option_menu

def MonitoringConstructor():

    st.write("Select the Farm")
    option2 = option_menu(None, ["Pak choy", "Rice", "Aqua"],
                                  menu_icon="forward", default_index=0, orientation="horizontal",
                                  styles={
                                      "container": {"padding": "0!important", "background-color": "#fafafa"},
                                      "icon": {"color": "orange", "font-size": "15px"},
                                      "nav-link": {"font-size": "15px", "text-align": "right", "margin": "0px",
                                                   "--hover-color": "#eee", },
                                      "nav-link-selected": {"background-color": "green"},
                                  }
                                  )

    import requests

    # Function to fetch data for a specific field
    def get_field_data(field_number):
        URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
        KEY = 'YOUR_API_KEY'
        NEW_URL = URL + KEY

        get_data = requests.get(NEW_URL).json()
        channel_id = get_data['channel']['id']
        field_data = get_data['feeds']

        # Extracting values for the specified field
        values = [field_data[1][f'field{field_number}']]

        return values

    # Fetching data for all fields (field1 to field5)
    all_data = {f'Field {i}': get_field_data(i) for i in range(1, 6)}
    print(all_data)

    # Creating a DataFrame for all data
    import pandas as pd
    df = pd.DataFrame(all_data)

    # Displaying the DataFrame with minimum values for each entry
    st.write("Real Values:")
    st.table(df)



