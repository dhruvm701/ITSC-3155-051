def int(param):
    pass
def input(param):
    pass
def print(param):
    pass

class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        return total_amount

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = coins - cost
            print(f"Transaction successful! Your change is ${change:.2f}")
            return True
        else:
            print("Insufficient funds. Please insert more coins.")
            return False