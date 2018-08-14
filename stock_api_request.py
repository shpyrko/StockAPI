import requests, datetime

#time&date
current_month = datetime.datetime.now().strftime("%m")
current_day = datetime.datetime.now().strftime("%d")
current_year = datetime.datetime.now().strftime("%Y")
current_hour = str(int(datetime.datetime.now().strftime("%H")))
current_minute = str(int(datetime.datetime.now().strftime("%M")))
current_time = current_hour + ":" + current_minute + ":00"
#date_and_time_frmt = today_date + " " + current_time

#today_date = current_year + "-" + current_month + "-" + current_day
today_date = '2018-08-10'

# API KEY = 7JL79SYMCBQPX0I4
key = "7JL79SYMCBQPX0I4"


#stock json
def load_daily_json_data(symbol):
    r = requests.get("https://www.alphavantage.co/query?function="
                   "TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" + key)

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()


# load daily data
def load_daily_data(symbol):
        daily_stock_json_data = load_daily_json_data(symbol)
        final = []

        data_labels = ["Last Time Refreshed", "Day High", "Day Low", "Day Open", "Day Close", "Volume"]

        last_time_refreshed = daily_stock_json_data['Meta Data']['3. Last Refreshed']
        try:
            specific_day_open_points = daily_stock_json_data['Time Series (Daily)'][today_date]['1. open']
        except KeyError:
            return "Market Closed"

        specific_day_high_points = daily_stock_json_data['Time Series (Daily)'][today_date]['2. high']
        specific_day_low_points = daily_stock_json_data['Time Series (Daily)'][today_date]['3. low']
        specific_day_close_points = daily_stock_json_data['Time Series (Daily)'][today_date]['4. close']
        specific_day_volume = daily_stock_json_data['Time Series (Daily)'][today_date]['5. volume']
        data_list = [last_time_refreshed, specific_day_high_points, specific_day_low_points, specific_day_open_points,
                 specific_day_close_points, specific_day_volume]

        for i in range(len(data_labels)):
            final.append((data_labels[i], data_list[i]))
        return final



# current stock price
def load_intraday_stock_data(symbol):
    r = requests.get("https://www.alphavantage.co/query?function="
                     "TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=5min&apikey=" + key)
    intraday_data_points = []
    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        intraday_stock_json_data = r.json()
        for i in intraday_stock_json_data['Time Series (5min)']:
            intraday_data_points.append(intraday_stock_json_data['Time Series (5min)'][i]['4. close'])

        return intraday_data_points[0]


# forex json
def load_forex_json_data(from_curr, to_curr):
    r = requests.get("https://www.alphavantage.co/query?function="
                     "FX_DAILY&from_symbol=" + from_curr + "&to_symbol=" + to_curr + "&apikey=" + key)

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()


# current forex rate
def load_forex_rate_data(from_curr, to_curr):
    r = requests.get("https://www.alphavantage.co/query?function="
                     "CURRENCY_EXCHANGE_RATE&from_currency=" + from_curr + "&to_currency=" + to_curr + "&apikey=" + key)
    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        forex_rate_json_data = r.json()
        exchange_rate = float(forex_rate_json_data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return exchange_rate

# daily forex
def load_daily_forex_data(from_curr, to_curr):
    data_labels = ["Last Time Refreshed", "Day High", "Day Low", "Day Open", "Day Close"]
    final = []
    daily_forex_json_data = load_forex_json_data(from_curr, to_curr)

    forex_last_refreshed = daily_forex_json_data['Meta Data']['5. Last Refreshed']
    forex_open_rate = daily_forex_json_data['Time Series FX (Daily)'][today_date]['1. open']
    forex_high_rate = daily_forex_json_data['Time Series FX (Daily)'][today_date]['2. high']
    forex_low_rate = daily_forex_json_data['Time Series FX (Daily)'][today_date]['3. low']
    forex_close_rate = daily_forex_json_data['Time Series FX (Daily)'][today_date]['4. close']
    data_list = [forex_last_refreshed, forex_high_rate, forex_low_rate, forex_open_rate, forex_close_rate]

    for i in range(len(data_labels)):
        final.append((data_labels[i], data_list[i]))
    return final

# daily crypto
def load_daily_crypto_data(crypto_name):
    r = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY"
                     "&symbol=" + crypto_name + "&market=CNY&apikey=" + key)
    data_labels = ["Last Time Refreshed", "Day High", "Day Low", "Day Open", "Day Close"]
    final = []

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        daily_crypto_json = r.json()
        crypto_last_refreshed = daily_crypto_json['Meta Data']['7. Last Refreshed']

def load_realtime_crypto(crypto_name):
    r = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&"
                     "symbol=" + crypto_name + "&market=USD&apikey=" + key)
    intraday_crypto_points = []
    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        realtime_crypto_json = r.json()
        for i in realtime_crypto_json['Time Series (Digital Currency Intraday)']:
            intraday_crypto_points.append(realtime_crypto_json['Time Series (Digital Currency Intraday)'][i]['1a. price (USD)'])

        return intraday_crypto_points[0]


print(load_daily_crypto_data("BTC"))



