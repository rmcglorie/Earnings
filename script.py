import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol (AAPL) and date range
stock_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-06-10'

# Fetch the stock data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Plot the closing price
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'])
plt.title(f'{stock_symbol} Stock Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()

