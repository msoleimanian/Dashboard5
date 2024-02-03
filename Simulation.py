import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import pandas as pd
import time

import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """


def printWithTitleAndBoarder(title, context):
    return f"""
        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h4 style="color:#333333;">{title}</h4>
            <table>
                    <tr>
                        <th>Status</th>
                        <th>Score(10)</th>
                        <th>Risk Level</th>
                    </tr>
                    <tr>
                        <td style="color : red;">good</td>
                        <td style="color : red;">4</td>
                        <td style="color : red;">High Risk</td>
                    </tr>
            </table>
            <h4 style="color:#333333;">Health Status of the Pots</h4>
            <table>
                    <tr>
                        <th>Pot Number</th>
                        <th>Predicted Crop Health Status</th>
                        <th>Yeild Report</th>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td style="color : red;">bad</td>
                        <td style="color : red;">Predicted Average Weight for Generation 3 at Week4: 670 gram (% 39.09 lower than the best, Best weight grain is 1100 gram.)</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td style="color : red;">bad</td>
                        <td style="color : red;">Predicted Average Weight for GenerationGeneration 3 at Week4: 690 gram (% 37.27 lower than the best, Best weight grain is 1100 gram.)</td>
                    </tr>
            </table>
        </div>
        """


def cardCreator(title, value):
    html_code = """
    <html>
        <style>
            .status-card {
                background-color: #c1f0c1; /* Light green color */
                padding: 20px;
                border-radius: 50%; /* Make it circular */
                width: 170px; /* Set a fixed width for the circular card */
                height: 170px; /* Set a fixed height for the circular card */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
        </style>"""

    html_code = html_code + f"""<div class='status-card'>
            <h5>{title}</h5>
            <p> {value} </p>
        </div>
        </html>
    """
    st.markdown(html_code, unsafe_allow_html=True)


def animated_gauge_progress_bar(value, title, rmin, rmax):
    if 1 <= value <= 10:
        bar_color = "red"
    else:
        bar_color = "#4CAF50"  # Default color for other values

    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{'type': 'indicator'}]]
    )
    fig.add_trace(go.Indicator(
        mode="number+gauge",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 50, 'position': 'top'},
        gauge=dict(
            axis=dict(range=[rmin, rmax]),
            bar=dict(color='black'),  # Set color dynamically
            bgcolor="white",
            borderwidth=2,
            bordercolor="gray",
            steps=[dict(range=[0, 100], color="lightgray")]
        ),
        title=dict(text=title, font=dict(size=20)),  # Set title directly within the trace
    ))

    fig.update_layout(
        height=200,
        margin=dict(l=15, r=15, b=15, t=60),
    )

    return fig


def guageCreator(vlaue, title, rmin, rmax):
    # Streamlit app
    chart_placeholder = st.empty()
    vla = round(vlaue)
    if vla <= 1:
        animated_chart = animated_gauge_progress_bar(vlaue, title, rmin, rmax)
        chart_placeholder.plotly_chart(animated_chart, use_container_width=True)
    # Update the progress value with an animation
    else:
        for value in range(0, vla, 1):
            animated_chart = animated_gauge_progress_bar(value, title, rmin, rmax)
            chart_placeholder.plotly_chart(animated_chart, use_container_width=True)
            st.empty()  # Clear the previous chart to create animation effect


def textwithboarder(title, text):
    html_content = f"""
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <h3 style="color:#333333;">{title}</h3>
                                <p>{text}</p>
                            </div>"""
    # Show the Guage of the Nutrients levels
    st.markdown(html_content, unsafe_allow_html=True)


def printWithTitleAndBoarderwithoutTable(title, context):
    return f"""
        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h4 style="color:#333333;">{title}</h4>
            <table>
                    <tr>
                        <th>Status</th>
                        <th>Score(10)</th>
                    </tr>
                    <tr>
                        <td style="color : red;">bad</td>
                        <td style="color : red;">5</td>
                    </tr>
            </table>
            <h4 style="color:#333333;">Plant Cycle</h4>
            <table>
                    <tr>
                        <th>Current Growth Time</th>
                        <th>Total Germination Time</th>
                    </tr>
                    <tr>
                        <td>2 week</td>
                        <td>4 week</td>
                    </tr>
            </table>
            <h4 style="color:#333333;">Health Status of the Pots</h4>
            <table>
                    <tr>
                        <th>Pot Number</th>
                        <th>Current Crop Health Status</th>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td style="color : red;">bad</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td style="color : orange;">normal</td>
                    </tr>
            </table>
        </div>
        """


def printWithTitleAndBoarder1(title, context):
    return f"""
        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h3 style="color:#333333;">{title}</h3>
            <h5>{context}</h5>
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

def SimulationConstructor():
    import pandas as pd
    import numpy as np

    def generate_logical_random_data(num_subplots, generation, pot_number):

        subpot_numbers = [f'SubPot{i + 1}' for i in range(num_subplots)]

        # Set max values
        max_plant_height = 167
        max_leaf_count = 7
        max_longest_leaf = 110

        # Generate one random value for plant height
        reference_plant_height = np.random.uniform(0.9 * max_plant_height, max_plant_height)

        # Generate traits based on the reference plant height
        plant_heights = np.round(
            np.random.uniform(0.9 * reference_plant_height, reference_plant_height, size=num_subplots))
        longest_leaves = np.round(np.random.uniform(0.9 * max_longest_leaf, max_longest_leaf, size=num_subplots))
        leaf_counts = np.round(np.random.uniform(0.9 * max_leaf_count, max_leaf_count, size=num_subplots))

        # Determine status based on percentage distribution
        num_good = int(0.23 * num_subplots)
        num_normal = int(0.13 * num_subplots)
        num_bad = num_subplots - num_good - num_normal

        statuses = np.array(['Good'] * num_good + ['Normal'] * num_normal + ['Bad'] * num_bad)
        np.random.shuffle(statuses)

        data = {
            'subpotnumber': subpot_numbers,
            'longestleaf': longest_leaves,
            'plantheight': plant_heights,
            'leafcount': leaf_counts,
            'status': statuses
        }

        df = pd.DataFrame(data)
        filename = f'Dataset/Pock choy /Generation{generation}_pot{pot_number}_Simulation.csv'
        df.to_csv(filename, index=False)

        return df

    # Main Streamlit app



    st.markdown(printWithTitleAndBoarder1('Simulation' , """Experiment with various nutrient levels and observe their impact on the week4 outcomes.""") , unsafe_allow_html=True)

    optionpot = st.selectbox('Select the pot:', (1, 2))
    # Your dataframe

    if optionpot == 1:
        # Replace 'Dataset/Pock choy /Generation3_pot1.csv' with the actual path to your CSV file
        file_path = 'Dataset/Pock choy /Generation3_pot1.csv'

    if optionpot == 2:
        file_path = 'Dataset/Pock choy /Generation3_pot2.csv'
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Define a mapping for status to color
    status_color_mapping = {'good': 'green', 'normal': 'orange', 'bad': 'red'}

    # Create a dictionary with pot number as keys and color as values
    pot_color_dict = {}

    def update_status(leaf_count, benchmark=10):
        if 8 <= leaf_count <= 10:
            return 'Good'
        elif 7 <= leaf_count <= 8:
            return 'Normal'
        else:
            return 'Bad'

    df['status'] = df['leafcount'].apply(update_status)
    for index, row in df.iterrows():
        pot_number = row['subpotnumber']
        status = row['status'].lower()  # Convert to lowercase for case-insensitivity
        color = status_color_mapping.get(status,
                                         'unknown')  # Default to 'unknown' if status is not one of the specified values
        pot_color_dict[pot_number] = color
    dataframe = pot_color_dict
    col1, col2 = st.columns(2)

    # Sliders in the first column
    temperature = col1.slider("Temperature (°C)", min_value=0, max_value=100, value=25, step=1)
    salinity = col1.slider("Salinity", min_value=0, max_value=50, value=25, step=1)
    tds = col1.slider("TDS (ppm)", min_value=0, max_value=1000, value=500, step=10)

    # Sliders in the second column
    orp = col2.slider("ORP (mV)", min_value=0, max_value=1000, value=500, step=10)
    sr = col2.slider("Sr", min_value=0, max_value=100, value=50, step=1)
    ec = col2.slider("EC (µS/cm)", min_value=0, max_value=100, value=50, step=1)
    ph = col2.slider("pH", min_value=0, max_value=14, value=7, step=1)


    col1 , col2 , col3 , col4, col5  = st.columns(5)
    import time
    if col3.button('_______Apply_______'):
        # Generate and save logical data for Generation 3, Pot 1
        generation_3_pot_1 = generate_logical_random_data(num_subplots=40, generation=3, pot_number=1)
        #st.write('Generated and Saved CSV for Generation 3, Pot 1:', generation_3_pot_1)

        # Generate and save logical data for Generation 3, Pot 2
        generation_3_pot_2 = generate_logical_random_data(num_subplots=40, generation=3, pot_number=2)
        #st.write('Generated and Saved CSV for Generation 3, Pot 2:', generation_3_pot_2)

    if optionpot == 1:
        # Replace 'Dataset/Pock choy /Generation3_pot1.csv' with the actual path to your CSV file
        file_path = 'Dataset/Pock choy /Generation3_pot1_Simulation.csv'

    if optionpot == 2:
        file_path = 'Dataset/Pock choy /Generation3_pot2_Simulation.csv'
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Define a mapping for status to color
    status_color_mapping = {'good': 'green', 'normal': 'orange', 'bad': 'red'}

    # Create a dictionary with pot number as keys and color as values
    pot_color_dict = {}

    def update_status(leaf_count, benchmark=10):
        if 8 <= leaf_count <= 10:
            return 'Good'
        elif 7 <= leaf_count <= 8:
            return 'Normal'
        else:
            return 'Bad'

    df['status'] = df['leafcount'].apply(update_status)
    for index, row in df.iterrows():
        pot_number = row['subpotnumber']
        status = row['status'].lower()  # Convert to lowercase for case-insensitivity
        color = status_color_mapping.get(status,
                                         'unknown')  # Default to 'unknown' if status is not one of the specified values
        pot_color_dict[pot_number] = color
    dataframe = pot_color_dict


    col1, col2 = st.columns(2)
    with col1:
        css_styles = """
                    <style>
                        .button-container {
                            display: grid;
                            grid-template-columns: repeat(8, 1fr);
                            gap: 10px;
                            border: 2px solid #ddd; /* Border around the button container */
                            padding: 10px; /* Add some padding for better appearance */
                        }
                        .button {
                            width: 100%;
                            height: 70px;
                            background-color: #eee;
                            color: #333;
                            font-size: 10px;
                            font-weight: bold;
                            border: 2px solid #ddd;
                            border-radius: 55px;
                            cursor: pointer;
                        }
                    </style>
                """
        # Display CSS styles
        st.markdown(css_styles, unsafe_allow_html=True)

        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1_Simulation.csv')
        # Create button grid
        button_container = f"""<div style="border: 2px solid #333333; padding:10px; border-radius:5px;">     <p style='text-align: center'>Pot  {optionpot}</p>  <div class='button-container'>"""
        for key, value in dataframe.items():
            # Use Streamlit's button widget with a callback to display text on click
            button_container += f"""<button class='button' style='background-color: {value}; border-color: {value}; color: white'
                                       onclick='st.write("{key} clicked!")'>{key}</button>"""
        button_container += "</div> </div>"

        # Display button grid
        st.markdown(button_container, unsafe_allow_html=True)

    with col2:
        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1_Simulation.csv')
        selectpot = st.selectbox('Select the SubPot Number', range(1, 41))
        subpot = f"SubPot{selectpot}"
        filtered_df = df[df['subpotnumber'] == subpot]
        html_content = f"""
                    <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                        <h2 style="color: {dataframe[subpot]}; ">Health Crop Status: {filtered_df['status'].values[0]}</h2>
                        <h2>Current Crop Traits</h2>
                        <table>
                            <tr>
                                <th>Leaf Count</th>
                                <th>Longest Leaf (mm)</th>
                                <th>Plant Height (mm)</th>
                            </tr>
                            <tr>
                                <td>{filtered_df['leafcount'].values[0]}</td>
                                <td>{filtered_df['longestleaf'].values[0]}</td>
                                <td>{filtered_df['plantheight'].values[0]}</td>
                            </tr>
                        </table>
                        <h2>Crop Traits at week4</h2>
                        <table border='1'>
                            <tr>
                                <th>Leaf Count</th>
                                <th>Longest Leaf (mm)</th>
                                <th>Plant Height (mm)</th>
                            </tr>
                            <tr>
                                <td>{filtered_df['leafcount'].values[0] + 3}</td>
                                <td>{filtered_df['longestleaf'].values[0] + 22}</td>
                                <td>{filtered_df['plantheight'].values[0] + 44}</td>
                            </tr>
                        </table>
                    </div>
                    """
        st.markdown(html_content, unsafe_allow_html=True)

