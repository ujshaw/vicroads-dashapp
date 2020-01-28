import plotly.graph_objects as go

mapbox_access_token = open(".mapbox_token").read()

fig = go.Figure(go.Scattermapbox(
        lat=['-37.840935'],
        lon=['144.946457'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=14
        ),
        text=['Melbourne'],
    ))

fig.update_layout(
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=-37,
            lon=145.4
        ),
        pitch=0,
        zoom=5.5
    )
)

fig.show()