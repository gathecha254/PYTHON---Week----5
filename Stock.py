class Stock:  
    def __init__(self, symbol, name, price, quantity):  
        # Initialize stock attributes  
        self.symbol = symbol          
        self.name = name              
        self.price = price            
        self.quantity = quantity      

    def buy(self, shares):  
        # Buy a number of shares  
        self.quantity += shares  
        print(f"Bought {shares} shares of {self.name}.")  

    def sell(self, shares):  
        # Sell a number of shares, ensuring quantity is not exceeded  
        if shares > self.quantity:  
            print("Not enough shares to sell.")  
        else:  
            self.quantity -= shares  
            print(f"Sold {shares} shares of {self.name}.")  

    def get_value(self):  
        # Calculate total value of stocks owned  
        return self.price * self.quantity  

    def __str__(self):  
        # Return stock details as a string  
        return f"{self.name} ({self.symbol}): ${self.price:.2f} | Shares owned: {self.quantity}"  


# Inheritance
class TechStock(Stock):  
    def __init__(self, symbol, name, price, quantity, market_cap):  
        super().__init__(symbol, name, price, quantity)  
        self.market_cap = market_cap  # Market capitalization  

    def get_market_cap(self):  
        # Return market capitalization  
        return f"Market Capitalization of {self.name}: ${self.market_cap:.2f}"  

    def __str__(self):  
        # Include market cap in string representation  
        parent_str = super().__str__()  
        return f"{parent_str} | Market Cap: ${self.market_cap:.2f}"  
 
if __name__ == "__main__":  
    # stock instance  
    stock1 = Stock("AAPL", "Apple Inc.", 175.00, 10)  
    print(stock1)  
    stock1.buy(5)  
    print(f"Total value of stocks: ${stock1.get_value():.2f}")  
    
    # tech stock instance  
    tech_stock1 = TechStock("GOOGL", "Alphabet Inc.", 2750.00, 5, 1800_000_000_000)  
    print(tech_stock1)  
    tech_stock1.sell(2)  
    print(tech_stock1.get_market_cap())  
