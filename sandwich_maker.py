class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < quantity:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Updates machine resources and returns the sandwich."""
        if self.check_resources(order_ingredients):
            for ingredient, quantity in order_ingredients.items():
                self.machine_resources[ingredient] -= quantity
            return f"Here is your {sandwich_size} sandwich!"
        else:
            return "Sorry, we don't have enough ingredients to make your sandwich. Please choose another size or type."