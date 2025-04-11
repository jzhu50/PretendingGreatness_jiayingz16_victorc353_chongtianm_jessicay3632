import urllib.request
from urllib.request import Request
from urllib.request import urlopen
import json
import datetime

def getHistoricalTeslaData():
    current_time = datetime.datetime.now()
    url = f"https://financialmodelingprep.com/api/v3/historical-chart/1day/TSLA?from=2010-6-30&to={current_time.year}-{current_time.month}-{current_time.day}&apikey="
    FMP = open("./keys/key_FMP.txt", "r");
    api_key = FMP.read();
    try:
       with urllib.request.urlopen(url + api_key) as response:
          if response.getcode() == 200:
              html = response.read()
              str = html.decode('utf-8')
              data = json.loads(str)
              returner = []
              for i in data:
                  returner.append([i['date'], i['open'], i['close']])
              return returner
          else:
              print(f'Failed to retrieve data {response.status_code}')
    except Exception as e:
        print(f"Exception occurred: {e}")
        return "Failed"

print(getHistoricalTeslaData())