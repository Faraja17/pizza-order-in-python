from os import truncate


size_prices = {
    "small": [12, .50],
    "medium": [16, .75],
    "large": [18, 1]
}

def order_pizza():
    pizza_order = {
        "customer_name": "",
        "size": "",
        "num_toppings": 0,
        "toppings": []
    }
    pizza_order["customer_name"] = input("What is your name? ")
    pizza_order["size"] = input("What size pizza would you like (small, medium, or large)? ")
    pizza_order["num_toppings"] = int(input("How many toppings would you like? "))

  
    total_toppings = 0
    while len(pizza_order["toppings"]) < pizza_order["num_toppings"]:
        current_topping = input("What topping would you like? ")
        pizza_order["toppings"].append(current_topping)
        total_toppings += 1

    return pizza_order

def calculate_price(pizza_order):
    base_price =  size_prices[pizza_order["size"].lower()][0]
    per_topping_price = size_prices[pizza_order["size"].lower()][1]
    toppings_total = pizza_order["num_toppings"] * per_topping_price
    return base_price + toppings_total

pizza_order = order_pizza()
pizza_price = calculate_price(pizza_order)

print("Thank you for your order, " + pizza_order["customer_name"] + "! ")
print("Order: " + pizza_order["size"] + " pizza with " + str(pizza_order["num_toppings"])+ " toppings (" + ", ".join(pizza_order["toppings"]) + ")")
print("Total cost: $" + str(pizza_price))
