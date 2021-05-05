from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Avocados", "Plums", "Pears"],
        "Amount": [4, 1, 2, 4, 7, 5],
        "City": ["Bomet", "Kisumu", "Nairobi", "Mombasa", "Arusha", "Kampala"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('basic.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)