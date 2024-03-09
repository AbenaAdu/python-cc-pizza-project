#Toppings for pizza
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#Prices for pizza
prices = [2, 6, 1, 3, 2, 7, 2]

#Counting how many $2 slices there are 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#This is the length of the toppings list
num_pizzas = len(toppings)
print(num_pizzas)

print("We sell" , num_pizzas ,"different kinds of pizza!")

