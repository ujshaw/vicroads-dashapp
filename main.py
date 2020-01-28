import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

from dash.dependencies import Input, Output
from plotly import graph_objs as go
from plotly.graph_objs import *
from datetime import datetime as dt


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Mapbox Public Token
mapbox_access_token = "pk.eyJ1IjoidWpzaGF3IiwiYSI6ImNrNXg4NGlzYTA2ZmczaHI3ejE0cXZzcmoifQ.isz4NhCTX5wj8qshctJGRA"

# Dictionary of important locations in New York
list_of_locations = {
    "Melbourne": {"lat": -37.814, "lon": 144.963},
    "Geelong": {"lat": -38.147, "lon": 144.361},
    "Ballarat": {"lat": -37.580, "lon": 143.848},
    "Bendigo": {"lat": -36.759, "lon": 144.280},
    "Shepparton": {"lat": -36.381, "lon": 145.399},
    "Melton": {"lat": -37.683, "lon": 144.583},
    "Mildura": {"lat": -34.185, "lon": 142.166},
    "Warrnambool": {"lat": -38.383, "lon": 142.483},
    "Sunbury": {"lat": -37.577, "lon": 144.731},
}

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()



app.run_server(debug=True)