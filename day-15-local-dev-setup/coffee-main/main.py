# TODO: 1. Test
import sys


class Coffee:
    def __init__(self, water, coffee, price, milk=0):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.price = price


class CoffeeMachine:
    def __init__(self):
        self.water = 5000
        self.coffee = 1000
        self.milk = 2500
        self.earnings = 0

    def report(self):
        return f'''--- Machine Report: ---
    Water: {self.water}mL
    Coffee: {self.coffee}g
    Milk: {self.milk}mL
    Earnings: {self.earnings}'''

    def turn_off(self):
        sys.exit()

    def menu(self):
        self.selection = input(
            'What would you like? (espresso/latte/cappuccino): ').lower().strip()
        if self.selection == 'off':
            print('Shutting down.')
            self.turn_off()

        if self.selection == 'report':
            print(self.report())
            return 0

        if self.selection not in ('espresso', 'latte', 'cappuccino', 'off', 'report'):
            print(
                f'{self.selection.capitalize()} is not in the menu. Please choose again.')
            return 0
        else:
            return 1

    def make_coffee(self):
        if self.selection == 'espresso':
            if self.water < espresso.water:
                print('Sorry there is not enough water')
            elif self.coffee < espresso.coffee:
                print('Sorry there is not enough coffee')
            elif self.milk < espresso.milk:
                print('Sorry there is not enough milk')
            else:
                self.water -= espresso.water
                self.coffee -= espresso.coffee
                self.milk -= espresso.milk
                self.earnings += espresso.price

        elif self.selection == 'latte':
            if self.water < latte.water:
                print('Sorry there is not enough water')
            elif self.coffee < latte.coffee:
                print('Sorry there is not enough coffee')
            elif self.milk < latte.milk:
                print('Sorry there is not enough milk')
            else:
                self.water -= latte.water
                self.coffee -= latte.coffee
                self.milk -= latte.milk
                self.earnings += latte.price

        elif self.selection == 'cappuccino':
            if self.water < cappuccino.water:
                print('Sorry there is not enough water')
            elif self.coffee < cappuccino.coffee:
                print('Sorry there is not enough coffee')
            elif self.milk < cappuccino.milk:
                print('Sorry there is not enough milk')
            else:
                self.water -= cappuccino.water
                self.coffee -= cappuccino.coffee
                self.milk -= cappuccino.milk
                self.earnings += cappuccino.price
        print(
            f'{self.selection.capitalize()} is brewed successfully. Please take out your coffee.')

    def run(self):
        if self.menu():
            self.make_coffee()


espresso = Coffee(50, 1.5, 18)
latte = Coffee(200, 24, 2.5, 150)
cappuccino = Coffee(250, 24, 3.0, 100)


coffee_machine = CoffeeMachine()

while True:
    coffee_machine.run()
