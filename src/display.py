import json
from src.retrieve.iextrading import IexData
import time, datetime


def format_cap(value):
    if value > 1000000000000:
        return "{0:.2f}T".format(value / 1000000000000)
    elif value > 1000000000:
        return "{0:.2f}B".format(value / 1000000000)
    elif value > 1000000:
        return "{0:.2f}M".format(value / 1000000)
    else:
        return value

class Display:
    mIexData = IexData()
    DATE_FORMAT = "%a %b %d %I:%M %p"
    DAY_FORMAT = "%a %b %d"
    # FLOAT_FORMAT = "{0:.2f}"

    # format quote data
    def display_quote(self, index):
        data = self.mIexData.get_quote(index)
        if data == []:
            print("Error, could not read data")
            return

        # Header info
        print(data['symbol'])
        print(data['companyName'])
        print(data['sector'])
        # End Header, print break
        print()

        # Latest delta/price/time
        timePrint = datetime.datetime.fromtimestamp(data['latestUpdate'] / 1000).strftime(self.DATE_FORMAT)
        print("{0:+.2f}% ".format((data['latestPrice'] - data['open']) / data['open'] * 100) + "{0:.2f}".format(data['latestPrice']) + "\t" + timePrint)
        # End Latest, print break
        print()

        # Last open/close
        timePrint = datetime.datetime.fromtimestamp(data['openTime']/1000).strftime(self.DAY_FORMAT)
        print("Open:  " + "{0:.2f}".format(data['open']) + "\t" + timePrint)
        timePrint = datetime.datetime.fromtimestamp(data['closeTime']/1000).strftime(self.DAY_FORMAT)
        print("Close: " + "{0:.2f}".format(data['close']) + "\t" + timePrint)
        # End last open/close, print break
        print()

        # Basic financial
        print("MC: \t" + format_cap(data['marketCap']))
        print("P/E:\t" + str(data['peRatio']))
        print('52H:\t' + str(data['week52High']))
        print('52L:\t' + str(data['week52Low']))

temp  = Display()
temp.display_quote('amd')