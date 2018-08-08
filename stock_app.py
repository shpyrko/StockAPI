from flask import *
from graph_generator import create_daily_graph
from stock_api_request import load_daily_data, load_intraday_stock_data

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


#TODO add different graph views for stock
@app.route('/stock', methods=['POST'])
def show_daily_stock():
    stock_symbol = request.form['stock_name']
    graph_div = create_daily_graph(stock_symbol)
    realtime_points = load_intraday_stock_data(stock_symbol)
    data = load_daily_data(stock_symbol)

    status = float(realtime_points) > float(data[3][1])

    return render_template('daily_stock.html', symbol=stock_symbol, status=status, realtime_points=realtime_points,
                           graph=graph_div, data=data)

#@app.route('/sectors', method=['POST'])
#def show_sectors():
#TODO add sectors option (realtime is the only interesting metric)



#TODO add forex page (same as home page but with two form input)

#TODO add crypto data (same as stock)
if __name__ == '__main__':
    app.run(debug=True)
