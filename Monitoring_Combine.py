import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

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
                        <td style="color : red;">bad</td>
                        <td style="color : red;">4</td>
                        <td style="color : red;">High Risk</td>
                    </tr>
            </table>
            <h4 style="color:#333333;">Health Status of the Pots</h4>
            <table>
                    <tr>
                        <th>Pot Number</th>
                        <th>Predicted Crop Health Status</th>
                        <th>Yield Report</th>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td style="color : red;">bad</td>
                        <td style="color : red;">Predicted Average Weight for Generation 3 at Week4: 670 gram (% 39.09 lower than the best, Best weight grain is 1100 gram.)</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td style="color : red;">bad</td>
                        <td style="color : red;">Predicted Average Weight for Generation 3 at Week4: 690 gram (% 37.27 lower than the best, Best weight grain is 1100 gram.)</td>
                    </tr>
            </table>
        </div>
        """

def createprediction():
    return f"""
    
    
     <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h4 style="color:#333333;">Prediction at week4</h4>
            <div style="display: flex; justify-content: center; align-items: center; height: 5vh;">
                <div style="font-size: 24px; font-weight: bold; background-color: #FF4136; color: #FFFFFF; padding: 10px; border-radius: 5px; animation: pulse 1s infinite alternate;">
                <span style="animation: blink-animation 1s steps(5, start) infinite; color: #FFFF00;">WARNING!</span> Risk Detected!
                </div>
            </div>
            <h4 style="color:#333333;">Health Status of the Pots</h4>
            <table>
                    <tr>
                        <th>Pot Number</th>
                        <th>Predicted status</th>
                        <th>Explanation</th>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td style="color : red;">bad(Average Weight is 670 gram)</td>
                        <td style="color : red;">% 39.09 lower than the best, Best weight grain is 1100 gram.</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td style="color : red;">bad(Average Weight is 690 gram) </td>
                        <td style="color : red;">% 37.27 lower than the best, Best weight grain is 1100 gram.</td>
                    </tr>
            </table>
        </div>
        
            """
    warning_html = """
    <style>
    .warning-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .warning-message {
        font-size: 24px;
        font-weight: bold;
        background-color: #FF4136;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 5px;
        animation: pulse 1s infinite alternate;
    }

    @keyframes pulse {
        from {
            transform: scale(1);
        }
        to {
            transform: scale(1.1);
        }
    }

    .blink {
        animation: blink-animation 1s steps(5, start) infinite;
        color: #FFFF00;
    }

    @keyframes blink-animation {
        to {
            visibility: hidden;
        }
    }
    </style>

    <div class="warning-container">
        <div class="warning-message">
            <span class="blink">WARNING!</span> Risk Detected!
        </div>
    </div>
    """

    st.markdown(warning_html, unsafe_allow_html=True)

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
        animated_chart = animated_gauge_progress_bar(vla, title, rmin, rmax)
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
                        <th>Total Generation Time</th>
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


def MonitConstructor():
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

    if option2 == "Pak choy":

        import pandas as pd
        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(printWithTitleAndBoarderwithoutTable('Current Health Status Generation 3',
                                                             'Farm health Status: Good (7/10)', ),
                        unsafe_allow_html=True)
        with col2:
            st.markdown(createprediction(), unsafe_allow_html=True)

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

        print(pot_color_dict)

        dataframe = pot_color_dict
        # Streamlit app layout
        # Define CSS styles
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

            df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
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
            df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
            dfbenchmark = pd.read_csv('Dataset/Benchmark/Pakchoyparameter.csv')
            subpot = st.selectbox('Select the SubPot Number', df['subpotnumber'].unique())
            filtered_df = df[df['subpotnumber'] == subpot]
            html_content = f"""
            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                <h2 style="color: {dataframe[subpot]}; ">Crop Status: {filtered_df['status'].values[0]}</h2>
                <h2>Crop Traits Status</h2>
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
                        <td> Current </td>
                    </tr>
                    <tr>
                        <td>{filtered_df['leafcount'].values[0] + 1}</td>
                        <td>{filtered_df['longestleaf'].values[0] + 12}</td>
                        <td>{filtered_df['plantheight'].values[0] + 24}</td>
                        <td> Predicted </td>
                    </tr>
                    <tr>
                        <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'leavescount']['Goal'].values[0] }</td>
                        <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'longestleaf']['Goal'].values[0] }</td>
                        <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'plantheight']['Goal'].values[0] }</td>
                        <td> Target </td>
                    </tr>
                </table>
            </div>
            """
            st.markdown(html_content, unsafe_allow_html=True)

        #--------------------------------------------- Real time monitoring

        if optionpot == 1:
            # Replace 'Dataset/Pock choy /Generation3_pot1.csv' with the actual path to your CSV file
            file_path = 'Dataset/Pock choy /Generation3_pot1.csv'

        if optionpot == 2:
            file_path = 'Dataset/Pock choy /Generation3_pot2.csv'
            # Read the CSV file into a pandas DataFrame
        dfmain = pd.read_csv(file_path)

        import plotly.graph_objects as go
        import pandas as pd

        # Load your dataset
        def load_data():
            return pd.read_csv("Dataset/Pock choy /greenhouse_data.csv")

        df = load_data()
        df['Status']  = dfmain['status']
        df['PlantHeight']  = dfmain['plantheight']
        # Function to create 3D plot
        def create_3d_plot(df, key):
            fig = go.Figure()

            # Add plant cones in 3D scatter plot
            for i, row in df.iterrows():
                # Adjust the color based on harvested status or any other criteria you have
                if row['Status'] == 'Bad':
                    color = 'red'

                elif row['Status'] == 'Good':
                    color = 'green'


                else :
                    color = 'lightblue'
                # Add cones for the plants with transparency
                fig.add_trace(go.Cone(
                    x=[row['Row']*10],
                    y=[row['Column']*10],
                    z=[row['PlantHeight']],  # Start of the cone at z=0
                    u=[0],  # Direction of the cone in x-axis
                    v=[0],  # Direction of the cone in y-axis
                    w=[row['PlantHeight']],  # Height of the cone
                    sizemode="absolute",
                    sizeref=row['LeafCount']+10,  # Scale factor for the cones' size
                    colorscale=[[0, color], [1, color]],  # Color of the cone
                    showscale=False,  # Do not show color scale
                    opacity=0.5,  # Adjust the opacity (transparency)
                    anchor="tip"  # Anchor the cone at the top
                ))
                fig.add_trace(go.Scatter3d(
                    x=[row['Row']*10, row['Row']*10],
                    y=[row['Column']*10, row['Column']*10],
                    z=[0, row['PlantHeight']],
                    mode='lines',
                    marker=dict(
                        color=color,
                        size=18,  # Adjust the size of the markers
                        opacity=1,  # Adjust the opacity (transparency)
                        line=dict(
                            color='#ffffff',  # Set the border color to black
                            width=1  # Adjust the border width
                        )
                    ),
                    showlegend=False
                ))

            # Update layout for larger plot with rectangular aspect ratio
            fig.update_layout(
                scene=dict(
                    xaxis_title='Row',
                    yaxis_title='Column',
                    zaxis_title='Plant Height',
                    aspectmode='manual',  # Set aspect ratio manually
                    aspectratio=dict(x=1, y=1, z=1),  # Adjust the aspect ratio as needed
                ),
                width=1100,  # Adjust the width of the plot
                height=1100,  # Adjust the height of the plot
            )

            st.plotly_chart(fig, key=key)

        # Display the 3D plot

        st.write('')
        st.markdown(printWithTitleAndBoarder1('3D Model Farm' , ''),unsafe_allow_html= True)

        with st.expander('3D model'):
            create_3d_plot(df, key='unique_chart3')

        #__------------------------------------------------------------
        st.markdown(textwithboarder('Real-time Traits',
                                    f"""View the latest data from Aqua Fish traits and explore the forecast for the upcoming traits. (latest data)"""))
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            cardCreator('Average Longest Leaf', 88)
        with col2:
            cardCreator('Average Plant Height', 124)
        with col3:
            cardCreator('Average Leaf Count', 5)
        with col4:
            cardCreator('Future Average Longest Leaf', 113)
        with col5:
            cardCreator('Future Average Plant Height', 167)
        with col6:
            cardCreator('Future Average Leaf Count', 8)

        st.write('')

        html_content = f"""
                                                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                                                    <h3 style="color:#333333;">Real-Time Monitoring</h3>
                                                                    <p>Track real-time nutrient levels for Pak Choy.</p>
                                                                </div>
                                                            """
        # Show the Guage of the Nutrients levels
        st.markdown(html_content, unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            guageCreator(24.8, 'Temperature (°C)', 0, 100)
        with col2:
            guageCreator(7.5, 'pH', 0, 14)
        with col3:
            guageCreator(34, 'Salinity', 0, 55)
        with col4:
            guageCreator(390, 'TDS (ppm)', 200, 450)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            guageCreator(210, 'ORP (mV)', 180, 300)
        with col2:
            guageCreator(12, 'Sr', 0, 20)
        with col3:
            guageCreator(13, 'EC', 0, 20)

        # ------------------------------------------------------------

        generation = 'Generation 3'
        pot = f"Pot {optionpot}"

        benchmark = {'Temperature': 24, 'Salinity': 5, 'TDS': 12, 'Orp': 22, 'Sr': 7, 'EC': 13, 'pH': 6}
        dataset = {
            'Generation 3': {
                'Pot 1': {"Temperature": 25.5, "Salinity": 35, "TDS": 400, "Orp": 200, "Sr": 10, "pH": 7.2, 'EC': 13},
                'Pot 2': {"Temperature": 24.8, "Salinity": 34, "TDS": 390, "Orp": 210, "Sr": 12, "pH": 7.5, 'EC': 13}
            },
            'Generation 4': {
                'Pot 1': {"Temperature": 26.2, "Salinity": 36, "TDS": 410, "Orp": 195, "Sr": 9, "pH": 7.0, 'EC': 13},
                'Pot 2': {"Temperature": 25.7, "Salinity": 35.5, "TDS": 405, "Orp": 205, "Sr": 11, "pH": 7.3, 'EC': 13}
            }

        }
        html = f"""

                            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                    <h3 style="color:#333333;">Suggestions</h3>
                                    <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                                <tr>
                                    <th style="border: 2px solid #000; padding: 10px;"></th>
                                    <th style="border: 2px solid #000; padding: 10px;">Temperature</th>
                                    <th style="border: 2px solid #000; padding: 10px;">Salinity</th>
                                    <th style="border: 2px solid #000; padding: 10px;">TDS</th>
                                    <th style="border: 2px solid #000; padding: 10px;">Orp</th>
                                    <th style="border: 2px solid #000; padding: 10px;">Sr</th>    
                                    <th style="border: 2px solid #000; padding: 10px;">EC</th>    
                                    <th style="border: 2px solid #000; padding: 10px;">pH</th>    
                            <tr>
                            <td style='border: 2px solid #000; padding: 10px;'>Benchmark</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Temperature']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Salinity']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['TDS']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Orp']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Sr']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['EC']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['pH']}</td>

                            </tr>

                            <tr>
                            <td style='border: 2px solid #000; padding: 10px;'>Current {generation} and {pot}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Temperature']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Salinity']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['TDS']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Orp']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['Sr']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['EC']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{dataset[generation][pot]['pH']}</td>

                            </tr>


                            <tr><td style='border: 2px solid #000; padding: 10px;'>Intervention plan</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{round(benchmark['Temperature'] - dataset[generation][pot]['Temperature'], 2)}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Salinity'] - dataset[generation][pot]['Salinity']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['TDS'] - dataset[generation][pot]['TDS']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Orp'] - dataset[generation][pot]['Orp']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['Sr'] - dataset[generation][pot]['Sr']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{benchmark['EC'] - dataset[generation][pot]['EC']}</td>
                            <td style='border: 2px solid #000; padding: 10px;'>{round(benchmark['pH'] - dataset[generation][pot]['pH'], 2)}</td>
                            </tr>
                            </table>
                            </div>
                        """

        st.write("")
        st.markdown(html, unsafe_allow_html=True)
        st.write('')
        html_content_with_border = f"""
                            <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                                <h3 style="color:#333333;">Yield Report</h3>
                                <p style="color:green;">Predicted Average Weight Grain for {generation} at week 4: 1011 gram after applay the Intervention plan (% 4 lower than the best, Best weight grain is 1100 gram.)</p>
                                <table style="border-collapse: collapse; width: 100%;">
                                </div>
                                <h3>Crop Traits</h3>
                                <table style="border-collapse: collapse; width: 100%;">
            <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <th style="border: 1px solid #dddddd; padding: 8px;">Generation</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">Pot number</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">Predicted Plant Height(mm)</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">Predicted Leaves Count(mm)</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">Predicted Longest Leaf(mm)</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">Estimated Harvest Weight(gram)</th>
            </tr>
            <tr style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <th style="border: 1px solid #dddddd; padding: 8px;">{generation}</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">{pot}</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">283</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">12</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">184</th>
                <th style="border: 1px solid #dddddd; padding: 8px;">1011</th>
            </tr>
                            </div>
                        """
        col1, col2, col3 = st.columns(3)
        if col2.button("Apply Intervention plan"):
            st.markdown(html_content_with_border, unsafe_allow_html=True)

        # --------------------------------------------------------------

        def color_row(val):
            color = 'green' if val == df['plantheight'].max() else 'orange' if val > df['plantheight'].mean() else 'red'
            return f'background-color: {color}'

        st.write('')
        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
        df1 = df.iloc[:20, :]
        df2 = df.iloc[20:, :]

        # Load the CSV dat

        # Define a function to apply color based on plantheight

        # Apply the color function to the plantheight column

        # Display the styled dataframe
        with st.expander("More Information about Subplots"):
            # Put content inside the expander
            st.write("Here you can find additional information about each subplot.")
            col1, col2 = st.columns(2)
            with col1:
                df1 = df1.style.applymap(color_row, subset=['plantheight'])
                html_table = df1.to_html(index=False, classes='table-style', justify='center')

                # Display the HTML using st.markdown
                st.markdown(html_table, unsafe_allow_html=True)
            with col2:
                df2 = df2.style.applymap(color_row, subset=['plantheight'])
                html_table = df2.to_html(index=False, classes='table-style', justify='center')

                # Display the HTML using st.markdown
                st.markdown(html_table, unsafe_allow_html=True)

        st.write('')
