from stock_api_request import load_crypto_json, load_daily_json_data, load_forex_json_data
import plotly
import plotly.graph_objs as go

def create_daily_graph(symbol):
    date_time = []
    close_points = []
    json_data = load_daily_json_data(symbol)
    for i in json_data['Time Series (Daily)']:
        date_time.append(i)
        close_points.append(float(json_data['Time Series (Daily)'][i]['4. close']))


    graph = plotly.offline.plot({
        "data": [go.Scatter(x=date_time, y=close_points)],
        "layout": go.Layout(
        autosize=False,
        width=800,
        height=650,)
    }, output_type='div', show_link=False)

    return graph

def create_forex_graph(from_curr, to_curr):
    date_time = []
    close_points = []
    forex_json = load_forex_json_data(from_curr, to_curr)
    for i in forex_json['Time Series FX (Daily)']:
        date_time.append(i)
        close_points.append(float(forex_json['Time Series FX (Daily)'][i]['4. close']))

    graph = plotly.offline.plot({
        "data": [go.Scatter(x=date_time, y=close_points)],
        "layout": go.Layout(
            autosize=False,
            width=800,
            height=650, )
    }, output_type='div', show_link=False)

    return graph



def create_crypto_graph(crypto_curr):
    date_time = []
    close_points = []
    crypto_json = load_crypto_json(crypto_curr)
    for i in crypto_json['Time Series (Digital Currency Daily)']:
        date_time.append(i)
        close_points.append(float(crypto_json['Time Series (Digital Currency Daily)'][i]['4a. close (USD)']))

    graph = plotly.offline.plot({
        "data": [go.Scatter(x=date_time, y=close_points)],
        "layout": go.Layout(
            autosize=False,
            width=800,
            height=650, )
    }, output_type='div', show_link=False)

    return graph
