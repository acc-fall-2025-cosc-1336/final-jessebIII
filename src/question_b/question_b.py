class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
    return stocks


def display_stock_purchase_history(stocks):
    print("\n--- Stock List ---")
    print(f"{'Symbol':<10} {'Company Name':<20}")
    print("-" * 30)
    for stock in stocks:
        print(f"{stock.get_symbol():<10} {stock.get_company_name():<20}")


def main():
    continue_program = True
    while continue_program:
        print("\n--- Menu ---")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        
        user_choice = input("Enter your choice (1 or 2): ").strip()
        
        if user_choice == '1':
            stock_list = get_stock_list()
            display_stock_purchase_history(stock_list)
        elif user_choice == '2':
            continue_program = False
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")