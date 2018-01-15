import json
from src.retrieve.iextrading import IexData

class Display:
    mIexData = IexData()

    # format quote data
    def display_quote(self, index):
        data = json.load(self.mIexData.get_quote(index))
        if data == []:
            print("Error, could not read data")
            return

        print("symbol: " + data['symbol'])