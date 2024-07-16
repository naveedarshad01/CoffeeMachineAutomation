import turtle
from turtle import Turtle, Screen
import ingredients

# Set up the screen
screen = Screen()
screen.title("Coffee Machine")
screen.setup(width=800, height=600)

# Set up the turtle for drawing
drawer = Turtle()
drawer.hideturtle()
drawer.penup()

# Variables to store user input
user_input = ""
coin_input = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}

def gen_report():
    report = f"Water: {ingredients.resources['water']} ml\nMilk: {ingredients.resources['milk']} ml\nCoffee: {ingredients.resources['coffee']} g\nMoney: ${ingredients.profit}"
    drawer.clear()
    drawer.goto(-200, 200)
    drawer.write(report, align="left", font=("Arial", 16, "normal"))

def check_resources(user_drink):
    drink_ingredients = ingredients.MENU[user_drink]['ingredients']
    for key in drink_ingredients:
        if ingredients.resources[key] < drink_ingredients[key]:
            drawer.clear()
            drawer.goto(-200, 200)
            drawer.write(f"Sorry there is not enough {key}", align="left", font=("Arial", 16, "normal"))
            return False
    return True

def process_payment():
    global coin_input
    total_money = round((coin_input["quarters"] * 0.25) + (coin_input["dimes"] * 0.10) + (coin_input["nickels"] * 0.05) + (coin_input["pennies"] * 0.01), 2)
    return total_money

def transaction_successful(func_drink, user_payment):
    if user_payment < ingredients.MENU[func_drink]['cost']:
        drawer.clear()
        drawer.goto(-200, 200)
        drawer.write("Sorry that is not enough money. Money refunded.", align="left", font=("Arial", 16, "normal"))
        return False
    else:
        ingredients.profit += ingredients.MENU[func_drink]['cost']
        if user_payment > ingredients.MENU[func_drink]['cost']:
            change = round(user_payment - ingredients.MENU[func_drink]['cost'], 2)
            drawer.goto(-200, 200)
            drawer.write(f"Here is ${change} dollars in change.", align="left", font=("Arial", 16, "normal"))
        return True

def make_coffee(func_input):
    user_drink = ingredients.MENU[func_input]['ingredients']
    for key in user_drink:
        ingredients.resources[key] -= user_drink[key]
    drawer.clear()
    drawer.goto(-200, 200)
    drawer.write(f"Here is your {func_input}. Enjoy!", align="left", font=("Arial", 16, "normal"))

def on_button_click(x, y):
    global user_input
    if -350 <= x <= -250 and 100 <= y <= 150:
        user_input = "espresso"
        process_order()
    elif -100 <= x <= 0 and 100 <= y <= 150:
        user_input = "latte"
        process_order()
    elif 150 <= x <= 250 and 100 <= y <= 150:
        user_input = "cappuccino"
        process_order()
    elif -100 <= x <= 100 and -50 <= y <= 0:
        user_input = "report"
        gen_report()

def process_order():
    if user_input == "report":
        gen_report()
    else:
        if check_resources(user_input):
            insert_coins()
            user_money = process_payment()
            if transaction_successful(user_input, user_money):
                make_coffee(user_input)

def setup_buttons():
    button = Turtle()
    button.penup()
    button.hideturtle()

    # Espresso button
    button.goto(-350, 100)
    button.write("Espresso", align="center", font=("Arial", 16, "normal"))
    button.goto(-350, 120)
    button.pendown()
    button.goto(-250, 120)
    button.goto(-250, 150)
    button.goto(-350, 150)
    button.goto(-350, 120)

    # Latte button
    button.penup()
    button.goto(-100, 100)
    button.write("Latte", align="center", font=("Arial", 16, "normal"))
    button.goto(-100, 120)
    button.pendown()
    button.goto(0, 120)
    button.goto(0, 150)
    button.goto(-100, 150)
    button.goto(-100, 120)

    # Cappuccino button
    button.penup()
    button.goto(150, 100)
    button.write("Cappuccino", align="center", font=("Arial", 16, "normal"))
    button.goto(150, 120)
    button.pendown()
    button.goto(250, 120)
    button.goto(250, 150)
    button.goto(150, 150)
    button.goto(150, 120)

    # Report button
    button.penup()
    button.goto(0, -50)
    button.write("Report", align="center", font=("Arial", 16, "normal"))
    button.goto(-100, -30)
    button.pendown()
    button.goto(100, -30)
    button.goto(100, 0)
    button.goto(-100, 0)
    button.goto(-100, -30)

def insert_coins():
    global coin_input
    coin_input["quarters"] = int(screen.numinput("Insert Coins", "Quarters:", minval=0, maxval=10))
    coin_input["dimes"] = int(screen.numinput("Insert Coins", "Dimes:", minval=0, maxval=10))
    coin_input["nickels"] = int(screen.numinput("Insert Coins", "Nickels:", minval=0, maxval=10))
    coin_input["pennies"] = int(screen.numinput("Insert Coins", "Pennies:", minval=0, maxval=10))

# Set up buttons
setup_buttons()

# Set up screen click handler
screen.onscreenclick(on_button_click)

# Main loop
screen.mainloop()