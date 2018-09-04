import requests, datetime

#time&date
current_month = datetime.datetime.now().strftime("%m")
current_day = datetime.datetime.now().strftime("%d")
current_year = datetime.datetime.now().strftime("%Y")
current_hour = str(int(datetime.datetime.now().strftime("%H")))
current_minute = str(int(datetime.datetime.now().strftime("%M")))
current_time = current_hour + ":" + current_minute + ":00"
#date_and_time_frmt = today_date + " " + current_time

today_date = current_year + "-" + current_month + "-" + current_day
#today_date = '2018-08-10'

daily_key = "7JL79SYMCBQPX0I4"
intraday_key = "WFV2JIQ61QD7N0SB"

#checks if market is open returns boolean
def check_time():
    check = False
    if datetime.date(int(current_year), int(current_month), int(current_day)).weekday() > 4:
        check = True
    if int(current_hour) > 17 or int(current_hour) < 9:
        check = True
    return check


#stock json
def load_daily_json_data(symbol):
    r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/quote")

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

def load_change_percent(symbol):
    daily_stock_json_data = load_daily_json_data(symbol)
    change_percent = float(daily_stock_json_data['changePercent']) * 100
    if change_percent >  0:
        output = "+" + str(round(change_percent, 2)) + "%"
    else:
        output = str(round(change_percent, 2)) + "%"
    return output

# load daily data returned as tuple list
def load_today_data(symbol):
        daily_stock_json_data = load_daily_json_data(symbol)
        final = []

        data_labels = ["Last Time Refreshed", "Day High", "Day Low", "Day Open", "Day Close", "Volume"]

        last_time_refreshed = daily_stock_json_data['latestTime']
        specific_day_open_points = daily_stock_json_data['open']
        specific_day_high_points = daily_stock_json_data['high']
        specific_day_low_points = daily_stock_json_data['low']
        specific_day_close_points = daily_stock_json_data['close']
        specific_day_volume = daily_stock_json_data['latestVolume']

        data_list = [last_time_refreshed, specific_day_high_points, specific_day_low_points, specific_day_open_points,
                 specific_day_close_points, specific_day_volume]


        for i in range(len(data_labels)):
            final.append((data_labels[i], data_list[i]))
        return final

# current stock price returned as int
def load_realtime_stock_price(symbol):
    r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/price")
    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

def load_intraday_stock_json(symbol):
    r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/chart/1d")
    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

def load_3_month_stock(symbol):
    r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/chart/3m")

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

def load_6_month_stock(symbol):
    r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/chart/6m")

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

def load_1_year_stock(symbol):
    r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/chart/1y")

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

def load_5_year_stock(symbol):
    r = requests.get("https://api.iextrading.com/1.0/stock/" + symbol + "/chart/5y")

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()



# forex json
def load_forex_json_data(from_curr, to_curr):
    r = requests.get("https://www.alphavantage.co/query?function="
                     "FX_DAILY&from_symbol=" + from_curr + "&to_symbol=" + to_curr + "&apikey=" + daily_key)

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

# current forex rate
def load_forex_rate_data(from_curr, to_curr):
    r = requests.get("https://www.alphavantage.co/query?function="
                     "CURRENCY_EXCHANGE_RATE&from_currency=" + from_curr + "&to_currency=" + to_curr + "&apikey=" +
                     intraday_key)
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

    forex_last_time_refreshed = daily_forex_json_data['Meta Data']['5. Last Refreshed']
    forex_last_day_refreshed = forex_last_time_refreshed[:10]
    forex_open_rate = daily_forex_json_data['Time Series FX (Daily)'][forex_last_day_refreshed]['1. open']
    forex_high_rate = daily_forex_json_data['Time Series FX (Daily)'][forex_last_day_refreshed]['2. high']
    forex_low_rate = daily_forex_json_data['Time Series FX (Daily)'][forex_last_day_refreshed]['3. low']
    forex_close_rate = daily_forex_json_data['Time Series FX (Daily)'][forex_last_day_refreshed]['4. close']
    data_list = [forex_last_time_refreshed, forex_high_rate, forex_low_rate, forex_open_rate, forex_close_rate]

    for i in range(len(data_labels)):
        final.append((data_labels[i], data_list[i]))
    return final

# crypto json
def load_crypto_json(crypto_curr):
    r = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY"
                     "&symbol=" + crypto_curr + "&market=USD&apikey=" + daily_key)

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        return r.json()

# daily crypto
def load_daily_crypto_data(crypto_name):
    r = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY"
                     "&symbol=" + crypto_name + "&market=USD&apikey=" + daily_key)
    data_labels = ["Last Time Refreshed", "Day High", "Day Low", "Day Open", "Day Close"]
    final = []

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        daily_crypto_json = r.json()
        crypto_last_refreshed = daily_crypto_json['Meta Data']['6. Last Refreshed']
        today_date = crypto_last_refreshed[:10]
        crypto_open_points = daily_crypto_json['Time Series (Digital Currency Daily)'][today_date]['1a. open (USD)']
        crypto_high_points = daily_crypto_json['Time Series (Digital Currency Daily)'][today_date]['2a. high (USD)']
        crypto_low_points = daily_crypto_json['Time Series (Digital Currency Daily)'][today_date]['3a. low (USD)']
        crypto_close_points = daily_crypto_json['Time Series (Digital Currency Daily)'][today_date]['4a. close (USD)']
        crypto_volume = daily_crypto_json['Time Series (Digital Currency Daily)'][today_date]['5. volume']
        data_list = [crypto_last_refreshed, crypto_high_points, crypto_low_points, crypto_open_points,
                     crypto_close_points, crypto_volume]

        for i in range(len(data_labels)):
            final.append((data_labels[i], data_list[i]))
        return final


def load_realtime_crypto(crypto_name):
    r = requests.get("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&"
                     "symbol=" + crypto_name + "&market=USD&apikey=" + intraday_key)
    intraday_crypto_points = []
    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        realtime_crypto_json = r.json()
        for i in realtime_crypto_json['Time Series (Digital Currency Intraday)']:
            intraday_crypto_points.append(realtime_crypto_json['Time Series (Digital Currency Intraday)'][i]['1a. price (USD)'])

        return intraday_crypto_points[0]




