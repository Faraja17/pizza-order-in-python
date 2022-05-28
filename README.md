# Pizza Order in Python

Descripton: This is my culminating project for the Girl Develop It! course, Python I: Learning Cohort. 

## Table of contents

- [Overview](#overview)
  - [The Code](#the-code)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)
- [Acknowledgments](#acknowledgments)
- [The Directions](#frontend-mentor---qr-code-component) 

## Overview

Through the creation of this interactive pizza order form, I was able to practice all that I learned during the 12-hour course: data types/espressions, variables, functions, conditionals, loops, and data structures.  The project was designed with a perfect balance of independent challenges and support.  I now feel more confident in writing Python, and I am happy that a lot of what I learned is transferrable to JavaScript, which is my next area of focus.


### The Code

```
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
```

### Links

- Live Site URL: [View the execution of the program here.](https://pythontutor.com/live.html#code=size_prices%20%3D%20%7B%0A%20%20%20%20%22small%22%3A%20%5B12,%20.50%5D,%0A%20%20%20%20%22medium%22%3A%20%5B16,%20.75%5D,%0A%20%20%20%20%22large%22%3A%20%5B18,%201%5D%0A%7D%0A%0Adef%20order_pizza%28%29%3A%0A%20%20%20%20pizza_order%20%3D%20%7B%0A%20%20%20%20%20%20%20%20%22customer_name%22%3A%20%22%22,%0A%20%20%20%20%20%20%20%20%22size%22%3A%20%22%22,%0A%20%20%20%20%20%20%20%20%22num_toppings%22%3A%200,%0A%20%20%20%20%20%20%20%20%22toppings%22%3A%20%5B%5D%0A%20%20%20%20%7D%0A%20%20%20%20pizza_order%5B%22customer_name%22%5D%20%3D%20input%28%22What%20is%20your%20name%3F%20%22%29%0A%20%20%20%20pizza_order%5B%22size%22%5D%20%3D%20input%28%22What%20size%20pizza%20would%20you%20like%20%28small,%20medium,%20or%20large%29%3F%20%22%29%0A%20%20%20%20pizza_order%5B%22num_toppings%22%5D%20%3D%20int%28input%28%22How%20many%20toppings%20would%20you%20like%3F%20%22%29%29%0A%0A%20%20%0A%20%20%20%20total_toppings%20%3D%200%0A%20%20%20%20while%20len%28pizza_order%5B%22toppings%22%5D%29%20%3C%20pizza_order%5B%22num_toppings%22%5D%3A%0A%20%20%20%20%20%20%20%20current_topping%20%3D%20input%28%22What%20topping%20would%20you%20like%3F%20%22%29%0A%20%20%20%20%20%20%20%20pizza_order%5B%22toppings%22%5D.append%28current_topping%29%0A%20%20%20%20%20%20%20%20total_toppings%20%2B%3D%201%0A%0A%20%20%20%20return%20pizza_order%0A%0Adef%20calculate_price%28pizza_order%29%3A%0A%20%20%20%20base_price%20%3D%20%20size_prices%5Bpizza_order%5B%22size%22%5D.lower%28%29%5D%5B0%5D%0A%20%20%20%20per_topping_price%20%3D%20size_prices%5Bpizza_order%5B%22size%22%5D.lower%28%29%5D%5B1%5D%0A%20%20%20%20toppings_total%20%3D%20pizza_order%5B%22num_toppings%22%5D%20*%20per_topping_price%0A%20%20%20%20return%20base_price%20%2B%20toppings_total%0A%0Apizza_order%20%3D%20order_pizza%28%29%0Apizza_price%20%3D%20calculate_price%28pizza_order%29%0A%0Aprint%28%22Thank%20you%20for%20your%20order,%20%22%20%2B%20pizza_order%5B%22customer_name%22%5D%20%2B%20%22!%20%22%29%0Aprint%28%22Order%3A%20%22%20%2B%20pizza_order%5B%22size%22%5D%20%2B%20%22%20pizza%20with%20%22%20%2B%20str%28pizza_order%5B%22num_toppings%22%5D%29%2B%20%22%20toppings%20%28%22%20%2B%20%22,%20%22.join%28pizza_order%5B%22toppings%22%5D%29%20%2B%20%22%29%22%29%0Aprint%28%22Total%20cost%3A%20%24%22%20%2B%20str%28pizza_price%29%29%0A&cumulative=false&curInstr=11&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## My process

Although this was a live class, I missed it, so I followed along with the recording. This actually worked out better, because I was able to pause the video throughout the project and challenge myself to attempt each part of the code independently, including research and debugging, before revealing the solutions. Then, upon viewing the solutions, I compared my code to the solution code, and made necessary corrections and adjustments. Step 3, calculating the total price, was the most challenging for me, but it was extremely fulfilling once I understood the logic of the solution. I wrote very detailed notes for myself in the description section of the commits, so that I may review them to track my learning.  I should have also written brief summaries for each commit.  I will be sure to always do so in the future.


### Built with

- Python

### What I learned

My biggest take-away is to think logically!  I really enjoyed deciphering the logic of the price calculator.

```
def calculate_price(pizza_order):
    base_price =  size_prices[pizza_order["size"].lower()][0]
    per_topping_price = size_prices[pizza_order["size"].lower()][1]
    toppings_total = pizza_order["num_toppings"] * per_topping_price
    return base_price + toppings_total
```

Here is what I wrote about it in the commit description, "It was such an "aha" moment when I understood ` base_price = size_prices[pizza_order['size'].lower()][0]`!  I see that we are filling in the key using the size input!  And we must  be sure to make it all lowercase so that it matches regardless of the user input!. . . .
  My approach using if statements was commendable, and maybe it would have eventually worked if I had continued fixing all the bugs, but I like this approach of first calculating the base price, then the per topping price,  the toppings total, and finally the base price plus the toppings total.  It seems to be more logical, clear, and concise."

### Continued development

I plan to spend more time learning and practicing JavaScript and data structures and algorithims, then I want to come back to Python and continue coding along with the book *Automate the Boring Stuff* by Al Sweigart, and working on more projects in Python. 

### Useful resources

- [Python I: Learning Cohort (6-class series)](https://girldevelopit.com/events/details/girl-develop-it-python-presents-python-i-learning-cohort-6-class-series-1/) - This is the GDI Python course that I just completed.
- [Python II: Learning Cohort (6-class series)](https://girldevelopit.com/events/details/girl-develop-it-python-presents-python-ii-cohort-6-class-series/) - This is an upcoming GDI Python course that will be offered four times per year.

## Author

Faraja Thompson

- [My Personal Website](https://faraja17.github.io/my-website/)
- [My Blog: Teacher to Techie](https://faraja17.github.io/)
- [Faraja Thompson, M.Ed. on LinkedIn](https://www.linkedin.com/in/faraja-thompson-m-ed-70885b8/)

## Acknowledgments

I'd like to acknowledge my son and mentor [DeForestt Thompson](https://github.com/DeForestt).  His steadfast support and encouragement keep me motivated!  Thanks for forcing me to use the command-line, Son <3 <3 <3.
