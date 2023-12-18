################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])

    # Compute the right stock price (average of bid and ask)
    price = (bid_price + ask_price) / 2

    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    return price_a / price_b if price_b != 0 else None


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        # Assume values for testing (replace with actual API response in a real scenario)
        quotes = [
            {"stock": "StockA", "top_bid": {"price": "10.0"}, "top_ask": {"price": "12.0"}},
            {"stock": "StockB", "top_bid": {"price": "5.0"}, "top_ask": {"price": "7.0"}}
        ]

        """ ----------- Update to get the ratio --------------- """
        prices = {}  # Store stock prices in a dictionary

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

            # Store stock prices in the prices dictionary
            prices[stock] = price

        # Check if we have enough data points to calculate the ratio
        if len(prices) >= 2:
            # Get stock names
            stock_names = list(prices.keys())

            # Get stock prices using the dictionary
            price_a = prices[stock_names[0]]
            price_b = prices[stock_names[1]]

            # Call getRatio and print the correct ratio
            ratio = getRatio(price_a, price_b)
            print(f"Stock Info: {stock_names[0]}, {stock_names[1]}")
            print(f"Prices: {price_a}, {price_b}")
            print(f"Ratio: {ratio}")
