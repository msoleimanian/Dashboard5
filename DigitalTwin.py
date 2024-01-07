import streamlit as st
import streamlit.components.v1 as components


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