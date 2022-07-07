import dash
from dash import html, dcc

# import dash_daq as daq
from dash.dependencies import Input, Output, State


crtevd = dash.Dash(__name__)
crtevd.layout = html.Div(
    [
        html.Div([html.H1("CRT EVD"), html.P()]),
        html.Div([dcc.Graph()]),
    ]
)

if __name__ == "__main__":
    crtevd.run_server(debug=True)
