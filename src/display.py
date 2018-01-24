import json
from src.retrieve.iextrading import IexData
import time, datetime


# Format large numbers to millions, billions, and trillions
def format_cap(value):
    if value is None:
        return '\t-'
    if value > 1000000000000:
        return "{0:+.1f}T".format(value / 1000000000000)
    elif value > 1000000000:
        return "{0:+.1f}B".format(value / 1000000000)
    elif value > 1000000:
        return "{0:+.1f}M".format(value / 1000000)
    elif value < -1000000000000:
        return "{0:+.1f}T".format(value / 1000000000000)
    elif value < -1000000000:
        return "{0:+.1f}B".format(value / 1000000000)
    elif value < -1000000:
        return "{0:+.1f}M".format(value / 1000000)
    else:
        return str(value)


# Pass in YYYY-mm-DD formatted string and return Quarter ' Year
def get_quarter(day):
    # format passed in string
    time = datetime.datetime.strptime(day, '%Y-%m-%d')

    # from last year 12-31 to this year 1-31
    if (time.day >= 31 and time.month == 12) or (time.day <= 31 and time.month == 1):
        return "Q4'" + time.strftime('%y')
    # from 3-31 to 4-30
    elif (time.day >= 31 and time.month == 3) or (time.day <= 30 and time.month == 4):
        return "Q1'" + time.strftime('%y')
    # from 6-30 to 7-31
    elif (time.day >= 30 and time.month == 6) or (time.day <= 31 and time.month == 7):
        return "Q2'" + time.strftime('%y')
    # from 9-30 to 10-31
    elif (time.day >= 30 and time.month == 9) or (time.day <= 31 and time.month == 10):
        return "Q3'" + time.strftime('%y')
    else:
        return 'N/A'


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

    def display_financials(self, index):
        data = self.mIexData.get_financials(index)
        if data == []:
            print("Error, could not read data")
            return

        quarters = data['financials']

        times = "Quarter\t\t"
        netIncome = "Net Income\t"
        totalAssets = "Total Assets"
        totalLiabilities = "Total Liab.\t"
        totalCash = "Total Cash\t"
        totalDebt = "Total Debt\t"
        shEquity = "SH Equity\t"
        cashFlow = "Cash Flow\t"

        for quarter in quarters:
            times += '\t' + get_quarter(quarter['reportDate'])
            netIncome += '\t' + format_cap(quarter['netIncome'])
            totalAssets += '\t' + format_cap(quarter['totalAssets'])
            totalLiabilities += '\t' + format_cap(quarter['totalLiabilities'])
            totalCash += '\t' + format_cap(quarter['totalCash'])
            totalDebt += '\t' + format_cap(quarter['totalDebt'])
            shEquity += '\t' + format_cap(quarter['shareholderEquity'])
            cashFlow += '\t' + format_cap(quarter['cashFlow'])

        divider = ''
        for i in range(len(times)):
            if times[i] == '\t':
                for i in range(0, (i % 4) + 1):
                    divider += '_'
            else:
                divider += '_'
        divider += '_'

        print(times)
        print(divider)
        print(netIncome)
        print(totalAssets)
        print(totalLiabilities)
        print(totalCash)
        print(totalDebt)
        print(shEquity)
        print(cashFlow)

    def display_earnings(self, index):
        data = self.mIexData.get_earnings(index)
        if data == []:
            print("Error, could not read data")
            return

        quarter = "Quarter"
        actual = "Actual"
        estimated = "Est."

        for earning in data['earnings']:
            # When data is none, then fill with dash
            if earning['actualEPS'] is None:
                actual += '\t' + '-' + '\t'
            else:
                actual += '\t' + "{0:.2f}".format(earning['actualEPS'])
            if earning['estimatedEPS'] is None:
                estimated += '\t' + '-' + '\t'
            else:
                estimated += '\t' + "{0:.2f}".format(earning['estimatedEPS'])

            temp_q = list(earning['fiscalPeriod'])
            # Q1 2017 becomes Q1'17
            if len(temp_q) > 3:
                temp_q.pop(len(temp_q) - 3)
                temp_q.pop(len(temp_q) - 3)
                temp_q[len(temp_q) - 3] = "'"

            quarter += '\t' + "".join(temp_q)

        print(quarter)
        print(actual)
        print(estimated)

    def display_stats(self, index):
        data = self.mIexData.get_stats(index)
        if data == []:
            print("Error, could not read data")
            return

        print("Name\t" + data['companyName'])
        print("MC  \t" + format_cap(data['marketcap']))
        print("Beta\t" + "{0:.2f}".format(data['beta']))
