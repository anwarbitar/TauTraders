import random

class CryptoTradingBot:
    def __init__(self):
        self.balance = 10000  # Starting balance in USD
        self.crypto_balance = 0  # Starting cryptocurrency balance
        self.current_price = 0  # Current price of the cryptocurrency

    def fetch_price(self):
        # Simulate fetching the current price from an exchange API
        self.current_price = random.uniform(50, 150)  # Replace with real API calls

    def buy_crypto(self, amount):
        # Simulate buying cryptocurrency
        cost = amount * self.current_price
        if cost <= self.balance:
            self.crypto_balance += amount
            self.balance -= cost

    def sell_crypto(self, amount):
        # Simulate selling cryptocurrency
        if amount <= self.crypto_balance:
            revenue = amount * self.current_price
            self.crypto_balance -= amount
            self.balance += revenue

    def run_strategy(self):
        # Implement our trading strategy here
        # This is where we would analyze data and decide when to buy or sell
        # For demonstration purposes, we'll use a random strategy
        if random.random() > 0.5:
            self.buy_crypto(1)
        else:
            self.sell_crypto(1)

if __name__ == "__main__":
    bot = CryptoTradingBot()

    for _ in range(10):
        bot.fetch_price()
        bot.run_strategy()
        print(f"Balance: ${bot.balance:.2f}, Crypto Balance: {bot.crypto_balance:.2f}")

