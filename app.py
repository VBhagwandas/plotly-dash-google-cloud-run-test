import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA]) 
app.title = 'Powered by Tasting Intelligence'

server = app.server

Card = dbc.Card([
    html.Div([html.H2('Card:')]),
    ],  color="dark", outline=True, body=True)

app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(dbc.CardDeck([Card]),
                    width={'size': 9, 'offset': 0})
        ], justify='around'
        ),
    ])

if __name__ == '__main__':
    app.run_server()
