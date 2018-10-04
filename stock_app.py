from flask import *
from graph_generator import *
from stock_api_request import *

app = Flask(__name__)

#TODO add more company informtion
#TODO add search bar to daily stock
#TODO add percentage change from open (forex, crypto)
#TODO add advanced analytical graphs for stock (new key) https://plot.ly/python/line-charts/
#TODO Add session with favorites (maybe login)
#TODO maybe incorporate crypto exchange from https://coinswitch.co/tools?utm_source=ph

@app.route('/')
def home():
    return render_template('index_pages/stock_index.html', check = check_time())

@app.route('/forex')
def forex():
    return render_template('index_pages/forex_index.html')

@app.route('/crypto')
def crypto():
    return render_template("index_pages/crypto_index.html")

@app.route('/stock/today/<stock_symbol>', methods=['POST', 'GET'])
def load_today_stock(stock_symbol):
    if stock_symbol == "quote":
        stock_symbol = request.form['stock_name']
    graph_div = create_1_day_stock_graph(stock_symbol)
    realtime_points = load_realtime_stock_price(stock_symbol)
    change_percent = load_change_percent(stock_symbol)
    data = load_today_data(stock_symbol)

    status = float(realtime_points) > float(data[3][1])

    return render_template('daily_pages/daily_stock.html', symbol=stock_symbol, status=status, realtime_points=realtime_points,
                           change_percent=change_percent, graph=graph_div, data=data)

@app.route('/stock/3-months/<stock_symbol>', methods=['GET'])
def load_3_months_stock(stock_symbol):
    graph_div = create_3_months_stock_graph(stock_symbol)
    realtime_points = load_realtime_stock_price(stock_symbol)
    data = load_today_data(stock_symbol)

    status = float(realtime_points) > float(data[3][1])

    return render_template('daily_pages/daily_stock.html', symbol=stock_symbol, status=status, realtime_points=realtime_points,
                           graph=graph_div, data=data)

@app.route('/stock/6-months/<stock_symbol>', methods=['GET'])
def load_6_months_stock(stock_symbol):
    graph_div = create_6_month_stock_graph(stock_symbol)
    realtime_points = load_realtime_stock_price(stock_symbol)
    data = load_today_data(stock_symbol)

    status = float(realtime_points) > float(data[3][1])

    return render_template('daily_pages/daily_stock.html', symbol=stock_symbol, status=status, realtime_points=realtime_points,
                           graph=graph_div, data=data)

@app.route('/stock/1-year/<stock_symbol>', methods=['GET'])
def load_1_year_stock(stock_symbol):
    graph_div = create_1_year_stock_graph(stock_symbol)
    realtime_points = load_realtime_stock_price(stock_symbol)
    data = load_today_data(stock_symbol)

    status = float(realtime_points) > float(data[3][1])

    return render_template('daily_pages/daily_stock.html', symbol=stock_symbol, status=status, realtime_points=realtime_points,
                           graph=graph_div, data=data)

@app.route('/stock/all-time/<stock_symbol>', methods=['GET'])
def load_5_year_stock(stock_symbol):
    graph_div = create_5_year_stock_graph(stock_symbol)
    realtime_points = load_realtime_stock_price(stock_symbol)
    data = load_today_data(stock_symbol)

    status = float(realtime_points) > float(data[3][1])

    return render_template('daily_pages/daily_stock.html', symbol=stock_symbol, status=status, realtime_points=realtime_points,
                           graph=graph_div, data=data)




@app.route('/forex/daily-quotes', methods=['POST'])
def show_forex():
    currency1 = request.form['currency_name_1']
    currency2 = request.form['currency_name_2']
    forex_graph = create_forex_graph(currency1, currency2)
    realtime_forex = load_forex_rate_data(currency1, currency2)
    forex_data = load_daily_forex_data(currency1, currency2)
    status = float(realtime_forex) > float(forex_data[3][1])

    return render_template('daily_pages/daily_forex.html', symbol=currency1 + " / " + currency2, status=status, realtime_points=realtime_forex,
                           graph=forex_graph, data=forex_data)

# crypto does NOT need different graph views
@app.route('/crypto/daily-quotes', methods=['POST'])
def show_crypto():
    crypto_name = request.form['crypto_name']
    crypto_graph = create_crypto_graph(crypto_name)
    realtime_crypto = load_realtime_crypto(crypto_name)
    crypto_data = load_daily_crypto_data(crypto_name)
    status = float(realtime_crypto) > float(crypto_data[3][1])

    return render_template('daily_pages/daily_crypto.html', symbol=crypto_name, status=status, realtime_points=realtime_crypto,
                           graph=crypto_graph, data=crypto_data)


if __name__ == '__main__':
    app.run(debug=True)
