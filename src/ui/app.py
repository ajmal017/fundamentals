# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from src.retrieve.iextrading import IexData


mIexData = IexData()


def get_1day_chart(index):
    data = mIexData.get_chart(index, '1d')
    ret_data = []
    indexes = []
    closes = []
    volumes = []

    for i in range(len(data)):
        indexes.append(i)
        temp = data[i]['average']
        if temp == 0 and i > 0:
            temp = closes[i - 1]
        closes.append(temp)
        volumes.append(data[i]['volume'])

    ret_data.append(indexes)
    ret_data.append(closes)
    ret_data.append(volumes)

    return ret_data


app = dash.Dash()

dat = get_1day_chart('amd')
quote = mIexData.get_quote('amd')
app.layout = html.Div(children=[
    html.Div([
        html.H3(quote['symbol'], id='symbol'),
        html.P(''''quote['companyName']'
                'quote['sector']'
                'str(quote['latestPrice'])'
                'str(quote['peRatio'])' ''',
               id='info')
    ]),

    dcc.Graph(
        id='prices-data',
        figure={
            'data': [
                {'x': dat[0], 'y': dat[1], 'type': 'line', 'name': 'Price'},
                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'AMD',
                'autosize': False,
                'width': 1000,
                'height': 300,
                'margin': {
                    'l': 50,
                    'r': 50,
                    'b': 50,
                    't': 50,
                    'pad': 4
                }
            }
        }
    ),
    dcc.Graph(
        id='volume-data',
        figure={
            'data': [
                {'x': dat[0], 'y': dat[2], 'type': 'bar', 'name': 'Volume'},
            ],
            'layout': {
                'autosize': False,
                'width': 1000,
                'height': 200,
                'margin': {
                    'l': 50,
                    'r': 50,
                    'b': 50,
                    't': 0,
                    'pad': 4
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)