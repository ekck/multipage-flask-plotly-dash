from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Avocados", "Plums", "Pears"],
        "Amount": [4, 1, 2, 4, 7, 5],
        "City": ["Bomet", "Kisumu", "Nairobi", "Mombasa", "Arusha", "Kampala"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header="Fruit in East Africa"
    description = """
    An academic study of the number of apples, oranges and bananas in the cities of
    East Africa.
    """
    return render_template('multipage.html.jinja', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart2')
def chart2():
    df = pd.DataFrame({
        "Vegetables": ["Lettuce", "Cauliflower", "Carrots", "Lettuce", "Cauliflower", "Carrots"],
        "Amount": [10, 15, 8, 5, 14, 25],
        "City": ["South Africa", "Nigeria", "DRC", "Morocco", "Uganda", "Ethiopia"]
    })

    fig = px.bar(df, x="Vegetables", y="Amount", color="City", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Vegetables in Africa"
    description = """
    Descriptive chart of vegetables in africa.
    """
    return render_template('multipage.html', graphJSON=graphJSON, header=header,description=description)

if __name__=='__main__':
    app.secret_key='1234'
    app.run(debug=True)