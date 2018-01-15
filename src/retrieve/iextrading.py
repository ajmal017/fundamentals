import requests


# “Data provided for free by IEX.”
# In terms of service  https://iextrading.com/api-exhibit-a
class IexData:
    ROOT_URL = "https://api.iextrading.com/1.0/"

    # https://iextrading.com/developer/docs/#quote
    def get_quote(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/quote?displayPercent=true")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#chart
    # 1d, 1m, 3m, 6m, ytd, 1y, 2y, 5y
    def get_chart(self, index, interval):
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/chart/" + interval)
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#company
    def get_company(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/company")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#key-stats
    def get_stats(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/stats")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#peers
    # There is also relevant if there are no direct peers.
    def get_peers(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/peers")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#news
    def get_news(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/news")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#financials
    def get_financials(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/financials")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#earnings
    def get_earnings(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/earnings")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()

    # https://iextrading.com/developer/docs/#dividends
    def get_dividends(self, index):
        # HTTPS GET for JSON
        request = requests.get(self.ROOT_URL + "/stock/" + index + "/dividends")
        # When an error occurs when retrieving the data, return empty data
        if request.status_code > 299 or request.status_code < 200:
            print("Error retrieving: " + request.status_code)
            return []
        # Return raw data
        return request.json()
