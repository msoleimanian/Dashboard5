import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu


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


def digitaltwinconstructor():
    option2 = option_menu(None, ["Pak choy v.1" , "Pak choy v.2", "Rice", "Aqua"],
                          menu_icon="forward", default_index=0, orientation="horizontal",
                          styles={
                              "container": {"padding": "0!important", "background-color": "#fafafa"},
                              "icon": {"color": "orange", "font-size": "15px"},
                              "nav-link": {"font-size": "15px", "text-align": "right", "margin": "0px",
                                           "--hover-color": "#eee", },
                              "nav-link-selected": {"background-color": "green"},
                          }
                          )
    st.markdown(printCostumTitleAndContenth1("Explore", ""), unsafe_allow_html=True)

    if option2 == "Pack choy v.1":
        st.markdown(printCostumTitleAndContenth1('3D Represent of the Pack Choy Farm ',''), unsafe_allow_html=True)
        # Replace 'your_embed_code' with the actual embed code of your Sketchfab model
        embed_code = """
        <iframe width="800" height="600" src="https://sketchfab.com/3d-models/hydroponic-farming-setup-1486c6b628ba44f8a5e579927f51a7f7/embed" frameborder="0" allow="autoplay; fullscreen; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        """

        # Extract the URL from the embed code
        model_url = embed_code.split('src="')[1].split('"')[0]

        # Embed the Sketchfab model using an iframe
        st.components.v1.iframe(model_url, width=900, height=500)


        st.markdown(printCostumTitleAndContenth1('3D Represent of each pot ',''), unsafe_allow_html=True)
        st.markdown(printCostumTitleAndContenth3('Pot1', ''), unsafe_allow_html=True)
        # Replace 'your_embed_code' with the actual embed code of your Sketchfab model
        embed_code = """
        <iframe width="800" height="600" src="https://sketchfab.com/3d-models/tryout-8-2f68372773374eba820713e6c3b173b2/embed" frameborder="0" allow="autoplay; fullscreen; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        """

        # Extract the URL from the embed code
        model_url = embed_code.split('src="')[1].split('"')[0]

        # Embed the Sketchfab model using an iframe
        st.components.v1.iframe(model_url, width=900, height=500)


        st.markdown(printCostumTitleAndContenth1('2D Represent of each pot ',''), unsafe_allow_html=True)

        # Display the 3D paper with controllable rotation and image texture using st.markdown
        components.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Rectangle with Circles</title>
            <style>
                #rectangle {{
                    position: relative;
                    width: calc(100% - 40px); /* 4 طرف مارجین */
                    height: calc(101vh - 40px); /* 4 طرف مارجین */
                    background-color: gray;
                    margin: 2px; /* مارجین */
                    display: flex;
                    flex-direction: column-reverse; /* قرار دادن مارجین از پایین به بالا */
                }}
    
                .circle {{
                    position: absolute;
                    background-color: white;
                    border-radius: 45%;
                    cursor: pointer; /* اضافه کردن پوینتر دلخواه به دایره‌ها */
                    margin: 5px; /* مارجین */
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
            </style>
        </head>
        <body>
            <div id="rectangle">
                <!-- Circles will be added dynamically using JavaScript -->
            </div>
    
            <script>
                // Number of rows and columns
                var numRows = 5;
                var numCols = 8;
    
                // Size of the rectangle
                var rectWidth = document.getElementById('rectangle').clientWidth;
                var rectHeight = document.getElementById('rectangle').clientHeight;
    
                // Size of each circle
                var circleRadius = 35; // دایره‌ها بزرگتر
    
                // Reference to the rectangle element
                var rectangle = document.getElementById('rectangle');
    
                // Draw circles inside the rectangle
    var circlesData = [
        ['Pot1', 'hsl(30, 70%, 70%)', 'Longest leaf: 12mm        Plant Height: 200mm        Leaf count: 10        Status: Healthy'],
        ['Pot2', 'hsl(60, 70%, 70%)', 'Longest leaf: 15mm        Plant Height: 220mm        Leaf count: 8        Status: Healthy'],
        ['Pot3', 'hsl(90, 70%, 70%)', 'Longest leaf: 10mm        Plant Height: 180mm        Leaf count: 15        Status: Unhealthy'],
        ['Pot4', 'hsl(120, 70%, 70%)', 'Longest leaf: 14mm        Plant Height: 250mm        Leaf count: 12        Status: Healthy'],
        ['Pot5', 'hsl(150, 70%, 70%)', 'Longest leaf: 16mm        Plant Height: 230mm        Leaf count: 9        Status: Healthy'],
        ['Pot6', 'hsl(180, 70%, 70%)', 'Longest leaf: 11mm        Plant Height: 210mm        Leaf count: 13        Status: Unhealthy'],
        ['Pot7', 'hsl(210, 70%, 70%)', 'Longest leaf: 13mm        Plant Height: 240mm        Leaf count: 11        Status: Healthy'],
        ['Pot8', 'hsl(240, 70%, 70%)', 'Longest leaf: 17mm        Plant Height: 260mm        Leaf count: 7        Status: Healthy'],
        ['Pot9', 'hsl(270, 70%, 70%)', 'Longest leaf: 9mm        Plant Height: 190mm        Leaf count: 14        Status: Unhealthy'],
        ['Pot10', 'hsl(300, 70%, 70%)', 'Longest leaf: 14mm        Plant Height: 220mm        Leaf count: 10        Status: Healthy'],
        ['Pot11', 'hsl(330, 70%, 70%)', 'Longest leaf: 15mm        Plant Height: 240mm        Leaf count: 8        Status: Healthy'],
        ['Pot12', 'hsl(0, 70%, 70%)', 'Longest leaf: 13mm        Plant Height: 210mm        Leaf count: 12        Status: Healthy'],
        ['Pot13', 'hsl(30, 70%, 70%)', 'Longest leaf: 16mm        Plant Height: 230mm        Leaf count: 9        Status: Healthy'],
        ['Pot14', 'hsl(60, 70%, 70%)', 'Longest leaf: 10mm        Plant Height: 180mm        Leaf count: 15        Status: Unhealthy'],
        ['Pot15', 'hsl(90, 70%, 70%)', 'Longest leaf: 14mm        Plant Height: 250mm        Leaf count: 12        Status: Healthy'],
        ['Pot16', 'hsl(120, 70%, 70%)', 'Longest leaf: 16mm        Plant Height: 230mm        Leaf count: 9        Status: Healthy'],
        ['Pot17', 'hsl(150, 70%, 70%)', 'Longest leaf: 11mm        Plant Height: 210mm        Leaf count: 13        Status: Unhealthy'],
        ['Pot18', 'hsl(180, 70%, 70%)', 'Longest leaf: 13mm        Plant Height: 240mm        Leaf count: 11        Status: Healthy'],
        ['Pot19', 'hsl(210, 70%, 70%)', 'Longest leaf: 17mm        Plant Height: 260mm        Leaf count: 7        Status: Healthy'],
        ['Pot20', 'hsl(240, 70%, 70%)', 'Longest leaf: 9mm        Plant Height: 190mm        Leaf count: 14        Status: Unhealthy'],
        ['Pot21', 'hsl(270, 70%, 70%)', 'Longest leaf: 14mm        Plant Height: 220mm        Leaf count: 10        Status: Healthy'],
        ['Pot22', 'hsl(300, 70%, 70%)', 'Longest leaf: 15mm        Plant Height: 240mm        Leaf count: 8        Status: Healthy'],
        ['Pot23', 'hsl(330, 70%, 70%)', 'Longest leaf: 13mm        Plant Height: 210mm        Leaf count: 12        Status: Healthy'],
        ['Pot24', 'hsl(0, 70%, 70%)', 'Longest leaf: 16mm        Plant Height: 230mm        Leaf count: 9        Status: Healthy'],
        ['Pot25', 'hsl(30, 70%, 70%)', 'Longest leaf: 10mm        Plant Height: 180mm        Leaf count: 15        Status: Unhealthy'],
        ['Pot26', 'hsl(60, 70%, 70%)', 'Longest leaf: 14mm        Plant Height: 250mm        Leaf count: 12        Status: Healthy'],
        ['Pot27', 'hsl(90, 70%, 70%)', 'Longest leaf: 16mm        Plant Height: 230mm        Leaf count: 9        Status: Healthy'],
        ['Pot28', 'hsl(120, 70%, 70%)', 'Longest leaf: 11mm        Plant Height: 210mm        Leaf count: 13        Status: Unhealthy'],
        ['Pot29', 'hsl(150, 70%, 70%)', 'Longest leaf: 13mm        Plant Height: 240mm        Leaf count: 11        Status: Healthy'],
        ['Pot30', 'hsl(180, 70%, 70%)', 'Longest leaf: 17mm        Plant Height: 260mm        Leaf count: 7        Status: Healthy'],
        ['Pot31', 'hsl(210, 70%, 70%)', 'Longest leaf: 9mm        Plant Height: 190mm        Leaf count: 14        Status: Unhealthy'],
        ['Pot32', 'hsl(240, 70%, 70%)', 'Longest leaf: 14mm        Plant Height: 220mm        Leaf count: 10        Status: Healthy'],
        ['Pot33', 'hsl(270, 70%, 70%)', 'Longest leaf: 15mm        Plant Height: 240mm        Leaf count: 8        Status: Healthy'],
        ['Pot34', 'hsl(300, 70%, 70%)', 'Longest leaf: 13mm        Plant Height: 210mm        Leaf count: 12        Status: Healthy'],
        ['Pot35', 'hsl(330, 70%, 70%)', 'Longest leaf: 16mm        Plant Height: 230mm        Leaf count: 9        Status: Healthy'],
        ['Pot36', 'hsl(0, 70%, 70%)', 'Longest leaf: 10mm        Plant Height: 180mm        Leaf count: 15        Status: Unhealthy'],
        ['Pot37', 'hsl(30, 70%, 70%)', 'Longest leaf: 14mm        Plant Height: 250mm        Leaf count: 12        Status: Healthy'],
        ['Pot38', 'hsl(60, 70%, 70%)', 'Longest leaf: 16mm        Plant Height: 230mm        Leaf count: 9        Status: Healthy'],
        ['Pot39', 'hsl(90, 70%, 70%)', 'Longest leaf: 11mm        Plant Height: 210mm        Leaf count: 13        Status: Unhealthy'],
        ['Pot40', 'hsl(120, 70%, 70%)', 'Longest leaf: 13mm        Plant Height: 240mm        Leaf count: 11        Status: Healthy']
    ];
    
    
                for (var row = 0; row < numRows; row++) {{
                    for (var col = 0; col < numCols; col++) {{
                        var x = col * (rectWidth / numCols) + 5;
                        var y = row * (rectHeight / numRows) + 25;
    
                        var circle = document.createElement('div');
                        circle.className = 'circle';
                        circle.style.width = circle.style.height = circleRadius * 2 + 'px';
                        circle.style.left = x + 'px';
                        circle.style.top = rectHeight - y - circleRadius * 2 + 'px'; // تغییر در محاسبه مختصات Y
    
                        // افزودن دیتا-موقعیت به هر دایره
                        circle.setAttribute('data-x', x);
                        circle.setAttribute('data-y', rectHeight - y - circleRadius * 2);
    
                        // افزودن تابع تاخیری برای رویداد کلیک
                        circle.addEventListener('click', function(event) {{
                            var x = event.target.getAttribute('data-x');
                            var y = event.target.getAttribute('data-y');
                            var text = event.target.getAttribute('data-text');
                            alert(text);
                        }});
    
                        // افزودن متن به یکی از دایره‌ها
                        var text = document.createTextNode('Pot' + (row * numCols + col + 1));
                        circle.appendChild(text);
    
                        // افزودن متن به دیتا-متن دایره
                        var csvText = circlesData[row * numCols + col][2];
                        circle.setAttribute('data-text', csvText);
    
                        // تغییر رنگ بر اساس داده هر پت
                        var color = circlesData[row * numCols + col][1];
                        circle.style.backgroundColor = color;
    
                        rectangle.appendChild(circle);
                    }}
                }}
            </script>
        </body>
        </html>
        """, width=800, height=600)

        st.markdown(printCostumTitleAndContenth1('3D Represent of each crop ',''), unsafe_allow_html=True)
        # Replace 'your_embed_code' with the actual embed code of your Sketchfab model
        embed_code = """
        <iframe width="800" height="600" src="https://sketchfab.com/3d-models/bok-choy-pak-choy-or-chinese-chard-07ad992bab3a4dd494936adeb288dd9d/embed" frameborder="0" allow="autoplay; fullscreen; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        """

        # Extract the URL from the embed code
        model_url = embed_code.split('src="')[1].split('"')[0]

        # Embed the Sketchfab model using an iframe
        st.components.v1.iframe(model_url, width=900, height=500)

    if option2 == "Pack choy v.2":
        import plotly.graph_objects as go
        import pandas as pd
        import numpy as np

        # Function to create 3D greenhouse layout with plants
        def create_greenhouse_layout(rows, cols):
            layout = np.zeros((rows, cols))
            return layout

        # Function to plot 3D greenhouse with plants
        def plot_greenhouse(layout, plant_heights, leaf_counts):
            fig = go.Figure()

            # Plot greenhouse structure
            fig.add_trace(go.Mesh3d(x=[20, 20, 20, 20, -5, -5, -5, -5],
                                    y=[0, 0, 10, 10, 0, 0, 10, 10],
                                    z=[10, 10, 10, 10, 10, 10, 10, 10],  # Extend the bottom surface
                                    opacity=0.5, color='white', name='Greenhouse Structure'))

            fig.add_trace(go.Mesh3d(x=[30, 30, 30, 30, 15, 15, 15, 15],
                                    y=[0, 0, 10, 10, 0, 0, 10, 10],
                                    z=[10, 10, 10, 10, 10, 10, 10, 10],
                                    opacity=0.5, color='lightgray', name='Space between Sets'))

            plant_counter = 1

            # Plot first set of plants
            for i in range(len(layout)):
                for j in range(len(layout[i])):
                    if layout[i, j] == 1:
                        plant_height = plant_heights[i, j]
                        leaf_count = leaf_counts[i, j]

                        # Draw stem (line)
                        fig.add_trace(go.Scatter3d(x=[j + 0.5, j + 0.5],
                                                   y=[i + 0.5, i + 0.5],
                                                   z=[1, 1 + plant_height],
                                                   mode='lines',
                                                   line=dict(color='green', width=3),
                                                   name=f'Plant {plant_counter}',
                                                   customdata=[plant_counter, leaf_count, plant_height]))

                        # Draw plant head (scatter3d markers)
                        fig.add_trace(go.Scatter3d(x=[j + 0.5],
                                                   y=[i + 0.5],
                                                   z=[1 + plant_height],
                                                   mode='markers',
                                                   marker=dict(size=leaf_count, color='green'),
                                                   name=f'Plant {plant_counter}',
                                                   customdata=[plant_counter, leaf_count, plant_height]))

                        plant_counter += 1

            # Plot second set of plants with a distance of 10 units
            for i in range(len(layout)):
                for j in range(len(layout[i])):
                    if layout[i, j] == 1:
                        plant_height = plant_heights[i, j]
                        leaf_count = leaf_counts[i, j]

                        # Draw stem (line) for the second set
                        fig.add_trace(go.Scatter3d(x=[j + 10.5, j + 10.5],
                                                   y=[i + 0.5, i + 0.5],
                                                   z=[1, 1 + plant_height],
                                                   mode='lines',
                                                   line=dict(color='green', width=3),
                                                   name=f'Plant {plant_counter}',
                                                   customdata=[plant_counter, leaf_count, plant_height]))

                        # Draw plant head (scatter3d markers) for the second set
                        fig.add_trace(go.Scatter3d(x=[j + 10.5],
                                                   y=[i + 0.5],
                                                   z=[1 + plant_height],
                                                   mode='markers',
                                                   marker=dict(size=leaf_count, color='green'),
                                                   name=f'Plant {plant_counter}',
                                                   customdata=[plant_counter, leaf_count, plant_height]))

                        plant_counter += 1

            # Set layout properties
            fig.update_layout(scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=1, z=0.5),
                                         xaxis=dict(showgrid=False),
                                         yaxis=dict(showgrid=False),
                                         zaxis=dict(showgrid=False)))

            return fig

        # Streamlit UI
        st.title("Greenhouse 3D Layout")

        # Read plant heights and leaf counts from greenhouse_data.csv
        csv_file = "Dataset/Pock choy /greenhouse_data.csv"
        df = pd.read_csv(csv_file)
        plant_heights = df.pivot(index='Row', columns='Column', values='PlantHeight').values
        leaf_counts = df.pivot(index='Row', columns='Column', values='LeafCount').values

        # Create greenhouse layout
        rows, cols = plant_heights.shape
        greenhouse_layout = create_greenhouse_layout(rows, cols)

        # Checkboxes to represent plants in the greenhouse
        st.write("Select the cells to place plants in the greenhouse:")
        for i in range(rows):
            for j in range(cols):
                greenhouse_layout[i, j] = 1

        # Plot 3D greenhouse
        fig = plot_greenhouse(greenhouse_layout, plant_heights, leaf_counts)
        fig.update_layout(scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=1, z=0.5),
                                     xaxis=dict(showgrid=False),
                                     yaxis=dict(showgrid=False),
                                     zaxis=dict(showgrid=False)),
                          title='Greenhouse 3D Layout',
                          width=800,
                          height=800
                          )

        # Display the 3D plot
        st.plotly_chart(fig)

        # Handle click events
        scatter = next(fig.select_traces(selector=dict(type='scatter3d')))
        points_data = scatter['customdata']

        # Check if a point is clicked
        if st.button("Show Info"):
            point_clicked = st.selectbox("Select Plant:", [f"Plant {i}" for i in range(1, len(points_data) + 1)])
            plant_number = int(point_clicked.split()[-1])
            leaf_count, plant_height = points_data[plant_number - 1][1:]
            st.write(f"Plant {plant_number} - Leaf Count: {leaf_count}, Plant Height: {plant_height}")



