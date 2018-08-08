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
    data_labels = data[0]
    raw_data = data[1]

    f = open('templates/daily_stock.html', 'w')


    f.write("<head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">"
            "<title>StockAPI-Project</title><link rel=\'stylesheet\' href=\'static/main.css\'>  <link rel=\"stylesheet\" "
            "href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\" "
            "integrity=\"sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO\" crossorigin=\"anonymous\"></head>")

    f.write("<nav class=\"navbar navbar-expand-sm bg-light navbar-light\"><ul class=\"navbar-nav\"><li class=\"nav-item active\">"
            "<a class=\"nav-link\" href=\"{{ url_for('home') }}\">Stock-API Project</a></li><li class=\"nav-item\">"
            "<a class=\"nav-link\" href=\"#\">Daily Stock Data</a></li><li class=\"nav-item\"><a class=\"nav-link\" href=\"#\" "
            ">Sector Data</a</li><li class=\"nav-item\"><a class=\"nav-link\" href=\"#\">Forex Data</a></li><li class=\"nav-item\">"
            "<a class=\"nav-link\" href=\"#\">Crypto Data</a></li></ul></nav>")

    f.write("<body><div class=\"row pt-3 mt-3\"><h1 class=\'col-lg-6 pt-3 text-center\'>" + stock_symbol + "</h1>")
    if float(realtime_points) > float(raw_data[3]):
        f.write("<h2 class=\'col-lg-6 pt-3 text-center text-success\'>" + realtime_points + "</h2></div>")
    else:
        f.write("<h2 class=\'col-lg-6 pt-3 text-center text-danger\'>" + realtime_points + "</h2></div>")

    f.write("<center>")

    f.write(graph_div)


    f.write("<table style=\'width: 100%\'class=\'table-striped\'>")
    for i in range(len(data_labels)):
        f.write("<tr class=\'text-center\'height=\'40px\'><td>" + data_labels[i] + "</td><td>" + raw_data[i] + "</td></tr>")
    f.write("</table>")
    f.write("</center></body>")
    f.close()

    return render_template('daily_stock.html')

#@app.route('/sectors', method=['POST'])
#def show_sectors():
#TODO add sectors option (realtime is the only interesting metric)



#TODO add forex page (same as home page but with two form input)

#TODO add crypto data (same as stock)
if __name__ == '__main__':
    app.run(debug=True)
