menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 600,
    "milk": 500,
    "coffee": 300,
}
balance = 0
continue_order = True
correct_option = True

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}
profit = 0

def printReport():
    for key in resources:
        if key == 'water' or key == 'milk':
            print(f"{key} : {resources[key]}ml")
        else:
             print(f"{key} : {resources[key]}g")
    print(f"Money : ${balance}")
        
def calculateMoney(q,d,n,p):
    my_money = ( p * coins['penny'] ) + ( d * coins['dime'] ) + ( q * coins['quarter'] ) + ( n * coins['nickel'] )
    return my_money
      
def calculateChange(item, cash):
    if cash > menu[item]['cost']:
        change = round(cash - menu[item]['cost'], 2)
        resources['water'] = resources['water'] - menu[item]['ingredients']['water']
        resources['milk'] = resources['milk'] - menu[item]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - menu[item]['ingredients']['coffee']
        return f"Here is your {change}, enjoy your {item}"
    else:
        return "sorry your money is not enough, money refunded"

def transaction(item, cash):
    change = 0
    if cash > menu[item]['cost']:
        change = cash - menu[item]['cost']
        resources['water'] = resources['water'] - menu[item]['ingredients']['water']
        if item != "espresso":
            resources['milk'] = resources['milk'] - menu[item]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - menu[item]['ingredients']['coffee']
        return True, cash, change
    else:
        return False, cash, change

    
while continue_order:    
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'report':
        printReport()
    elif order == 'off':
        continue_order = False
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if resources['water'] < menu[order]['ingredients']['water']:
            print(f"sorry there is no enough water")
        elif order != "espresso" and resources['milk'] < menu[order]['ingredients']['milk']:
            print(f"sorry there is no enough milk")
        elif resources['coffee'] < menu[order]['ingredients']['coffee']:
            print(f"sorry there is no enough coffee")
        else:
            print("please insert some coins")
            quarters = float(input('how many quarters?: '))
            dimes = float(input('how many dimes?: '))
            nickels = float(input('how many nickels?: '))
            pennies = float(input('how many pennies?: '))
            customer_cash = calculateMoney(quarters, dimes, nickels, pennies)
            # print(customer_cash)
            success, cash, change = transaction(order, customer_cash)
            # print(success)
            # print(cash)
            # print(change)
            if success:
                if change > 0:
                    print(f"Here is ${change:.2f} in change")
                    print(f"Here is {order}")
                balance += menu[order]['cost']
            else:
                print(f"sorry there is no enough money")
    else:
        while correct_option:
            print("choose a correct option")
            correct_option = False