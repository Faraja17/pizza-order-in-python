# In this exercise, we'll put together several of the concepts we've learned over the past few weeks to build an app that takes a user's pizza order, calculates the price and prints the order and the total to the console.

# 1. Create a dictionary size_prices that contains pizza sizes (small, medium, large) as keys. Each key should have a list as a value. The list should contain the base price of the pizza and the additional cost per topping. Prices are:
# small: 12 base price, .50 per topping
# medium: 16 base price, .75 per topping
# large: 18 base price, 1 per topping

size_prices = {
    "small": [12, .50],
    "medium": [16, .75],
    "large": [18, 1]
}


# 2. Write a function order_pizza that uses the built-in input() method to get the following values from a user in the console and populate a dictionary named pizza_order.
# customer_name (the customer's name)
# size (desired pizza size - small, medium or large)
# num_toppings (desired number of toppings)
# toppings (desired toppings)
# Using the num_toppings value, write a while loop that uses input() to prompt the user to enter the corresponding number of toppings
# Return the pizza_order dictionary
# Hint! Create the order_pizza dictionary with keys customer_name, size, num_toppings, and toppings at the beginning of the function and set the values to empty values based on the data type that goes in each field.

def order_pizza():
    pizza_order = {
        "customer_name": "",
        "size": "",
        "num_toppings": 0,
        "toppings": []
    }
    pizza_order["customer_name"] = input("What is your name?")
    pizza_order["size"] = input("What size pizza would you like (small, medium, or large?)")
    pizza_order["num_toppings"] = int(input("How many toppings would you like?"))

  
    total_toppings = 0
    while len(pizza_order["toppings"]) < pizza_order["num_toppings"]:
        current_topping = input("What topping would you like?")
        pizza_order["toppings"].append(current_topping)
        total_toppings += 1
    return pizza_order

# 3. Write a function calculate_price that takes the pizza_order dictionary as an argument and uses its values, as well as the values in size_prices, to calculate the price of the pizza ordered by the user based on the size and number of toppings. Return the calculated price.



# 4. Call the 2 functions above and use their return values to print out a nicely-formatted summary of the customer's pizza order and the total price. 
# Ex: 
# Thank you for your order, Liz!
# Order: Small pizza with 3 toppings (mushrooms, onions, olives)
# Total cost: $13.50
# Hint! Use the ''.join() list method to join the pizza toppings list together into a string.


pizza_order = order_pizza()
print(pizza_order)

