#Toppings for pizza
toppings = ["pepperoni", 
            "pineapple", 
            "cheese", 
            "sausage", 
            "olives", 
            "anchovies", 
            "mushrooms"]

#Prices for pizza
prices = [2, 6, 1, 3, 2, 7, 2]

#Counting how many $2 slices there are 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#This is the length of the toppings list
num_pizzas = len(toppings)
print(num_pizzas)

#Message for customers
print("We sell" , num_pizzas ,"different kinds of pizza!")

#2D List of the toppings and prices
pizza_and_prices = [[2, "pepperoni"], 
                    [6, "pineapple"], 
                    [1, "cheese"], 
                    [3, "sausage"], 
                    [2, "olives"], 
                    [7, "anchovies"], 
                    [2, "mushrooms"]]

#Sorts pizza in ascending order of price
pizza_and_prices.sort()

#Displays the first pizza topping and price
cheapest_pizza = pizza_and_prices[0]

#Displays the most expensive pizza 
priciest_pizza = pizza_and_prices[-1]

#Removes the anchovies pizza
pizza_and_prices.pop() 

#Inserted new pizza type
pizza_and_prices.insert(4, [2.5, "peppers"])

#The three lowest cost pizzas
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)