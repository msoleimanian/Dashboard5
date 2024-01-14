import streamlit as st
import pandas as pd
import urllib.request
import requests
import threading
import json
import random
import plotly.express as px
import time
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import requests
import json

def get_field_data(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    print(field_data[len(field_data)-1]['created_at'])
    # Extracting values for the specified field
    values = [field_data[1][f'field{field_number}']]
    time = field_data[len(field_data)-1]['created_at']
    return values


def get_field_datas(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    time=[]
    val=[]
    df = pd.DataFrame()
    for data in field_data:
        time.append(data['created_at'])
        val.append(data[f'field{field_number}'])

    df['time'] = time
    df['value'] = val
    print(field_data)
    # Extracting values for the specified field
    return df

def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """

def printCostumTitleAndContenth2(title, context):
    return f"""
        <div class="jumbotron">
        <h2>{title}</h2>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleAndContenth1(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <h5>{context}</h5>
        </div>
        <div class="container">
        </div>
        """

def getPakChoyData(nutreint):


    url = "https://api.satu.singularityaero.tech/api/telemetries"

    payload = json.dumps({
        "deviceUniqueId": "UPMSO2001",
        "telemetryTypeCode": nutreint,
        "dateStart": "2023-10-10 21:50:39"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 25|iEjCopmkc73ZFYtCzHCFLnCJb670ErvV3VBfGCt2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    print("$$$$$$$$$$$$$$$$$$$")
    print(data)
    time = []
    val = []
    dataframe = pd.DataFrame()

    for d in data['data']:
        val.append(d['value'])
        time.append(d['readingAt'])

    dataframe['time'] = time
    dataframe['value'] = val
    print("$$$$$$$$$$$$$$$$$$$")
    return dataframe


def get_field_data(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    print(field_data[len(field_data)-1]['created_at'])
    # Extracting values for the specified field
    values = [field_data[1][f'field{field_number}']]
    time = field_data[len(field_data)-1]['created_at']
    return values


def get_field_datas(field_number):
    URL = f'https://api.thingspeak.com/channels/1649792/fields/{field_number}.json?api_key='
    KEY = 'YOUR_API_KEY'
    NEW_URL = URL + KEY

    get_data = requests.get(NEW_URL).json()
    channel_id = get_data['channel']['id']
    field_data = get_data['feeds']
    time=[]
    val=[]
    df = pd.DataFrame()
    for data in field_data:
        time.append(data['created_at'])
        val.append(data[f'field{field_number}'])

    df['time'] = time
    df['value'] = val
    print(field_data)
    # Extracting values for the specified field
    return df

def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """

def printCostumTitleAndContenth2(title, context):
    return f"""
        <div class="jumbotron">
        <h2>{title}</h2>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleAndContenth1(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <h5>{context}</h5>
        </div>
        <div class="container">
        </div>
        """

def getPakChoyData(nutreint):


    url = "https://api.satu.singularityaero.tech/api/telemetries"

    payload = json.dumps({
        "deviceUniqueId": "UPMSO2001",
        "telemetryTypeCode": nutreint,
        "dateStart": "2023-10-10 21:50:39"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 25|iEjCopmkc73ZFYtCzHCFLnCJb670ErvV3VBfGCt2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    time = []
    val = []
    dataframe = pd.DataFrame()

    for d in data['data']:
        val.append(d['value'])
        time.append(d['readingAt'])

    dataframe['time'] = time
    dataframe['value'] = val
    print("$$$$$$$$$$$$$$$$")
    print(dataframe)
    print("$$$$$$$$$$$$$$$$")
    return dataframe


def getPakChoyDatas(nutreint):


    url = "https://api.satu.singularityaero.tech/api/telemetries"

    payload = json.dumps({
        "deviceUniqueId": "UPMSO2001",
        "telemetryTypeCode": "Temperature",
        "dateStart": "2023-10-10 21:50:39"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 25|iEjCopmkc73ZFYtCzHCFLnCJb670ErvV3VBfGCt2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    return data



def MonitoringConstructor():
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





    if option2 == "Aqua":


        fieldname = {'Field 1' : 'Temperature' ,'Field 2' : 'pH', 'Field 3' : 'Ammonia','Field 4' : 'DO', 'Field 5':'Salinity'}
        all_data = {fieldname[f'Field {i}']: get_field_data(i) for i in range(1, 6)}
        print(all_data)
        print(float(all_data['pH'][0]))


        #---------------------------------------------------------------------------------

        import plotly.graph_objects as go

        fig_ph = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['pH'][0]),
            mode="gauge+number+delta",
            title={'text': "pH"},
            delta={'reference': 7 , },
            gauge={'axis': {'range': [None, 14] ,},
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                   {'range': [8.5, 9], 'color': "orange"},
                   {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_temp = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['Temperature'][0]),
            mode="gauge+number+delta",
            title={'text': "Temperature"},
            delta={'reference': 30, },
            gauge={'axis': {'range': [None, 40], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 22], 'color': "red"},
                       {'range': [22, 26], 'color': "orange"},
                       {'range': [26, 32], 'color': "green"},
                       {'range': [32, 35], 'color': "orange"},
                       {'range': [35, 40], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_Amo = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['Ammonia'][0]),
            mode="gauge+number+delta",
            title={'text': "Ammonia"},
            delta={'reference': 0.5, },
            gauge={'axis': {'range': [None, 0.12], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 0.05], 'color': "red"},
                       {'range': [0.05, 0.06], 'color': "orange"},
                       {'range': [0.06, 0.08], 'color': "green"},
                       {'range': [0.08, 1.2], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_Do = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['DO'][0]),
            mode="gauge+number+delta",
            title={'text': "Do"},
            delta={'reference': 9, },
            gauge={'axis': {'range': [None, 20], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 4], 'color': "red"},
                       {'range': [4, 9], 'color': "orange"},
                       {'range': [9, 20], 'color': "green"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_Salinity = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['Salinity'][0]),
            mode="gauge+number+delta",
            title={'text': "Salinity"},
            delta={'reference': 20, },
            gauge={'axis': {'range': [None, 40], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 20], 'color': "orange"},
                       {'range': [20, 35], 'color': "green"},
                       {'range': [35, 37], 'color': "orange"},
                       {'range': [37, 40], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        URL = f'https://api.thingspeak.com/channels/1649792/fields/1.json?api_key='
        KEY = 'YOUR_API_KEY'
        NEW_URL = URL + KEY

        get_data = requests.get(NEW_URL).json()
        channel_id = get_data['channel']['id']
        field_data = get_data['feeds']
        print(field_data[len(field_data) - 1]['created_at'])


        html_content = f"""
                                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                    <h3 style="color:#333333;">Real-Time Monitoring</h3>
                                                    <p>You can see the level of the nutrients at {field_data[len(field_data) - 1]['created_at']}</p>
                                                </div>
                                            """
        st.markdown(html_content, unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.plotly_chart(fig_ph,use_container_width=True , height = 500)
        with col2:
            st.plotly_chart(fig_temp,use_container_width=True)
        with col3:
            st.plotly_chart(fig_Amo,use_container_width=True ,height=20)
        with col4:
            st.plotly_chart(fig_Do,use_container_width=True ,height=20)
        with col5:
            st.plotly_chart(fig_Salinity,use_container_width=True ,height=20)
        options = st.selectbox(
            'Select the option',
            ('Temperature', 'pH', 'Ammonia', 'DO','Salinity'))

        fieldname2 = { 'Temperature':1, 'pH':2, 'Ammonia' :3 ,'DO':4, 'Salinity':5}
        print(get_field_datas(fieldname2[options]))
        df = get_field_datas(fieldname2[options])
        p = px.line(df, x='time', y='value', title='Salinity Trend')
        st.plotly_chart(p)

    if option2 == "Pak choy":
        data = getPakChoyData('waterPh')

        import plotly.graph_objects as go

        fig_ph = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "pH"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterEc')
        fig_ec = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "EC"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterSr')
        fig_sr = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Sr"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterOrp')
        fig_orp = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Orp"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterTds')
        fig_tds = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "TDS"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterSalinity')
        fig_Salinity = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Salinity"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterTemperature')
        fig_Temperature = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data["data"][0]["value"]),
            mode="gauge+number+delta",
            title={'text': "Temperature"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))


        html_content = f"""
                                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                            <h3 style="color:#333333;">Real-Time Monitoring</h3>
                                                            <p>You can see the level of the nutrients at {data["data"][0]["readingAt"]}</p>
                                                        </div>
                                                    """
        st.markdown(html_content, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.plotly_chart(fig_ph, use_container_width=True, height=500)
        with col2:
            st.plotly_chart(fig_ec, use_container_width=True, height=500)
        with col3:
            st.plotly_chart(fig_sr, use_container_width=True, height=500)
        with col4:
            st.plotly_chart(fig_orp, use_container_width=True, height=500)
        with col5:
            st.plotly_chart(fig_tds, use_container_width=True, height=500)
        with col6:
            st.plotly_chart(fig_Salinity, use_container_width=True, height=500)
        with col7:
            st.plotly_chart(fig_Temperature, use_container_width=True, height=500)

        options = st.selectbox(
            'Select the option',
            ('Temperature', 'pH', 'Sr', 'Orp', 'Tds', 'Salinity'))
        df = getPakChoyDatas(options)
        print(df)



def getPakChoyDatas(nutreint):


    url = "https://api.satu.singularityaero.tech/api/telemetries"

    payload = json.dumps({
        "deviceUniqueId": "UPMSO2001",
        "telemetryTypeCode": "Temperature",
        "dateStart": "2023-10-10 21:50:39"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 25|iEjCopmkc73ZFYtCzHCFLnCJb670ErvV3VBfGCt2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    return data



def MonitoringConstructor():
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





    if option2 == "Aqua":


        fieldname = {'Field 1' : 'Temperature' ,'Field 2' : 'pH', 'Field 3' : 'Ammonia','Field 4' : 'DO', 'Field 5':'Salinity'}
        all_data = {fieldname[f'Field {i}']: get_field_data(i) for i in range(1, 6)}
        print(all_data)
        print(float(all_data['pH'][0]))


        #---------------------------------------------------------------------------------

        import plotly.graph_objects as go

        fig_ph = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['pH'][0]),
            mode="gauge+number+delta",
            title={'text': "pH"},
            delta={'reference': 7 , },
            gauge={'axis': {'range': [None, 14] ,},
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                   {'range': [8.5, 9], 'color': "orange"},
                   {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_temp = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['Temperature'][0]),
            mode="gauge+number+delta",
            title={'text': "Temperature"},
            delta={'reference': 30, },
            gauge={'axis': {'range': [None, 40], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 22], 'color': "red"},
                       {'range': [22, 26], 'color': "orange"},
                       {'range': [26, 32], 'color': "green"},
                       {'range': [32, 35], 'color': "orange"},
                       {'range': [35, 40], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_Amo = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['Ammonia'][0]),
            mode="gauge+number+delta",
            title={'text': "Ammonia"},
            delta={'reference': 0.5, },
            gauge={'axis': {'range': [None, 0.12], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 0.05], 'color': "red"},
                       {'range': [0.05, 0.06], 'color': "orange"},
                       {'range': [0.06, 0.08], 'color': "green"},
                       {'range': [0.08, 1.2], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_Do = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['DO'][0]),
            mode="gauge+number+delta",
            title={'text': "Do"},
            delta={'reference': 9, },
            gauge={'axis': {'range': [None, 20], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 4], 'color': "red"},
                       {'range': [4, 9], 'color': "orange"},
                       {'range': [9, 20], 'color': "green"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        fig_Salinity = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(all_data['Salinity'][0]),
            mode="gauge+number+delta",
            title={'text': "Salinity"},
            delta={'reference': 20, },
            gauge={'axis': {'range': [None, 40], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 20], 'color': "orange"},
                       {'range': [20, 35], 'color': "green"},
                       {'range': [35, 37], 'color': "orange"},
                       {'range': [37, 40], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        URL = f'https://api.thingspeak.com/channels/1649792/fields/1.json?api_key='
        KEY = 'YOUR_API_KEY'
        NEW_URL = URL + KEY

        get_data = requests.get(NEW_URL).json()
        channel_id = get_data['channel']['id']
        field_data = get_data['feeds']
        print(field_data[len(field_data) - 1]['created_at'])


        html_content = f"""
                                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                    <h3 style="color:#333333;">Real-Time Monitoring</h3>
                                                    <p>You can see the level of the nutrients at {field_data[len(field_data) - 1]['created_at']}</p>
                                                </div>
                                            """
        st.markdown(html_content, unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.plotly_chart(fig_ph,use_container_width=True , height = 500)
        with col2:
            st.plotly_chart(fig_temp,use_container_width=True)
        with col3:
            st.plotly_chart(fig_Amo,use_container_width=True ,height=20)
        with col4:
            st.plotly_chart(fig_Do,use_container_width=True ,height=20)
        with col5:
            st.plotly_chart(fig_Salinity,use_container_width=True ,height=20)
        options = st.selectbox(
            'Select the option',
            ('Temperature', 'pH', 'Ammonia', 'DO','Salinity'))

        fieldname2 = { 'Temperature':1, 'pH':2, 'Ammonia' :3 ,'DO':4, 'Salinity':5}
        print(get_field_datas(fieldname2[options]))
        df = get_field_datas(fieldname2[options])
        p = px.line(df, x='time', y='value', title=options)
        st.plotly_chart(p)

    if option2 == "Pak choy":
        data = getPakChoyData('waterPh')

        import plotly.graph_objects as go

        fig_ph = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data.iloc[0]['value']),
            mode="gauge+number+delta",
            title={'text': "pH"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterEc')
        fig_ec = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data.iloc[0]['value']),
            mode="gauge+number+delta",
            title={'text': "EC"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterSr')
        fig_sr = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data.iloc[0]['value']),
            mode="gauge+number+delta",
            title={'text': "Sr"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterOrp')
        fig_orp = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data.iloc[0]['value']),
            mode="gauge+number+delta",
            title={'text': "Orp"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterTds')
        fig_tds = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data.iloc[0]['value']),
            mode="gauge+number+delta",
            title={'text': "TDS"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterSalinity')
        fig_Salinity = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data.iloc[0]['value']),
            mode="gauge+number+delta",
            title={'text': "Salinity"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        data = getPakChoyData('waterTemperature')
        fig_Temperature = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=float(data.iloc[0]['value']),
            mode="gauge+number+delta",
            title={'text': "Temperature"},
            delta={'reference': 7, },
            gauge={'axis': {'range': [None, 14], },
                   'bar': {'color': "black"},
                   'steps': [
                       {'range': [0, 5], 'color': "red"},
                       {'range': [5, 6], 'color': "orange"},
                       {'range': [6, 8.5], 'color': "green"},
                       {'range': [8.5, 9], 'color': "orange"},
                       {'range': [9, 14], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))


        html_content = f"""
                                        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                            <h3 style="color:#333333;">Real-Time Monitoring</h3>
                                                            <p>You can see the level of the nutrients at {data.iloc[0]['time']}</p>
                                                        </div>
                                                    """
        st.markdown(html_content, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.plotly_chart(fig_ph, use_container_width=True, height=500)
        with col2:
            st.plotly_chart(fig_ec, use_container_width=True, height=500)
        with col3:
            st.plotly_chart(fig_sr, use_container_width=True, height=500)
        with col4:
            st.plotly_chart(fig_orp, use_container_width=True, height=500)
        with col5:
            st.plotly_chart(fig_tds, use_container_width=True, height=500)
        with col6:
            st.plotly_chart(fig_Salinity, use_container_width=True, height=500)
        with col7:
            st.plotly_chart(fig_Temperature, use_container_width=True, height=500)

        options = st.selectbox(
            'Select the option',
            ('waterTemperature', 'waterPh', 'waterSr', 'waterOrp', 'waterTds', 'waterSalinity'))
        df = getPakChoyData(options)
        print(df)
        p = px.line(df, x='time', y='value', title=options)
        st.plotly_chart(p)