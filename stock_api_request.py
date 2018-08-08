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
#today_date = '2018-07-27'

# API KEY = 7JL79SYMCBQPX0I4
key = "7JL79SYMCBQPX0I4"
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





def load_forex_rate_data(from_curr, to_curr):
    r = requests.get("https://www.alphavantage.co/query?function="
                     "CURRENCY_EXCHANGE_RATE&from_currency=" + from_curr + "&to_currency=" + to_curr + "&apikey=" + key)
    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        forex_rate_json_data = r.json()
        exchange_rate = float(forex_rate_json_data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return exchange_rate



def load_daily_forex_data(from_curr, to_curr):
    r = requests.get("https://www.alphavantage.co/query?function="
                     "FX_DAILY&from_symbol=" + from_curr + "&to_symbol=" + to_curr + "&apikey=" + key)

    if r.status_code != 200:
        print("error" + r.status_code)
    else:
        daily_forex_json_data = r.json()
        return daily_forex_json_data






"""
def load_sector_data():
    # list of sectors

    sectors = ['Telecommunication Services', 'Financials', 'Consumer Staples', 'Industrials', 'Consumer Discretionary',
               'Materials', 'Utilities', 'Energy', 'Health Care', 'Real Estate', 'Information Technology']

    r = requests.get("https://www.alphavantage.co/query?function=SECTOR&apikey=" + key)
    if r.status_code != 200:
        print("error" + r.status_code)

    sector_json_data = r.json()

    #refreshed time
    sector_last_refreshed = sector_json_data['Meta Data']['Last Refreshed']

    #realtime performace
    real_time_perf_sector = []
    for i in sector_json_data['Rank A: Real-Time Performance']:
        real_time_perf_sector.append(sector_json_data['Rank A: Real-Time Performance'][i])

    #1-day perfomrence
    one_day_perf_sector = []
    for i in sector_json_data['Rank B: 1 Day Performance']:
        one_day_perf_sector.append(sector_json_data['Rank B: 1 Day Performance'][i])

    #5 day perf
    five_day_perf_sector = []
    for i in sector_json_data['Rank C: 5 Day Performance']:
        five_day_perf_sector.append(sector_json_data['Rank C: 5 Day Performance'][i])

    #1 month perf
    one_month_perf_sector = []
    for i in sector_json_data['Rank D: 1 Month Performance']:
        one_month_perf_sector.append(sector_json_data['Rank D: 1 Month Performance'][i])

    #3 month perf
    three_month_perf_sector = []
    for i in sector_json_data['Rank E: 3 Month Performance']:
        three_month_perf_sector.append(sector_json_data['Rank E: 3 Month Performance'][i])

    #ytd perf
    ytd_perf_sector = []
    for i in sector_json_data['Rank F: Year-to-Date (YTD) Performance']:
        ytd_perf_sector.append(sector_json_data['Rank F: Year-to-Date (YTD) Performance'][i])

    #one year perf
    one_year_perf_sector = []
    for i in sector_json_data['Rank G: 1 Year Performance']:
        one_year_perf_sector.append(sector_json_data['Rank G: 1 Year Performance'][i])

    # 3 year perf
    three_year_perf_sector = []
    for i in sector_json_data['Rank H: 3 Year Performance']:
        three_year_perf_sector.append(sector_json_data['Rank H: 3 Year Performance'][i])

    sector_data = [sector_last_refreshed, real_time_perf_sector, one_day_perf_sector,
                   five_day_perf_sector, one_month_perf_sector, three_month_perf_sector,
                   ytd_perf_sector, one_year_perf_sector, three_year_perf_sector]

    return sector_json_data['Rank A: Real-Time Performance']
"""
