import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def input(param):
    pass
def print(param):
    pass
def int(param):
    pass
def float(param):
    pass

def main():
    print("Welcome to the Ham Sandwich Maker Machine!")
    print("1. Choose Transportation to UNCC")
    print("2. Decide on an Outdoor Activity")
    print("3. UNC Charlotte Course Registration\n")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        distance_to_uncc = float(input("Enter the distance to UNCC in miles: "))
        if distance_to_uncc < 2:
            print("It's a short distance. Consider walking to UNCC.")
        else:
            print("You might want to take the light rail to UNCC.")

    elif choice == 2:
        temperature = int(input("Enter the temperature in degrees Fahrenheit: "))
        chance_of_rain = int(input("Enter the chance of rain in percentage: "))
        if temperature > 70 and chance_of_rain < 50:
            print("It's a great day for Romare Bearden Park.")
        else:
            print("You might want to visit an indoor attraction like the Discovery Place Science Museum.")

    elif choice == 3:
        credits_completed = int(input("Enter the total completed credits: "))
        gpa = float(input("Enter the grade point average: "))
        enrollment_status = int(input("Enter enrollment status (0 for not enrolled, 1 for enrolled): "))
        if credits_completed >= 30 and gpa >= 3.0 and enrollment_status == 1:
            print("You are eligible to register for the course.")
        else:
            print("You are not eligible to register for the course at this time.")

if __name__ == "__main__":
    main()